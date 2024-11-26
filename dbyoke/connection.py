"""
Module for managing connections to databases.
"""

import importlib
from .connection_string import ConnectionStringBuilder


class DatabaseConnection:
    """
    Class for managing connections to databases.

    Supports a universal interface for working with various drivers.
    """

    _DRIVER_MAPPING = {
        "postgresql": "dbyoke.drivers.postgres_driver.PostgresDriver",
        "mssql": "dbyoke.drivers.mssql_driver.MssqlDriver",
        "oracle": "dbyoke.drivers.oracle_driver.OracleDriver",
    }

    def __init__(self, config: dict):
        """
        Initializing the connection.

        :param config: Dictionary with connection parameters (e.g. db_type, user, password, etc.).
        """
        self.config = config
        self.db_type = config.get("db_type")
        if self.db_type not in self._DRIVER_MAPPING:
            raise ValueError(f"Driver for database type '{self.db_type}' is not supported.")

        driver_path = self._DRIVER_MAPPING[self.db_type]
        try:
            module_name, class_name = driver_path.rsplit(".", 1)
            module = importlib.import_module(module_name)
            self.driver_class = getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ValueError(
                f"Unable to load driver for {self.db_type}. Please install the necessary driver. Details: {e}.")

        self.driver_instance = None
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the database.

        :return: The connection object provided by the driver.
        """
        if self.connection:
            return self.connection

        connection_string = ConnectionStringBuilder(self.config).build()

        self.driver_instance = self.driver_class(connection_string)
        self.connection = self.driver_instance.connect()
        return self.connection

    def close(self):
        """
        Closes the connection to the database.
        """
        if self.connection:
            self.driver_instance.close(self.connection)
            self.connection = None
            self.driver_instance = None

    def __enter__(self):
        """
        Context manager for working with the database.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closing connection when exiting context manager.
        """
        self.close()
