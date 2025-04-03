from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./leave_requests.db"  # Ensure the database URL is correct
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Initialize database and create tables
def init_db():
    from app.models import LeaveRequest  # Import your models to ensure they are created
    Base.metadata.create_all(bind=engine)
