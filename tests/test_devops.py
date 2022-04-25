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

def test_devops_unauthorized(client: FlaskClient):
    resp = client.post('/DevOps')
    assert resp.status_code == 401


def test_devops(client: FlaskClient):
    data = {
        'message':'this is a test',
        'to':'juan',
        'from':'rita',
        'timeToLifeSec': 45
    }
    headers = {
        'content-type': "application/json",
        'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',
        'X-JWT-KWY0': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTA4ODk0NjEsIkFQSV9LRVkiOiIyZjVhZTk2Yy1iNTU4LTRjN2ItYTU5MC1hNTAxYWUxYzNmNmMifQ.dDWUgjU9WdHiN6pBdnZ94BzB4Q-n5huM1cdKB6wohdDmva2tQF1L0XtBaBTwdaMEleMbpOaEU21vSL-Hx59L3KhmkoHuwfyPipz6g74Vj0lJGBi1FE-HscXFcgwpgCjGT21hb7onYzPboXdc-x5tsyx_4cjvk_fIRapxfBzRBa_Pw7m936PoA3s1Xttkq0M6Gn7xgtZC1yS3B4y9acu3F_Se2EQy3lLcoPbgsqGuPSvQM3JC4hf0Se9r8LpLCiwwOuEl___6o5vq1gfQ4YRBqNtaLgUjbPSkqeCjjCaGWOE2xpclC0TwUi5D24lApkujTYSsS1NX0EB6LkyWej0pfA'
    }   
    resp = client.post('/DevOps', data = data, content_type="application/json", headers=headers)
    response = resp.data.decode()
    assert 'Missing token' in response
