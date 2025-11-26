import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    data = json.loads(response.get_data(as_text=True))
    assert data["message"] == "La API funciona correctamente"

def test_predict_ok(client):
    response = client.post("/predict", json={"text": "Hola"})
    data = json.loads(response.get_data(as_text=True))
    assert data["result"] == "IA procesó tu texto: Hola"

def test_predict_error(client):
    response = client.post("/predict", json={})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert "error" in data
