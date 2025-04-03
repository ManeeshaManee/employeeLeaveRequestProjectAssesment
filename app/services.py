from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.models import LeaveRequest
from app.schemas import LeaveRequestCreate,LeaveRequestResponse
from fastapi import HTTPException
import datetime

def calculating_working_days(start_date,end_date):
    total_days=(end_date - start_date).days + 1
    working_days=sum(1 for i in range(total_days) if(start_date + datetime.timedelta(days=i)).weekday()<5)
    return working_days

def is_overlapping(db:Session,employee_id:str,start_date:datetime.date,end_date:datetime.date):
    existing_requests=db.qquery(LeaveRequest).filter(LeaveRequest.employee_id==employee_id),and_(LeaveRequest.start_date <= end_date,LeaveRequest.end_date>=start_date).first()
    return existing_requests is not None

def create_leave_request(db:Session,request:LeaveRequestCreate):
    if request.end_date <= request.start_date:
        raise HTTPException(status_code=400,detail="end date must be after start date ") 
    
    working_days=calculating_working_days(request.start_date,request.end_date)
    if working_days>14:
        raise HTTPException(status_code=400,detail="Maximum consecutive leave days 14") 
    
    if is_overlapping(db,request.employee_id,request.start_date,request.end_date):
        raise HTTPException(status_code=400,detail="Overlapping leave request exists")

    leave_request=LeaveRequest(**request.dict(),working_days=working_days)
    db.add(leave_request)
    db.commit
    db.refresh(leave_request)
    return leave_request

def get_leave_requests(db:Session,employee_id:str):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).all()