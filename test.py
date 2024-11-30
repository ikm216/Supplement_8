import requests

def test_should_return_get_request():
    url = "https://pokeapi.co/api/v2/"
    response = http_get_request_url(url)

    assert response[0] == 200
    assert isinstance(response[1], dict)