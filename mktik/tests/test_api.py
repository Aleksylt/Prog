import pytest
from fastapi.testclient import TestClient

from app.main import app as web_app

client = TestClient(web_app)


def test_main_url():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
