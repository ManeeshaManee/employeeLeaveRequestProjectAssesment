from app.services import create_leave_request
from app.models import Base,engine,SessionLocal
from app.schemas import LeaveRequestCreate
import pytest
import datetime


Base.metadata.create_all(bind=engine)

def test_create_leave_request():
    db=SessionLocal()
    request=LeaveRequestCreate(
        id= "LR001",
        employee_id= "EMP001",
        start_date="2025-03-01",
        end_date="2025-03-05",
        leave_type= "ANNUAL",
        reason= "Family vacation to visit parents",
        status= "PENDING",
        working_days=3,
        created_at= "2025-02-11T10:00:00Z",
    )
    leave=create_leave_request(db,request)
    assert leave.employee_id=="EMP001"
    db.close()