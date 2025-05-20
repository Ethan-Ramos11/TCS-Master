from dotenv import load_dotenv
import os
import requests
from typing import Dict, Optional, Union

load_dotenv()


def get_api_key() -> str:
    """
    Retrieves the API key from environment variables.

    Returns:
        str: The API key for the weather service

    Raises:
        EnvironmentError: If the API key is not found in environment variables
    """
    pass


def get_weather_data(city: str, api_key: str) -> Dict:
    """
    Fetches weather data for a specified city using the weather API.

    Args:
        city (str): The name of the city to get weather data for
        api_key (str): The API key for authentication

    Returns:
        Dict: A dictionary containing the weather data

    Raises:
        requests.RequestException: If there's an error making the API request
        ValueError: If the city name is invalid or empty
    """
    pass


def parse_weather_data(weather_data: Dict) -> Dict:
    """
    Parses the raw weather data into a more usable format.

    Args:
        weather_data (Dict): The raw weather data from the API

    Returns:
        Dict: A dictionary containing parsed weather information including:
            - temperature
            - humidity
            - wind speed
            - weather description
            - timestamp
    """
    pass


def display_weather(parsed_data: Dict) -> None:
    """
    Displays the weather information in a user-friendly format.

    Args:
        parsed_data (Dict): The parsed weather data to display

    Returns:
        None
    """
    pass


def get_forecast(city: str, api_key: str, days: int = 5) -> Dict:
    """
    Fetches weather forecast data for a specified city.

    Args:
        city (str): The name of the city to get forecast for
        api_key (str): The API key for authentication
        days (int, optional): Number of days to forecast. Defaults to 5.

    Returns:
        Dict: A dictionary containing the forecast data

    Raises:
        requests.RequestException: If there's an error making the API request
        ValueError: If the city name is invalid or days parameter is out of range
    """
    pass


def main() -> None:
    """
    Main function to run the weather application.
    Handles user input and coordinates the flow of the program.
    """
    pass


if __name__ == "__main__":
    main()
