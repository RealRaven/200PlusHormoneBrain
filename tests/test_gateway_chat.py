import pytest
from fastapi.testclient import TestClient

from gateway.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_state(client):
    r = client.get("/state")
    assert r.status_code == 200
    assert "state" in r.json()


@pytest.mark.skip(reason="Requires live vLLM service")
def test_chat_streams(client):
    r = client.post("/chat", json={"message": "hello"})
    assert r.status_code == 200