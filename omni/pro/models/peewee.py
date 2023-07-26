from peewee import _StringField


class SelectionField(_StringField):
    """
        Custom Peewee field to handle selection options.

        Options are provided as a list of tuples during field initialization.
        Each tuple consists of a unique key and its corresponding label.

        Example:
        SelectionField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')])

        The allowed values for this field are the keys from the provided tuples.
        If an unauthorized value is attempted to be assigned to the field, a ValueError exception is raised.

        field_type : str
            Defines the field type in the database. In this case, it is 'VARCHAR'.

        Attributes
        ----------
        choices : list
            List of tuples provided during initialization. Each tuple consists of a key and a label.
        choice_keys : list
            List of the keys from each tuple in 'choices'. These are the only keys allowed for this field.

        Methods
        -------
        __init__(self, choices, *args, **kwargs)
            Initializes the field with the given choices.

        python_value(self, value)
            Converts the field's value to a Python value and checks if it is valid.
    """
    field_type = 'VARCHAR'

    def __init__(self, choices, *args, **kwargs):
        """
            Initializes the field with the given choices.

            Parameters
            ----------
            choices : list
               List of tuples, where each tuple consists of a key and a label.
       """
        self.choices = choices
        self.choice_keys = [choice[0] for choice in choices]
        super(SelectionField, self).__init__(*args, **kwargs)

    def python_value(self, value):
        """
            Converts the field's value to a Python value and checks if it is valid.

            Parameters
            ----------
            value : str
                The field's value to validate.

            Returns
            -------
            str
                The field's value if it is valid.

            Raises
            ------
            ValueError
                If the value is not among the allowed keys, a ValueError is raised.
        """
        if value not in self.choice_keys:
            raise ValueError(f"Invalid value {value}, options are{self.choice_keys}")
        return super(SelectionField, self).python_value(value)
