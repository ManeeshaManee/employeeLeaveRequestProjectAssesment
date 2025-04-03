import datetime
from email.policy import default
from sqlalchemy import Column,String,Date,Integer,create_engine,and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./leave_requests.db"
engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

class LeaveRequest(Base):
    __table_name__="leave_requests"
    id=Column(Integer,primary_key=True,index=True)
    employee_id= Column(String,index=True)
    start_date= Column(Date)
    end_date=Column(Date)
    leave_type= Column(String)
    reason= Column(String)
    status= Column(String)
    working_days= Column(Integer)
    created_at=Column(Date,default=datetime.date.today)

Base.metadata.create_all(bind=engine)
