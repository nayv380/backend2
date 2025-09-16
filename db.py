from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Model
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:12345678@127.0.0.1:3306/hackathon'
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
if __name__ == "__main__":
    Model.metadata.create_all(bind=engine)