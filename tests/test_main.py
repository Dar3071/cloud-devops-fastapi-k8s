import pytest
import sys
sys.path.append('/app')

from fastapi.testclient import TestClient
from app.main import app

# Create a test client to send requests to the FastAPI app
client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Health Check status OK"}
