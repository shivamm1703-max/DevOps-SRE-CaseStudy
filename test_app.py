
from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps and SRE Case Study" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "DevOps-SRE-CaseStudy"
