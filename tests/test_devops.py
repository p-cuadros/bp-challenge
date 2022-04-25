import pytest
from flask.testing import FlaskClient
#from controller_devops import app
#from __init__ import app
from src.controller_devops import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client: FlaskClient):
    resp = client.get('/')
    assert resp.status_code == 200

def test_get_token(client: FlaskClient):
    resp = client.get('/get_token')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)

def test_devops(client: FlaskClient):
    resp = client.post('/DevOps')
    assert resp.status_code == 401
