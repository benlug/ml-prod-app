"""
Module for data collection from the database.
This module contains functions to load data from the database for further processing.
"""

import pandas as pd

from loguru import logger

from config import engine
from db.db_model import RentApartments
from sqlalchemy import select


def load_data(path):
    """
    Load data from a CSV file.

    Parameters:
    path (str): The file path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    logger.info(f"Reading in data from {path}")
    return pd.read_csv(path)


def load_data_from_db():
    """
    Load data from the database.
    This function reads data from the database using a predefined query and returns it as a pandas DataFrame.
    Returns:
        pd.DataFrame: DataFrame containing the data read from the database.
    """
    logger.info("Reading in data from db")

    query = select(RentApartments)

    return pd.read_sql(query, engine)
