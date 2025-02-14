from collections import defaultdict
from datetime import datetime
from importlib import import_module

from dateutil import parser
from sqlalchemy import inspect, text


class ImportExportBase:
    def get_model(self, model_path):
        """
        Dynamically imports and returns a class from a given module path.
        Parameters:
            model_path (str): The dot-separated path to the module and class (e.g., "module.submodule.ClassName").
        Returns: The class object referred to by model_path
        """
        module_path, class_name = model_path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, class_name)


class QueryExport(ImportExportBase):
    def __init__(self, context: dict):
        """
        Initializes the QueryExport instance.
        Parameters:
        context (dict): The context containing database connection information and other relevant settings.
        """
        self.context = context
        self.db_types = {
            "SQL": self.get_data_sql,
            "NO_SQL": self.get_data_no_sql,
        }
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def get_data(self, model_path, fields, date_init, date_finish, context):
        """
        Fetches data from the database (SQL or NoSQL) based on the provided model path, fields, and context.
        Parameters:
        model_path (str): The path to the model class.
        fields (list): A list of field names to be fetched.
        date_init(datetime): The start date for the query.
        date_finish(datetime): The end date for the query.
        context (dict): The context for the database operation.
        Returns: The fetched data.
        """
        model = self.get_model(model_path)
        return self.db_types[self.db_type](model, model_path, fields, date_init, date_finish, context)

    def parse_date(self, date):
        result = None
        try:
            result = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            result = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        return parser.parse(result.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"))

    def get_data_no_sql(self, model, model_path, fields, start_date, end_date, context):
        """
        Fetches data from a NoSQL database.
        Parameters:
        model: The model class for the NoSQL operation.
        model_path (str): The path to the model class.
        fields (list): A list of field names to be fetched.
        date_init(datetime): The start date for the query.
        date_finish(datetime): The end date for the query.
        context (dict): The context for the NoSQL database operation.
        Returns: Data retrieved from the NoSQL database.
        """
        exclude = {"_id" if key == "id" else key: False for key in set(model._fields.keys()) - set(fields)}
        db = model.db
        query_filter = {
            "context.tenant": context["tenant"],
            "audit.created_at": {
                "$gte": self.parse_date(start_date),
                "$lte": self.parse_date(end_date),
            },
        }
        cursor = db[model._meta["collection"]].find(
            query_filter,
            projection=exclude,
        )
        result = list(cursor)
        return result

    def get_data_sql(self, model, model_path, fields, start_date, end_date, context) -> list:
        """
        Retrieve data from the database using a dynamically generated SQL query.
        Args:
            model (str): The name of the model to query.
            model_path (str): The path to the model.
            fields (list): A list of fields to retrieve.
            start_date (str): The start date for the query in 'YYYY-MM-DD' format.
            end_date (str): The end date for the query in 'YYYY-MM-DD' format.
            context (dict): Additional context for the query.
        Returns:
            list: A list of records retrieved from the database.
        """

        return DynamicQueryPostgresService(self.context.pg_manager).get_data_sql(
            model, fields, start_date, end_date, context
        )


class DynamicQueryPostgresService:
    def __init__(self, pg_manager):
        self.pg_manager = pg_manager

    def parse_nested_fields(self, model, fields) -> dict:
        """
        Parses a list of nested fields and validates them against the given SQLAlchemy model.
        Args:
            model (Base): The SQLAlchemy model to validate against.
            fields (list of str): A list of field names, which can include nested fields separated by dots.
        Returns:
            dict: A dictionary representing the nested structure of the fields.
        Raises:
            ValueError: If a field is invalid, such as using a column name ending with '_id' directly,
                        or if a subfield is not a valid relationship or column of the model.
        Examples:
            parse_nested_fields(Sale Order, ["id", "name", "flow.id", "flow.name"])
            # Returns:
            {
                "id": True,
                "name": True,
                "flow": {
                    "id": True,
                    "name": True
                }
            }

        """

        # Get the column names and relationships of the model
        root = {}

        for field in fields:
            parts = field.split(".")
            current_model = model
            current_dict = root

            for i, part in enumerate(parts):
                is_last = i == len(parts) - 1

                inspector = inspect(current_model)
                model_columns = set(col.name for col in inspector.columns)

                rels_by_key = {r.key: r for r in inspector.relationships}

                if i == 0 and part.endswith("_id") and part in model_columns:
                    raise ValueError(
                        f"Not allowed to include the column '{part}' directly. Include the relationship instead."
                    )

                if not is_last:
                    # Subfields are only allowed for relationships, not for columns.
                    # If you want to include a column, just include the column name directly.
                    if part not in rels_by_key:
                        # If it's not a relationship, we raise an error
                        raise ValueError(
                            f"The field '{part}' is not a valid column or relationship of the model {current_model.__name__}."
                        )
                    rel = rels_by_key[part]
                    current_dict = current_dict.setdefault(part, {})
                    current_model = rel.mapper.class_
                else:
                    # If it's a relationship, we must add the subfields
                    if part not in model_columns:
                        if part in rels_by_key:
                            raise ValueError(
                                f"The field '{part}' is a relationship and must include subfields. Example: '{part}.id'."
                            )
                        else:
                            raise ValueError(
                                f"The field '{part}' is not a valid column or relationship of the model {current_model.__name__}."
                            )
                    current_dict[part] = True

        return root

    def _get_relationship_info(self, model, relationship_name) -> tuple:
        """
        Retrieve information about a specific relationship of a SQLAlchemy model.
        Args:
            model (Base): The SQLAlchemy model class to inspect.
            relationship_name (str): The name of the relationship to retrieve information for.
        Returns:
            tuple: A tuple containing:
                - target_table (str or None): The name of the target table of the relationship, or None if the relationship does not exist.
                - target_model (class or None): The target model class of the relationship, or None if the relationship does not exist.
                - uselist (bool or None): A boolean indicating if the relationship is a one-to-many or many-to-many relationship (True) or a one-to-one relationship (False), or None if the relationship does not exist.
        """

        inspector = inspect(model)
        rel = inspector.relationships.get(relationship_name)
        if not rel:
            return None, None, None, False, None

        target_table = rel.mapper.persist_selectable.name
        target_model = rel.mapper.class_
        uselist = rel.uselist

        # Chequeamos si es muchos-a-muchos
        is_m2m = bool(rel.secondary is not None)  # True si rel.secondary existe
        pivot_table = rel.secondary.name if is_m2m else None

        return target_table, target_model, uselist, is_m2m, pivot_table

    def build_select_and_joins(self, model, nested_fields, alias_prefix="t") -> tuple:
        """
        Constructs SQL SELECT and JOIN clauses for a given SQLAlchemy model and its nested fields.
        Args:
            model (Base): The SQLAlchemy model class to build the SELECT and JOIN clauses for.
            nested_fields (dict): A dictionary specifying which fields to include in the SELECT clause.
                The keys are column or relationship names, and the values are either True (for direct columns)
                or nested dictionaries (for relationships).
            alias_prefix (str, optional): The prefix to use for table aliases in the SQL query. Defaults to "t".
        Returns:
            tuple: A tuple containing three elements:
                - columns_select (list): A list of SQL SELECT clause strings.
                - join_clauses (list): A list of SQL JOIN clause strings.
                - nested_mapping (dict): A dictionary mapping the original field names to their aliased names
                  or nested mappings for relationships.
        """

        main_alias = alias_prefix
        inspector = inspect(model)
        columns_select = []
        join_clauses = []
        nested_mapping = defaultdict(dict)

        # Process "direct" columns (those that are not dict but True)
        # For example: {"id": True, "name": True}
        for column_obj in inspector.columns:
            col_name = column_obj.name
            if col_name in nested_fields and nested_fields[col_name] is True:
                # SELECT t."id" AS t_id
                as_name = f"{main_alias}_{col_name}"
                columns_select.append(f'{main_alias}."{col_name}" AS {as_name}')
                nested_mapping[col_name] = as_name

        # Process relationships (subdicts)
        # For example: {"state": {"id": True, "name": True}}
        for key, subdict in nested_fields.items():
            if isinstance(subdict, dict):
                # 'key' in this case should be the name of the relationship
                target_table, related_model, is_uselist, is_m2m, pivot_table_name = self._get_relationship_info(
                    model, key
                )
                if not target_table:
                    continue

                related_alias = f"{alias_prefix}_{key}"

                rel = inspect(model).relationships.get(key)

                if is_m2m and pivot_table_name:
                    # Many-to-many relationship
                    pivot_alias = f"{alias_prefix}_{key}_assoc"  # p.e. main_orders_delivery_method_states_assoc
                    child_final_alias = f"{alias_prefix}_{key}_table"  # p.e. main_orders_delivery_method_states_table

                    join_clauses.append(
                        f'LEFT JOIN "{pivot_table_name}" AS {pivot_alias}'
                        f' ON {alias_prefix}."id" = {pivot_alias}."{list(rel.local_columns)[0]._key_label}"'
                    )
                    join_clauses.append(
                        f'LEFT JOIN "{target_table}" AS {child_final_alias}'
                        f' ON {pivot_alias}."{list(rel.remote_side)[0].name}" = {child_final_alias}."id"'
                    )

                    final_alias = f"{related_alias}_table"

                    sub_cols, sub_joins, sub_map = self.build_select_and_joins(
                        related_model, subdict, alias_prefix=final_alias
                    )
                    columns_select.extend(sub_cols)
                    join_clauses.extend(sub_joins)

                    nested_mapping[key] = {"_uselist": is_uselist, "_mapping": sub_map}

                else:
                    pairs = list(rel.local_remote_pairs)
                    if not pairs:
                        continue
                    local_col_obj, remote_col_obj = pairs[0]
                    local_col_name = local_col_obj.name
                    remote_col_name = remote_col_obj.name

                    on_clause = f'{main_alias}."{local_col_name}" = {related_alias}."{remote_col_name}"'
                    join_clauses.append(f'LEFT JOIN "{target_table}" AS {related_alias} ON {on_clause}')

                    sub_cols, sub_joins, sub_map = self.build_select_and_joins(
                        related_model, subdict, alias_prefix=related_alias
                    )
                    columns_select.extend(sub_cols)
                    join_clauses.extend(sub_joins)

                    nested_mapping[key] = {"_uselist": is_uselist, "_mapping": sub_map}

        return columns_select, join_clauses, dict(nested_mapping)

    def get_data_sql(self, model, fields, start_date, end_date, context) -> list:
        """
        Retrieves data from the database based on the provided model, fields, and date range.
        Args:
            model (Base): The SQLAlchemy model class to query.
            fields (list): List of fields to retrieve, including nested fields.
            start_date (datetime): The start date for the date range filter.
            end_date (datetime): The end date for the date range filter.
            context (dict): Additional context for the query, including tenant information.
        Returns:
            list: A list of dictionaries representing the retrieved data, grouped by the primary key of the main table.
        """
        # Parse nested fields
        nested_fields = self.parse_nested_fields(model, fields)

        # Build SELECT and JOIN clauses
        main_table = model.__tablename__
        columns_select, join_clauses, nested_mapping = self.build_select_and_joins(
            model, nested_fields, alias_prefix="main"
        )

        select_clause = ",\n    ".join(columns_select)
        if not select_clause:
            select_clause = "1"  # Prevent empty SELECT clause

        sql_query = f"""
        SELECT
            {select_clause}
        FROM "{main_table}" AS main
            {' '.join(join_clauses)}
        WHERE main."tenant" = :tenant
          AND main."created_at" BETWEEN :start_date AND :end_date
        """
        # Execute the query
        result = self.pg_manager.Session.execute(
            text(sql_query),
            {
                "tenant": context["tenant"],
                "start_date": start_date,
                "end_date": end_date,
            },
        )
        rows = result.fetchall()
        main_pk_col = list(inspect(model).primary_key)[0].name
        main_pk_alias = f"main_{main_pk_col}"

        grouped_data = {}
        for row in rows:
            row_dict = dict(row._mapping)
            main_id_value = row_dict.get(main_pk_alias)

            if main_id_value not in grouped_data:
                grouped_data[main_id_value] = self._build_base_dict(row_dict, nested_mapping)

            for rel_name, info in nested_mapping.items():
                if isinstance(info, dict):
                    sub_map = info.get("_mapping", {})
                    sub_dict = self._build_nested_dict(row_dict, sub_map)

                    if info.get("_uselist"):
                        existing_list = grouped_data[main_id_value][rel_name]
                        found = False
                        for idx, existing_item in enumerate(existing_list):
                            if self._compare_items(existing_item, sub_dict, sub_map):
                                merged_item = self._merge_nested_dicts(existing_item, sub_dict, sub_map)
                                existing_list[idx] = merged_item
                                found = True
                                break
                        if not found:
                            existing_list.append(sub_dict)
                    else:
                        existing_item = grouped_data[main_id_value].get(rel_name, {})
                        if existing_item:
                            merged_item = self._merge_nested_dicts(existing_item, sub_dict, sub_map)
                            grouped_data[main_id_value][rel_name] = merged_item
                        else:
                            grouped_data[main_id_value][rel_name] = sub_dict

        return list(grouped_data.values())

    def _merge_nested_dicts(self, existing, new, mapping):
        for key, key_info in mapping.items():
            if isinstance(key_info, dict):
                sub_mapping = key_info.get("_mapping", {})
                if key_info.get("_uselist", False):
                    existing_list = existing.get(key, [])
                    new_list = new.get(key, [])
                    for new_item in new_list:
                        found = False
                        for existing_item in existing_list:
                            if self._compare_items(existing_item, new_item, sub_mapping):
                                self._merge_nested_dicts(existing_item, new_item, sub_mapping)
                                found = True
                                break
                        if not found:
                            existing_list.append(new_item)
                    existing[key] = existing_list
                else:
                    existing_sub = existing.get(key, {})
                    new_sub = new.get(key, {})
                    merged_sub = self._merge_nested_dicts(existing_sub, new_sub, sub_mapping)
                    existing[key] = merged_sub
            else:
                if key in new and new[key] is not None:
                    existing[key] = new[key]
        return existing

    def _compare_items(self, item1, item2, mapping):
        """
        Compares two items based on the mapping, ignoring list-type keys.
        """
        for key, key_info in mapping.items():
            # Skip keys that are lists (uselist=True)
            if isinstance(key_info, dict) and key_info.get("_uselist", False):
                continue

            # Handle nested mappings (non-list)
            if isinstance(key_info, dict) and "_mapping" in key_info:
                nested_mapping = key_info["_mapping"]
                nested_item1 = item1.get(key, {})
                nested_item2 = item2.get(key, {})
                if not self._compare_items(nested_item1, nested_item2, nested_mapping):
                    return False
            elif isinstance(key_info, dict):
                # Handle other dict structures if needed
                pass
            else:
                # Simple key comparison
                if item1.get(key) != item2.get(key):
                    return False
        return True

    def _build_nested_dict(self, flat_row, nested_mapping) -> dict:
        """
        Recursively builds a nested dictionary from a flat dictionary based on a nested mapping.
        Args:
            flat_row (dict): The flat dictionary containing the data.
            nested_mapping (Union[str, dict]): The mapping that defines how to nest the flat dictionary.
                If a string is provided, it is used as a key to retrieve the value from the flat dictionary.
                If a dictionary is provided, it can contain a special key "_uselist" to indicate if the
                nested structure should be a list or a single dictionary.
        Returns:
            Union[dict, Any]: The nested dictionary structure or the value from the flat dictionary.
        """

        if isinstance(nested_mapping, str):
            return flat_row.get(nested_mapping)

        if isinstance(nested_mapping, dict):
            if "_uselist" in nested_mapping:
                is_uselist = nested_mapping["_uselist"]
                sub_mapping = nested_mapping["_mapping"]

                if is_uselist:
                    sub_element = self._build_nested_dict(flat_row, sub_mapping)
                    return [sub_element] if sub_element else []
                else:
                    return self._build_nested_dict(flat_row, sub_mapping)

            result = {}
            for sub_key, sub_val in nested_mapping.items():
                # Recursively build the nested dictionary for each sub-key
                result[sub_key] = self._build_nested_dict(flat_row, sub_val)
            return result

        return None

    def _build_base_dict(self, row_dict, nested_mapping) -> dict:
        """
        Constructs a base dictionary from a given row dictionary and a nested mapping.
        Args:
            row_dict (dict): The dictionary containing row data.
            nested_mapping (dict): The mapping that defines how to transform the row data into the result dictionary.
                - If the value is a string, it is treated as a direct column alias.
                - If the value is a dictionary, it may represent a nested structure:
                    - If the dictionary contains a key "_uselist", it is treated as a collection and initialized with an empty list.
                    - Otherwise, it is treated as a one-to-one relationship and a sub-dictionary is constructed using the "_mapping" key.
        Returns:
            dict: The constructed base dictionary with the transformed data.
        """

        result = {}
        for key, value in nested_mapping.items():
            if isinstance(value, str):
                result[key] = row_dict.get(value)

            elif isinstance(value, dict):
                # Check if it's a collection or a one-to-one relationship
                if value.get("_uselist"):
                    # Collection => initialize with an empty list
                    result[key] = []
                    sub_map = value.get("_mapping", {})
                    sub_element = self._build_nested_dict(row_dict, sub_map)
                    if sub_element:  # Solo agregar si hay datos
                        result[key].append(sub_element)
                else:
                    # # Relation one-to-one
                    sub_map = value.get("_mapping", {})
                    sub_dict = self._build_nested_dict(row_dict, sub_map)
                    result[key] = sub_dict
        return result


class BatchUpsert(ImportExportBase):
    def __init__(self, context: dict):
        """
        Initializes the BatchUpsert instance.
        Parameters:
        context (dict): The context containing database connection information and other relevant settings.
        """
        self.context = context
        self.db_types = {
            "SQL": self.upsert_data_sql,
            "NO_SQL": self.upsert_data_no_sql,
        }
        self.db_type = "NO_SQL" if not hasattr(self.context, "pg_manager") else "SQL"

    def upsert_data(self, data):
        """
        Performs a batch upsert operation using the appropriate database method based on the context.
        Parameters:
        data (dict): The data to be upserted.
        Returns: The result of the upsert operation.
        """
        model = self.get_model(data["model_path"])
        return self.db_types[self.db_type](model, data)

    def upsert_data_no_sql(self, model, data):
        """
        Handles the batch upsert operation in a NoSQL database.
        Parameters:
        model: The model class for the NoSQL operation.
        data (dict): The data to be upserted.
        Returns: The result of the NoSQL upsert operation.
        """
        return self.context.db_manager.batch_upsert(model, data)

    def upsert_data_sql(self, model, data):
        """
        Handles the batch upsert operation in a SQL database.
        Parameters:
        model: The model class for the SQL operation.
        data (dict): The data to be upserted.
        Returns: The result of the SQL upsert operation.
        """
        return self.context.pg_manager.batch_upsert(model, self.context.pg_manager.Session, data)
