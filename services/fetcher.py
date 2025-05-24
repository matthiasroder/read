import requests


def fetch_html(url):
    """
    Fetch HTML content from a given URL.
    
    Args:
        url (str): The URL to fetch
        
    Returns:
        str: Raw HTML content
        
    Raises:
        requests.exceptions.RequestException: For network-related errors
        ValueError: For non-200 status codes
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        raise requests.exceptions.RequestException(f"Request to {url} timed out")
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.RequestException(f"Failed to connect to {url}")
    except requests.exceptions.HTTPError as e:
        raise ValueError(f"HTTP error {response.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")