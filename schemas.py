
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    nome_completo: str
    cpf: str
    email: EmailStr
    password: str
    profissao: str
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
        from_attributes = True


    # Schemas para projetos
    class ProjectBase(BaseModel):
        titulo: str
        descricao: str = None
        tecnologias: str = None
        link: str = None
        imagem: str = None
        data_inicio: datetime = None
        data_conclusao: datetime = None

    class ProjectCreate(ProjectBase):
        pass

    class ProjectOut(ProjectBase):
        id: int
        usuario_id: int = None
        data_criacao: datetime
        data_atualizacao: datetime

        class Config:
            from_attributes = True

    # Schemas para posts de blog
    class BlogPostBase(BaseModel):
        titulo: str
        conteudo: str
        imagem: str = None

    class BlogPostCreate(BlogPostBase):
        pass

    class BlogPostOut(BlogPostBase):
        id: int
        autor_id: int = None
        data_publicacao: datetime

        class Config:
            from_attributes = True