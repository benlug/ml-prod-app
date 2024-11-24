"""
This module contains functions for preparing and parsing data columns in the model pipeline.
"""

import pandas as pd
import re
from model.pipeline.collection import load_data_from_db

from loguru import logger


def prepare_data() -> pd.DataFrame:
    """
    Prepares the data by performing a series of preprocessing steps.
    Steps:
    1. Loads data from the database.
    2. Encodes categorical columns.
    3. Parses the garden column.
    Returns:
        pd.DataFrame: The preprocessed data as a DataFrame.
    """
    logger.info("starting up preprocessing pipeline")

    data = load_data_from_db()

    data_encoded = _encode_cat_cols(data)

    df = parse_garden_col(data_encoded)

    return df


def _encode_cat_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes specified categorical columns in the given DataFrame using one-hot encoding.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing the data to be encoded.

    Returns:
    pd.DataFrame: A DataFrame with the specified categorical columns encoded as one-hot vectors.

    Notes:
    The columns to be encoded are: "balcony", "storage", "parking", "furnished", "garage".
    The first category in each column will be dropped to avoid multicollinearity.
    """
    cols = ["balcony", "storage", "parking", "furnished", "garage"]
    logger.info(f"encoding categorical columns: {cols}")
    return pd.get_dummies(dataframe, columns=cols, drop_first=True)


def parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Parses the 'garden' column in the given DataFrame.

    This function converts the 'garden' column values from strings to integers.
    If the value is 'Not present', it is converted to 0. Otherwise, it extracts
    the first integer found in the string and uses it as the value.

    Args:
        data (pd.DataFrame): The input DataFrame containing a 'garden' column.

    Returns:
        pd.DataFrame: The DataFrame with the parsed 'garden' column.
    """
    logger.info("parsing garden column")
    dataframe["garden"] = dataframe["garden"].apply(
        lambda x: 0 if x == "Not present" else int(re.findall(r"\d+", x)[0])
    )
    return dataframe
