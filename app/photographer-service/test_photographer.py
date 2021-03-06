import pytest
from starlette.testclient import TestClient
import json
from bson import json_util
import logging
from photographer_service import app
#logging.basicConfig(level=logging.DEBUG)

data1 = {'display_name': 'rdoisneau',
         'first_name': 'Robert',
         'last_name': 'Doisneau',
         'interests': ['street']
        }

data2 = {'display_name': 'hsentucq',
         'first_name': 'Hervé',
         'last_name': 'Sentucq',
         'interests': ['landscape']
        }

headers_content = {'Content-Type': 'application/json'}
headers_accept  = {'Accept': 'application/json'}

client = TestClient(app)

@pytest.mark.usefixtures("clearPhotographers")
@pytest.mark.usefixtures("initDB")
def test_post_once():
    response = client.post('/photographers',
                           headers=headers_content,
                           data=json.dumps(data1))
    assert response.headers['Location']
    assert response.status_code == 201

@pytest.mark.usefixtures("clearPhotographers")
@pytest.mark.usefixtures("initDB")
def test_post_twice():
    response1 = client.post('/photographers',
                            headers=headers_content,
                            data=json.dumps(data1))
    assert response1.status_code == 201

    response2 = client.post('/photographers',
                            headers=headers_content,
                            data=json.dumps(data1))
    assert response2.status_code == 409

@pytest.mark.usefixtures("clearPhotographers")
@pytest.mark.usefixtures("initDB")
def test_has_more_false_photographers():
    response = client.post('/photographers',
                           headers=headers_content,
                           data=json.dumps(data1))
    assert response.headers['Location']
    assert response.status_code == 201

    response2 = client.get('/photographers?offset=0&limit=10')
    assert response2.status_code == 200
    assert response2.json()['has_more'] == False

@pytest.mark.usefixtures("clearPhotographers")
@pytest.mark.usefixtures("initDB")
def test_has_more_true_photographers():
    response1 = client.post('/photographers',
                            headers=headers_content,
                            data=json.dumps(data1))

    assert response1.headers['Location']
    assert response1.status_code == 201

    response2 = client.post('/photographers',
                            headers=headers_content,
                            data=json.dumps(data2))
    assert response2.headers['Location']
    assert response2.status_code == 201

    response3 = client.get('/photographers?offset=0&limit=1')
    assert response3.status_code == 200
    assert response3.json()['has_more'] == True

@pytest.mark.usefixtures("clearPhotographers")
@pytest.mark.usefixtures("initDB")
def test_delete_one_photographer_that_exists_works():
    response = client.post('/photographers',
                           headers=headers_content,
                           data=json.dumps(data1))
    assert response.status_code == 201

    display_name = data1["display_name"]

    response = client.get(f'/photographer/{display_name}',
                           headers=headers_content)
    assert response.status_code == 200
    assert response.json()['display_name'] == display_name

    response = client.delete(f'/photographer/{display_name}',
                           headers=headers_content)
    assert response.status_code == 200

    response = client.get(f'/photographer/{display_name}',
                           headers=headers_content)
    assert response.status_code == 404

@pytest.mark.usefixtures("clearPhotographers")
@pytest.mark.usefixtures("initDB")
def test_delete_one_photographer_that_doesnt_exists_raise_404():
    display_name = data1["display_name"]

    response = client.get(f'/photographer/{display_name}',
                           headers=headers_content)
    assert response.status_code == 404

    response = client.delete(f'/photographer/{display_name}',
                           headers=headers_content)
    assert response.status_code == 404