import pytest
import json
import sys
import os

# Agregamos la ruta del proyecto para evitar problemas de import
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app  # importar la app de Flask

@pytest.fixture
def client():
    """
    Cliente de pruebas para Flask
    """
    with app.test_client() as client:
        yield client


def test_home(client):
    """
    Test del endpoint "/"
    """
    response = client.get("/")
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["message"] == "La API funciona"


def test_predict_ok(client):
    """
    Test de /predict con texto válido
    """
    response = client.post("/predict", json={"text": "Hola"})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data["result"] == "IA procesó tu texto: Hola"


def test_predict_error(client):
    """
    Test de /predict sin enviar texto
    """
    response = client.post("/predict", json={})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert "error" in data
