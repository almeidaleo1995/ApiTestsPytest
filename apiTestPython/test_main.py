import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
# Test for creating QA
def test_create_qa():
    data = {"id": 1, "name": "John", "country": "Brazil"}
    response = client.post("/qa", json=data)
    assert response.status_code == 200
    assert response.json() == data

# Test for reading QA
def test_read_qa():
    response = client.get("/qa/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John", "country": "Brazil"}

# Test for updating QA
def test_update_qa():
    # Primeiro, criamos uma QA para atualizar
    create_data = {"id": 1, "name": "John", "country": "Brazil"}
    client.post("/qa", json=create_data)

    # Agora, tentamos atualizar a QA
    update_data = {"id": 1, "name": "Math", "country": "USA"}
    response = client.put("/qa/1", json=update_data)

    assert response.status_code == 200
    updated_qa = response.json()
    assert updated_qa["name"] == update_data["name"]
    assert updated_qa["country"] == update_data["country"]


# Test for deleting QA
def test_delete_qa():
    response = client.delete("/qa/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Math", "country": "USA"}


# Test for reading QA after deletion
def test_read_qa_not_found():
    response = client.get("/qa/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "QA not found"}  # Check for "detail" instead of "error"


