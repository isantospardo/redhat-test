import requests
from requests.exceptions import ConnectionError


def test_ping():
    url = "http://localhost:8080/sample"
    try:
        res = requests.get(url).status_code
        print(res)
    except ConnectionError as e:
        print(e)
        assert False
    assert True
