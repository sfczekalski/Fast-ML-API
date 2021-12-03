import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> TestClient:
    """Test client fixture.

    Returns:
        TestClient: The test client.
    """
    from app.api import app

    return TestClient(app)


def test_smoke(client: TestClient):
    pass


def test_health(client: TestClient):
    response = client.get("/health")

    assert response.status_code == 200

    response = response.json()

    assert response["message"] == "OK"
    assert response["status-code"] == 200
    assert response["data"] == {}
