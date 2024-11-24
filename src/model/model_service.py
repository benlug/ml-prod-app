"""
This module provides a service class for managing and using a machine learning model.
The ModelService class allows for loading a model, making predictions, and handling
model-related operations.

Classes:
    ModelService: A service class for managing and using a machine learning model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService:
    """
    A service class for managing and using a machine learning model.
    Attributes:
        model: The machine learning model instance.
    Methods:
        __init__():
            Initializes the ModelService instance with no model loaded.
        load_model():
            Loads the machine learning model from the specified path in the settings.
            If the model does not exist, it triggers the model building process.
        predict(input_parameters):
            Makes a prediction using the loaded model with the given input parameters.
            Args:
                input_parameters (list): The input parameters for making the prediction.
            Returns:
                The prediction result from the model.
    """

    def __init__(self):
        """
        Initializes the model service with a model attribute set to None.
        """
        self.model = None

    def load_model(self):
        """
        Loads the machine learning model from the specified path.
        This method checks for the existence of the model configuration file at the
        specified path. If the model file does not exist, it triggers the model
        building process. If the model file exists, it loads the model into memory.
        Raises:
            FileNotFoundError: If the model file does not exist and the model building
                       process fails to create the model file.
        """
        logger.info(
            f"checking existance of model config file at {model_settings.model_path}/{model_settings.model_name}"
        )
        model_path = Path(f"{model_settings.model_path}/{model_settings.model_name}")

        if not model_path.exists():
            logger.warning(
                f"model at {model_settings.model_path}/{model_settings.model_name} was not found -> building model {model_settings.model_name}"
            )
            build_model()

        logger.info(f"model {model_settings.model_name} exists. -> loading model")
        self.model = pk.load(
            open(f"{model_settings.model_path}/{model_settings.model_name}", "rb")
        )

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using the model.

        Args:
            input_parameters (list or array-like): The input parameters for the prediction.

        Returns:
            array-like: The prediction result from the model.
        """
        logger.info("making prediction!")
        return self.model.predict([input_parameters])
