from enum import Enum, unique
from abc import ABC, abstractmethod


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


class CSVDocumentStrategy(DocumentStrategy):
    """
    Strategy for handling CSV documents.
    """

    def __init__(self, file_library, **kwargs):
        """
        Initializes the CSVDocumentStrategy.
        :param file_library: Library to be used for reading files.
        """
        self.file_library = file_library

    def open_file(self, file_path):
        """
        Opens and reads a CSV file using the specified file library.
        :param file_path: Path of the CSV file to be opened.
        :return: DataFrame object of the opened file.
        """
        return self.file_library.read_csv(file_path)

    def get_data(self, file_path):
        """
        Opens and reads a CSV file using the specified file library.
        :param file_path: Path of the CSV file to be opened.
        :return: List of dictionaries of the opened file.
        """
        import numpy as np

        csv_file = self.open_file(file_path)
        csv_file.replace({np.nan: None}, inplace=True)
        return csv_file.to_dict(orient="records")

    def add_data(self, file_path, data):
        """
        Adds data to the CSV file.
        :param file_path: Path of the CSV file to be opened.
        :param data: Data to be added to the CSV file.
        """

        csv_data = self.file_library.DataFrame(data)
        csv_data.to_csv(file_path, index=False)

    def validate(self, expected, file_path):
        """
        Validates the headers of the CSV file.
        :param expected: List of expected headers.
        :param file_path: Path of the CSV file to be validated.
        """
        csv_file = self.open_file(file_path)
        actual_headers = csv_file.columns.tolist()
        if set(expected) != set(actual_headers):
            raise ValueError("Csv headers do not match the expected model headers")


class JSONDocumentStrategy(DocumentStrategy):
    """
    Strategy for handling JSON files.
    """

    def __init__(self, file_library, **kwargs):
        """
        Initializes the JSONDocumentStrategy.
        :param file_library: Library to be used for reading files.
        """
        self.file_library = file_library

    def open_file(self, file_path):
        """
        Opens and reads a JSON file using the specified file library.
        :param file_path: Path of the JSON file to be opened.
        :return: DataFrame object of the opened file.
        """
        return self.file_library.read_json(file_path)

    def get_data(self, file_path):
        """
        Opens and reads a JSON file using the specified file library.
        :param file_path: Path of the JSON file to be opened.
        :return: List of dictionaries of the opened file.
        """
        import numpy as np

        json_file = self.open_file(file_path)
        json_file.replace({np.nan: None}, inplace=True)
        return json_file.to_dict(orient="records")

    def add_data(self, file_path, data):
        """
        Adds data to the JSON file.
        :param file_path: Path of the JSON file to be opened.
        :param data: Data to be added to the JSON file.
        """
        json_data = self.file_library.DataFrame(data)
        json_data.to_json(file_path, orient="records", lines=True)

    def validate(self, expected, file_path):
        """
        Validates the headers of the JSON file.
        :param expected: List of expected headers.
        :param file_path: Path of the JSON file to be validated.
        """
        json_file = self.open_file(file_path)
        actual_headers = json_file.columns.tolist()
        if set(expected) != set(actual_headers):
            raise ValueError("JSON headers do not match the expected model headers")


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
            FilesType.CSV: CSVDocumentStrategy,
            FilesType.XLSX: ExcelDocumentStrategy,
            FilesType.JSON: JSONDocumentStrategy,
        }
        self.allowed_extensions = allowed_extensions

    def allowed_extension(self, extension):
        """
        Checks if the given extension is allowed.
        :param extension: Extension to check.
        :return: Boolean indicating if the extension is allowed.
        """
        return extension in self.allowed_extensions

    def get_document_processor(self, file_type: FilesType, file_library: object):
        """
        Retrieves the appropriate file processor based on the file type.
        :param file_type: Type of the document file.
        :param file_library: Library to be used for reading files.
        :return: An instance of the corresponding document strategy.
        """
        if not self.allowed_extension(file_type.value):
            raise ValueError("Document type not allowed")

        strategy_class = self.document_strategies.get(file_type)
        if strategy_class is None:
            raise ValueError("Document type not supported")

        return strategy_class(file_library)
