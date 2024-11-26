# DbYoke

DbYoke is a library designed to standardize database connections. It supports multiple drivers (PostgreSQL,
MSSQL, Oracle) and simplifies connection string generation and connection management.

## Features

- Simplified database connection management.
- Support for PostgreSQL, Microsoft SQL Server, and Oracle.
- Unified interface for working with database drivers.
- Connection string generation.

---

## Installation

You can install **DbYoke** using `pip install dbyoke`.

### Install from PyPI

To install the library with all available drivers:

```bash
pip install dbyoke[all]
```
To install only specific drivers, use the following commands:

•	For PostgreSQL:
```bash
pip install dbyoke[postgresql]
```
•	For Oracle:
```bash
pip install dbyoke[oracle]
```
•	For MSSQL:
```bash
pip install dbyoke[mssql]
```

Optional Dependencies

DbYoke provides optional dependencies for different database drivers. You can install the specific drivers you need by using the extras feature of pip. For example, to install support for PostgreSQL, you can use:
```bash
pip install dbyoke[postgresql]
```

## Quick Start

Connecting to a Database

Example for PostgreSQL

```py
from dbyoke.connection import DatabaseConnection

config = {
    "db_type": "postgresql",
    "dbname": "example_db",
    "user": "admin",
    "password": "secret",
    "host": "localhost",
    "port": 5432
}

with DatabaseConnection(config) as db:
    connection = db.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_table")
    print(cursor.fetchall())
```

Example for MSSQL

```py
from dbyoke.connection import DatabaseConnection

config = {
    "db_type": "mssql",
    "dbname": "example_db",
    "user": "admin",
    "password": "secret",
    "host": "localhost",
    "driver": "{ODBC Driver 18 for SQL Server}",
    "trust_certificate": "yes"
}

with DatabaseConnection(config) as db:
    connection = db.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    print(cursor.fetchall())
```

Generating a Connection String

```py
from dbyoke.connection_string import ConnectionStringBuilder

config = {
    "db_type": "oracle",
    "user": "system",
    "password": "oracle",
    "host": "localhost",
    "port": 1521,
    "service_name": "XE"
}

builder = ConnectionStringBuilder(config)
print(builder.build())
# Output: "system/oracle@localhost:1521/XE"
```

## Logging

To enable logging, you can use the following utility function:

```py
from dbyoke.utils import configure_logging

logger = configure_logging(level="DEBUG")
```

## Supported Databases

| Database Type | Driver         | Dependency        |
|---------------|----------------|-------------------|
| PostgreSQL    | Psycopg2Driver | `psycopg2-binary` |
| MSSQL         | PyODBCDriver   | `pyodbc`          |
| Oracle        | OracleDriver   | `oracledb`        |