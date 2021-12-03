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
