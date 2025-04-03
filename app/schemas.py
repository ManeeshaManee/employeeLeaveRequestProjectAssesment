from pydantic import BaseModel,Field
import datetime

class LeaveRequestCreate(BaseModel):
    employee_id: str = Field(...)
    start_date : datetime.date
    end_date: datetime.date
    leave_type: str = Field(...,regex="^(ANNUAL|SICK|PERSONAL)$")
    reason:str=Field(...,min_length= 10)


class LeaveRequestResponse(LeaveRequestCreate):
    id:int
    status:str
    working_days:int
    leave_type:str
    created_at:datetime.date
