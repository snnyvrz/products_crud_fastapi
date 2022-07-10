from starlette.testclient import TestClient

from app.main import app
from tests.conftest import test_app

client = TestClient(app)


def test_hello(test_app):
    response = test_app.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"hello": "world!"}
