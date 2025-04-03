from fastapi import APIRouter,Depends
from app.database import get_db
from app.schemas import LeaveRequestCreate,LeaveRequestResponse
from sqlalchemy.orm import Session

from app.services import create_leave_request, get_leave_requests

router=APIRouter()

@router.post("/api/v1/leave-requests",response_model=list[LeaveRequestResponse])
def create_leave(request:LeaveRequestCreate,db:Session = Depends(get_db)):
    return create_leave_request(db,request)

@router.get("/api/v1/leave-requests/{employee_id}",response_model=list[LeaveRequestResponse])
def get_leaves(employee_id:str,db:Session=Depends(get_db)):
    return get_leave_requests(db,employee_id)