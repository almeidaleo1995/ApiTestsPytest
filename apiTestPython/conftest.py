import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
    # Any cleanup code can go here if needed
