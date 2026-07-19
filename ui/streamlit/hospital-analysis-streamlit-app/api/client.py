import os
from typing import Any

import requests

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
DEFAULT_TIMEOUT = int(os.getenv("API_TIMEOUT_SECONDS", "30"))


def get_data(endpoint: str) -> dict[str, Any]:
    """Execute a GET request and return the API JSON response."""
    url = f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"

    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        return {
            "success": False,
            "data": None,
            "error": str(exc),
            "endpoint": endpoint,
        }
    except ValueError as exc:
        return {
            "success": False,
            "data": None,
            "error": f"Invalid JSON response: {exc}",
            "endpoint": endpoint,
        }
