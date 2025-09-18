from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Model

import os 

# Configuração para MySQL (comentada)
# Exemplo:
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:125213@localhost:3306/hackathon"

# Configuração para SQLite (ativa)
    


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

# Criação automática das tabelas ao importar db.py
Model.metadata.create_all(bind=engine)