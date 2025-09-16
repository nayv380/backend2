from fastapi import FastAPI, Depends
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr

# import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from jose import jwt, JWTError
from datetime import timedelta, datetime
from pydantic import BaseModel, EmailStr
from db import get_db
from models import Usuario

from passlib.context import CryptContext

class UserCreate(BaseModel):
    nome_completo: str
    cpf: str
    email: EmailStr
    password: str
    data_nascimento: datetime = None


class UserLogin(BaseModel):
    cpf: str
    password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

app = FastAPI()

@app.post("/register", status_code=201)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # if (
    #     db.query(Usuario)
    #     .filter((Usuario.cpf == user.cpf) | (Usuario.email == user.email))
    #     .first()
    # ):
    #     raise HTTPException(status_code=409, detail="CPF ou email já cadastrado.")
    password_hash = get_password_hash(user.password)
    novo_usuario = Usuario(
        nome_completo=user.nome_completo,
        cpf=user.cpf,
        email=user.email,
        password_hash=password_hash,
        data_nascimento=user.data_nascimento,
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

