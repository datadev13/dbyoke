"""
Driver for connecting to PostgreSQL via psycopg2.
"""

try:
    import psycopg2
    from psycopg2.extensions import connection as PostgresConnection
except ImportError:
    raise ImportError(
        "The driver 'psycopg2' is not installed. Install it with: pip install dbyoke[postgresql]"
    )

from .base import BaseDriver


class PostgresDriver(BaseDriver):
    """
    Driver for working with PostgreSQL via psycopg2.
    """

    def connect(self) -> PostgresConnection:
        """
        Establishes a connection to PostgreSQL.

        :return: psycopg2 connection object.
        """
        try:
            connection = psycopg2.connect(self.connection_string)
            return connection
        except psycopg2.Error as e:
            raise ConnectionError(f"Error connecting to PostgreSQL: {e}")

    def close(self, connection: PostgresConnection):
        """
        Closes the connection to PostgreSQL.

        :param connection: The psycopg2 connection object.
        """
        try:
            connection.close()
        except psycopg2.Error as e:
            raise ConnectionError(f"Error closing connection: {e}")
