'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main.__init__ as __init__

SECRET = os.environ.get('JWT_SECRET', 'abc123abc1234')

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    __init__.APP.config['TESTING'] = True
    client = __init__.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
