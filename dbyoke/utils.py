"""
Useful functions for working with database connections.
"""

import logging


def validate_config(config: dict, required_keys: list):
    """
    Checks if the configuration contains all required keys.

    :param config: Dictionary with connection parameters.
    :param required_keys: List of required keys.
    :raises ValueError: If required keys are missing.
    """
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        raise ValueError(f"Missing required parameters: {', '.join(missing_keys)}")


def configure_logging(level: str = "INFO"):
    """
    Configure logging.

    :param level: Logging level (e.g. DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    log_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=log_level,
    )

    return logging.getLogger("dbyoke")


def get_default_port(db_type: str) -> int:
    """
    Returns the default port for the specified database type.

    :param db_type: Database type (e.g. postgresql, mssql, oracle).
    :return: The default port for the database.
    """
    default_ports = {
        "postgresql": 5432,
        "mssql": 1433,
        "oracle": 1521,
    }
    return default_ports.get(db_type)
