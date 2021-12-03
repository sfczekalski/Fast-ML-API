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


def test_predict(client: TestClient):
    payload = {
        "texts": [
            {"text": "Examplary text"},
            {"text": "Another one"},
        ]
    }

    response = client.post(
        url="/predict",
        json=payload,
    )
    assert response.status_code == 200

    response = response.json()
    assert response["message"] == "OK"
    assert response["status-code"] == 200


def test_predict_no_texts(client: TestClient):
    payload = {"texts": []}

    response = client.post(
        url="/predict",
        json=payload,
    )

    assert response.status_code == 422

    response = response.json()
    assert response["detail"][0]["type"] == "value_error"
    assert response["detail"][0]["msg"] == "Texts list cannot be empty"
