from flask import url_for
from app import create_app
import pytest


@pytest.fixture
def test_app():
    app = create_app()
    return app

def test_api_login(client):
    res = client.get(url_for('app.login'))
    assert res.json == {'ping': 'pong'}