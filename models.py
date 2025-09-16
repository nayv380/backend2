from typing import Optional
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType  # Se você planeja usar ChoiceType
# from db import engine


Model = declarative_base()

class Usuario(Model):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100))
    cpf = Column(String(11))
    email = Column(String(100))
    password_hash = Column(String(128), nullable=False)
    data_nascimento = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=datetime.now())
    data_atualizacao = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, nome_completo, cpf, email, password_hash, data_nascimento=None, is_active=True, is_admin=False):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email
        self.password_hash = password_hash
        self.data_nascimento = data_nascimento
        self.is_active = is_active
        self.is_admin = is_admin

    def __repr__(self):
        return f"<Usuario(nome_completo='{self.nome_completo}', cpf='{self.cpf}', email='{self.email}')>"
