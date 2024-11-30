
import requests
from unittest.mock import patch, Mock

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

def get_token_ip():
    """
    Sends a GET request to `https://echo.free.beeceptor.com` and get IP address and Postman Token.
    
    Returns:
        A dictionary containing 'Postman-Token' and 'IP-Address'.
    """
    url = "https://echo.free.beeceptor.com"
    response = requests.get(url)
    headers = response.headers
    return{
        "token": headers.get("Postman-Token"), "ip": headers.get("X-Forwarded-For") or headers.get("Remote-Addr")
    }

def http_post_request():
    url = "https://echo.free.beeceptor.com"
    sent = {"hello": "world"}
    response = requests.post(url, json = sent)
    return response



def test_should_return_get_request():
    url = "https://pokeapi.co/api/v2/"
    response = http_get_request_url(url)

    assert response[0] == 200
    assert isinstance(response[1], dict)

def test_should_return_tuple_of_token_and_ip():
    headers = get_token_ip()
    assert "token" in headers
    assert "ip" in headers

@patch("requests.post")
def test_should_return_json_object_key_hello_value_world(mock):
    mock.return_value = Mock(status_code = 200, json = lambda: {"hello": "world"})
    response = http_post_request()
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
