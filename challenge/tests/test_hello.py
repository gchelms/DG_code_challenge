import os
import pytest
import url_for


from challenge import challenge

@pytest.fixture
def test_app(client):
    assert client.get(url_for('/')).status_code == 200
    
def start(client, result, result1 = 9, result2 = 3):
    rv = client.post('/', data={ 'result': result})
    if result:
        assert b'3' in rv.data
    return rv
    

