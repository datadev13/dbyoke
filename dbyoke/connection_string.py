"""
Generating database connection strings.
"""


class ConnectionStringBuilder:
    """
    Class for creating database connection strings.
    """

    def __init__(self, config: dict):
        """
        Initialize the connection string builder.

        :param config: Dictionary with connection parameters (e.g. db_type, user, password, etc.).
        """
        self.config = config
        self.db_type = config.get("db_type")
        if not self.db_type:
            raise ValueError("Database type (db_type) is required.")

    def build(self) -> str:
        """
        Creates a connection string depending on the database type.

        :return: Connection string.
        """
        builders = {
            "postgresql": self._build_postgresql,
            "mssql": self._build_mssql,
            "oracle": self._build_oracle,
        }

        builder = builders.get(self.db_type)
        if not builder:
            raise ValueError(f"No support for database '{self.db_type}'.")

        return builder()

    def _build_postgresql(self) -> str:
        """
        Creates a connection string for PostgreSQL.

        :return: Connection string.
        """
        return (
            f"dbname='{self.config.get('dbname')}' "
            f"user='{self.config.get('user')}' "
            f"password='{self.config.get('password')}' "
            f"host='{self.config.get('host', 'localhost')}' "
            f"port={self.config.get('port', 5432)}"
        )

    def _build_sqlite(self) -> str:
        """
        Creates a connection string for SQLite.

        :return: Connection string.
        """
        database = self.config.get("database")
        if not database:
            raise ValueError("Connecting to SQLite requires the 'database' parameter.")
        return database

    def _build_mssql(self) -> str:
        """
         Creates a connection string for Microsoft SKL Server via ODBC.

         :return:Connection string.
         """
        return (
            f"DRIVER={self.config.get('driver', '{ODBC Driver 18 for SQL Server}')};"
            f"SERVER={self.config.get('host', 'localhost')},{self.config.get('port', 1433)};"
            f"DATABASE={self.config.get('dbname')};"
            f"UID={self.config.get('user')};"
            f"PWD={self.config.get('password')};"
            f"TrustServerCertificate={self.config.get('trust_certificate', 'yes')}"";"
        )

    def _build_oracle(self) -> str:
        """
        Creates a connection string for Oracle.

        :return: Connection string.
        """
        return (
            f"{self.config.get('user')}/{self.config.get('password')}@"
            f"{self.config.get('host', 'localhost')}:{self.config.get('port', 1521)}/"
            f"{self.config.get('service_name', 'XE')}"
        )
