"""
Driver for connecting to Oracle via oracledb.
"""

try:
    import oracledb
    from oracledb import Connection as OracleConnection
except ImportError:
    raise ImportError(
        "The driver 'oracledb' is not installed. Install it with: pip install dbyoke[oracle]"
    )

from .base import BaseDriver


class OracleDriver(BaseDriver):
    """
    Driver for working with Oracle databases via oracledb.
    """

    def connect(self) -> OracleConnection:
        """
        Establishes a connection to an Oracle database.

        :return: oracledb connection object.
        """
        try:
            connection = oracledb.connect(self.connection_string)
            return connection
        except oracledb.Error as e:
            raise ConnectionError(f"Error connecting to Oracle: {e}")

    def close(self, connection: OracleConnection):
        """
        Закрывает соединение с базой данных Oracle.

        :param connection: Объект соединения oracledb.
        """
        try:
            connection.close()
        except oracledb.Error as e:
            raise ConnectionError(f"Error closing connection: {e}")
