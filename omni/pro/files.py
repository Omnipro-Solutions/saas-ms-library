from abc import ABC, abstractmethod
from enum import Enum, unique
from io import BytesIO

import pandas as pd


@unique
class FilesType(Enum):
    CSV = "csv"
    XLSX = "xlsx"
    JSON = "json"

    @classmethod
    def valid_value(cls, value: str) -> bool:
        return value in cls._value2member_map_


class DocumentStrategy(ABC):
    """
    Abstract base class defining the interface for document handling strategies.
    """

    @abstractmethod
    def open_file(self, file_path):
        """
        Opens and reads a file from the given file path.
        :param file_path: Path of the file to be opened.
        """
        pass

    @abstractmethod
    def get_data(self, file_path):
        """
        Gets the data from the file.
        :param file_path: Path of the file to be opened.
        """
        pass

    @abstractmethod
    def add_data(self, file_path, data):
        """
        Adds data to the file.
        :param file_path: Path of the file to be opened.
        :param data: Data to be added to the file.
        """
        pass

    @abstractmethod
    def validate(self, expected, file_path):
        """
        Validates the file against the expected criteria.
        :param expected: Expected criteria to validate.
        :param file_path: Path of the file to be validated.
        """
        pass


class JSONDocumentStrategy:
    """
    Strategy for handling JSON files.
    """

    def load_data(self, data) -> BytesIO:
        """
        Adds data to the JSON file and returns the JSON content as bytes.
        :param data: Data to be added to the JSON file.
        :return: JSON content as bytes.
        """
        # Convert the data to a DataFrame
        json_data = pd.DataFrame(data)

        # Convert the DataFrame to JSON string
        json_str = json_data.to_json(orient="records", lines=True)

        # Convert the JSON string to bytes
        json_bytes = BytesIO(json_str.encode("utf-8"))

        return json_bytes


class ExcelDocumentStrategy(DocumentStrategy):
    """
    Strategy for handling Excel documents.
    """

    def __init__(self, file_library, **kwargs):
        """
        Initializes the ExcelDocumentStrategy.
        :param file_library: Library to be used for reading files.
        """
        self.file_library = file_library

    def open_file(self, file_path):
        """
        To be implemented for opening Excel files.
        """
        raise NotImplementedError

    def validate(self, expected, file_path):
        """
        To be implemented for validating Excel files.
        """
        raise NotImplementedError


class CSVDocumentStrategy:
    """
    Strategy for handling CSV documents.
    """

    def load_data(self, json_data) -> BytesIO:
        return self.vertical_scale_json(json_data)

    def explode_lists(self, df) -> pd.DataFrame:
        list_cols = [col for col in df.columns if isinstance(df[col].iloc[0], list)] if not df.empty else []
        if not list_cols:
            return df
        col = list_cols[0]
        df = df.explode(col).reset_index(drop=True)
        if df[col].apply(lambda x: isinstance(x, (dict, list))).any():
            expanded = pd.json_normalize(df[col], sep=".").add_prefix(f"{col}.")
            df = pd.concat([df.drop(col, axis=1), expanded], axis=1)
        return self.explode_lists(df)

    def vertical_scale_json(self, json_data) -> BytesIO:
        df = pd.json_normalize(json_data, sep=".")
        df = self.explode_lists(df)

        numeric_cols = []
        for col in df.columns:
            try:
                # Intentar convertir la columna a numérica
                pd.to_numeric(df[col], errors="raise")
                numeric_cols.append(col)
            except:
                pass

        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            # Eliminar decimales si son .0 (ej: 1628.0 → 1628)
            df[col] = df[col].apply(lambda x: int(x) if isinstance(x, float) and x.is_integer() else x)

        csv_bytes = BytesIO()
        df.to_csv(
            csv_bytes,
            index=False,
            encoding="utf-8",
            sep=";",
            decimal=",",
        )
        csv_bytes.seek(0)
        return csv_bytes


class FileProcessor:
    """
    Processor class for handling different types of  files.
    """

    def __init__(self, allowed_extensions: list = []):
        """
        Initializes the FileProcessor with allowed file extensions.
        :param allowed_extensions: List of allowed file extensions.
        """
        self.document_strategies = {
            FilesType.CSV.value: CSVDocumentStrategy,
            # FilesType.XLSX.value: ExcelDocumentStrategy, #TODO Implementar ExcelDocumentStrategy
            FilesType.JSON.value: JSONDocumentStrategy,
        }
        self.allowed_extensions = allowed_extensions

    def allowed_extension(self, extension):
        """
        Checks if the given extension is allowed.
        :param extension: Extension to check.
        :return: Boolean indicating if the extension is allowed.
        """
        return extension in self.allowed_extensions

    def get_document_processor(self, file_type: str):
        """
        Retrieves the appropriate file processor based on the file type.
        :param file_type: Type of the document file.
        :param file_library: Library to be used for reading files.
        :return: An instance of the corresponding document strategy.
        """
        if not self.allowed_extension(file_type):
            raise ValueError("Document type not allowed")

        strategy_class = self.document_strategies.get(file_type)
        if strategy_class is None:
            raise ValueError("Document type not supported")

        return strategy_class()
