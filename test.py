import requests

def http_get_request_url(url):
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