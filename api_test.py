import pytest
import requests
from config import BASE_URL, ENDPOINTS, TEST_USERS

@pytest.mark.parametrize('user', TEST_USERS)
def test_create_post(user):
    url = BASE_URL + ENDPOINTS['posts']
    response = requests.post(url, json=user)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == user['title']
    assert data['body'] == user['body']
    assert data['userId'] == user['userId']

@pytest.mark.parametrize('endpoint', ['posts', 'comments', 'todos'])
def test_get_endpoints(endpoint):
    url = BASE_URL + ENDPOINTS[endpoint]
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
