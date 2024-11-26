"""
dbyoke: A universal library for connecting to various databases.

This package provides a single interface for working with various databases,

allowing you to easily switch between drivers and databases.
"""

from .connection import DatabaseConnection
from .connection_string import ConnectionStringBuilder
from _temp.config import load_config_from_file

__all__ = [
    "DatabaseConnection",
    "ConnectionStringBuilder",
    "load_config_from_file",
]


__version__ = "0.1.0"
