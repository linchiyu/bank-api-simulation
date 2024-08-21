import pytest
import requests

@pytest.fixture(autouse=False)
def reset_state():
    response = requests.post('http://localhost:5000/reset')
    assert response.status_code == 200


@pytest.mark.parametrize('method, route, data, expected_status, expected_response', [
    ('get', 'balance?account_id=1234', {}, 404, '0'),
    ('post', 'event', {'type': 'deposit', 'destination': '100', 'amount': 10}, 201, {'destination': {'id': '100', 'balance': 10}}),
    ('post', 'event', {'type': 'deposit', 'destination': '100', 'amount': 10}, 201, {'destination': {'id': '100', 'balance': 20}}),
    ('get', 'balance?account_id=100', {}, 200, 20),
    ('post', 'event', {'type': 'withdraw', 'origin': '200', 'amount': 10}, 404, '0'),
    ('post', 'event', {'type': 'withdraw', 'origin': '100', 'amount': 5}, 201, {'origin': {'id': '100', 'balance': 15}}),
    ('post', 'event', {'type': 'transfer', 'origin': '100', 'amount': 15, 'destination': '300'}, 201, {'origin': {'id': '100', 'balance': 0}, 'destination': {'id': '300', 'balance': 15}}),
    ('post', 'event', {'type': 'transfer', 'origin': '200', 'amount': 15, 'destination': '300'}, 404, '0'),
])
def test_post_route(method, route, data, expected_status, expected_response):
    if method == 'get':
        response = requests.get(f'http://localhost:5000/{route}')
    elif method == 'post':
        response = requests.post(f'http://localhost:5000/{route}', json=data)
    print(response.status_code)
    assert int(response.status_code) == expected_status
    assert response.text == expected_response or response.json() == expected_response

