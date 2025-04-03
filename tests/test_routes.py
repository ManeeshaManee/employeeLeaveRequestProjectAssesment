from fastapi.testclient import TestClient
from app.main import app

test_client= TestClient()

def test_create_leave():
    response=test_client.post("/api/v1/leave-requests",json={
        "employee_id": "EMP001",
        "start_date": "2025-03-01",
        "end_date": "2025-03-05",
        "leave_type": "ANNUAL",
        "reason": "Family vacation to visit parents"

    })
    assert response.status_code==200

def test_get_leave_request():
    response=test_client.get("/api/v1/leave-requestsEMP001")
    assert response.status_code==200