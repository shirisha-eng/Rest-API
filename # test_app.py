# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_posts_endpoint(client):
    response = client.get('/posts')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 100

def test_users_endpoint(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 10

def test_todos_endpoint(client):
    response = client.get('/todos')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 200

def test_comments_endpoint(client):
    response = client.get('/comments')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 500