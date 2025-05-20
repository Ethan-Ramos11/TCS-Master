from dotenv import load_dotenv
import os
import requests
from typing import Dict, Optional, Union


def get_api_key() -> tuple[str, str]:
    """
    Retrieves the API key and URL from environment variables.

    Returns:
        tuple[str, str]: A tuple containing (api_key, url)

    Raises:
        EnvironmentError: If the API key or URL is not found in environment variables
    """
    try:
        load_dotenv()
        api_key = os.getenv("WEATHER_API_KEY")
        url = os.getenv("WEATHER_URL")

        if not api_key or not url:
            raise EnvironmentError("Missing required environment variables")

        return url, api_key
    except Exception as e:
        raise EnvironmentError(f"Error retrieving environment variables: {e}")


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
    if not city:
        raise ValueError("Expected a city")
    try:
        url, api_key = get_api_key()
        url += f"access_key={api_key}"
        query_string = {"query": city}
        response = requests.get(url, params=query_string)
        info = response.json()
        if not info.get("success", True):
            error = info.get("error")
            raise requests.RequestException(
                f"API Error: {error.get('type')} - {error.get('info')}"
            )
        return info
    except requests.RequestException as e:
        raise e
    except Exception as e:
        raise requests.RequestException(f"Unexpected error: {e}")


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

    current = weather_data.get("current", {})
    location = weather_data.get("location", {})

    info = {
        "timestamp": location.get("localtime", "N/A"),
        "temperature": current.get("temperature", "N/A"),
        "humidity": current.get("humidity", "N/A"),
        "wind_speed": current.get("wind_speed", "N/A"),
        "weather_descriptions": current.get("weather_descriptions", ["N/A"])
    }
    return info


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
