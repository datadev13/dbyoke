"""
Driver for connecting to SQL Server via pyodbc.
"""

try:
    import pyodbc
    from pyodbc import Connection as MssqlConnection
except ImportError:
    raise ImportError(
        "The driver 'pyodbc' is not installed. Install it with: pip install dbyoke[mssql]"
    )

from .base import BaseDriver


class MssqlDriver(BaseDriver):
    """
    Driver for working with SQL Server via pyodbc.
    """

    def connect(self) -> MssqlConnection:
        """
        Establishes a connection via pyodbc.

        :return: The pyodbc connection object.
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            return connection
        except pyodbc.Error as e:
            raise ConnectionError(f"Error connecting to pyodbc: {e}")

    def close(self, connection: MssqlConnection):
        """
        Closes the connection via pyodbc.

        :param connection: The pyodbc connection object.
        """
        try:
            connection.close()
        except pyodbc.Error as e:
            raise ConnectionError(f"Error closing connection: {e}")
