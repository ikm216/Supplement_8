import requests

def http_get_request_url(url):
    """
    Sends an HTTP GET request to the specified URL and returns the status code and response data.

    Args:
        url: The URL to send the GET request to.

    Returns:
        A tuple of the HTTP status code of the response and the JSON-parsed response data if the status code is 200.

    Raises:
        Exception: If the HTTP status code is not 200, an exception is raised
    """
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return response.status_code, pokemon_data
    else:
        raise Exception(f"Failed to get: {response.status}")

def test_should_return_get_request():
    url = "https://pokeapi.co/api/v2/"
    response = http_get_request_url(url)

    assert response[0] == 200
    assert isinstance(response[1], dict)