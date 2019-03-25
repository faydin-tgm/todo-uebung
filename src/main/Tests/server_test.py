import server
import pytest

@pytest.fixture
def client():
    server.app.testing = True

    yield server.app.test_client()

def test_get(client):
    assert client.get('/todos').status_code == 200