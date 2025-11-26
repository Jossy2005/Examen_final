import json
from app import app as flask_app
import pytest

@pytest.fixture
def client():
    flask_app.testing = True
    return flask_app.test_client()

def test_index(client):
    r = client.get("/")
    assert r.status_code == 200

def test_ia_empty(client):
    r = client.post("/ia", json={})
    assert r.status_code == 200
    data = r.get_json()
    # Si el endpoint recibe JSON vacío -> pregunta será None o '' -> respuesta indica que escriba pregunta
    assert "Escribe" in data.get("respuesta", "") or data.get("pregunta") is None

def test_ia_simple(client):
    r = client.post("/ia", data={"pregunta": "hola mundo"})
    assert r.status_code == 200
    data = r.get_json()
    assert "hola" in data.get("respuesta") or "Respuesta" in data.get("respuesta")
