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
    profissao = Column(String(100), nullable=True)
    data_nascimento = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=datetime.now())
    data_atualizacao = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, nome_completo, cpf, email, password_hash, profissao, data_nascimento=None, is_active=True, is_admin=False):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email
        self.password_hash = password_hash
        self.profissao = profissao
        self.data_nascimento = data_nascimento
        self.is_active = is_active
        self.is_admin = is_admin
        

    def __repr__(self):
        return f"<Usuario(nome_completo='{self.nome_completo}', cpf='{self.cpf}', email='{self.email}')>"


# Modelo para projetos
class Project(Model):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=True)
    tecnologias = Column(String(200), nullable=True)
    link = Column(String(200), nullable=True)
    imagem = Column(String(200), nullable=True)
    data_inicio = Column(DateTime, nullable=True)
    data_conclusao = Column(DateTime, nullable=True)
    usuario_id = Column(Integer, nullable=True)  # Relacionamento futuro
    data_criacao = Column(DateTime, default=datetime.now())
    data_atualizacao = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, titulo, descricao=None, tecnologias=None, link=None, imagem=None, data_inicio=None, data_conclusao=None, usuario_id=None):
        self.titulo = titulo
        self.descricao = descricao
        self.tecnologias = tecnologias
        self.link = link
        self.imagem = imagem
        self.data_inicio = data_inicio
        self.data_conclusao = data_conclusao
        self.usuario_id = usuario_id

    def __repr__(self):
        return f"<Project(titulo='{self.titulo}', usuario_id='{self.usuario_id}')>"

# Modelo para posts de blog
class BlogPost(Model):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    conteudo = Column(String(2000), nullable=False)
    autor_id = Column(Integer, nullable=True)  # Relacionamento futuro
    data_publicacao = Column(DateTime, default=datetime.now())
    imagem = Column(String(200), nullable=True)

    def __init__(self, titulo, conteudo, autor_id=None, imagem=None):
        self.titulo = titulo
        self.conteudo = conteudo
        self.autor_id = autor_id
        self.imagem = imagem

    def __repr__(self):
        return f"<BlogPost(titulo='{self.titulo}', autor_id='{self.autor_id}')>"