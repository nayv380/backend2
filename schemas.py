
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    nome_completo: str
    cpf: str
    email: EmailStr
    password: str
    data_nascimento: datetime = None


class UserLogin(BaseModel):
    cpf: str
    password: str

class UserOut(BaseModel):
    id_usuario: int
    nome_completo: str
    cpf: str
    email: EmailStr
    data_nascimento: datetime = None
    is_active: bool
    is_admin: bool
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        orm_mode = True