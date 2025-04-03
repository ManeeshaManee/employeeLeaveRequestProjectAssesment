from sqlalchemy.orm import sessionmaker
from app.models import engine

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()
        