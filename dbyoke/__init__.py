"""
dbyoke: A universal library for connecting to various databases.

This package provides a single interface for working with various databases,

allowing you to easily switch between drivers and databases.
"""

from .connection import DatabaseConnection
from .connection_string import ConnectionStringBuilder

__all__ = [
    "DatabaseConnection",
    "ConnectionStringBuilder",
]


__version__ = "0.1.3"
