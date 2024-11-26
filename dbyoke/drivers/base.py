"""
Base class for database connection drivers.
"""

from abc import ABC, abstractmethod


class BaseDriver(ABC):
    """
    Abstract base class for database drivers.

    Each driver must implement connect and close methods.
    """

    def __init__(self, connection_string: str):
        """
        Initializing the driver.

        :param connection_string: Database connection string.
        """
        self.connection_string = connection_string

    @abstractmethod
    def connect(self):
        """
        Establishes a connection to the database.

        :return: The connection object.
        """
        pass

    @abstractmethod
    def close(self, connection):
        """
        Closes the connection to the database.

        :param connection: The connection object to close.
        """
        pass
