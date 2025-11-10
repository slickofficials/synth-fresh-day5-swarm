import pytest
from application import app, service  # Your swarm from application.py

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_status(client):
    rv = client.get('/status')
    assert rv.status_code == 200
    assert rv.json == {'status': 'ok', 'counter_value': 0}

def test_increment(client):
    rv = client.get('/increment')
    assert rv.status_code == 200
    assert rv.json['status'] == 'success'
    assert rv.json['counter_value'] == 10

def test_metrics(client):
    rv = client.get('/metrics')
    assert rv.status_code == 200
    assert 'counter_requests_total' in rv.text  # Prometheus text
