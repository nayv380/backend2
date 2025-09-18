from fastapi import FastAPI, Depends, UploadFile, File
from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime
from pydantic import BaseModel, EmailStr
from db import get_db
from utils2 import enviar_email
from models import Usuario
from schemas import UserCreate, UserLogin, UserOut as User
from security import create_access_token, get_current_user
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

app = FastAPI()
origins = [
        "*"
        # Add other allowed origins here
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/auth/register", status_code=201)
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
        profissao=user.profissao,
        data_nascimento=user.data_nascimento
   
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.post("/auth/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.cpf == user.cpf).first()
    if not usuario or not verify_password(user.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="CPF ou senha inválidos.")
    access_token = create_access_token(
        data={
            "sub": usuario.id_usuario,
            "tipo": "admin" if usuario.is_admin else "regular",
        }
    )
    return {"access_token": access_token, "token_type": "bearer"}

# implementar a parte de disparo de email


# Endpoint para iniciar recuperação de senha
@app.post("/auth/forgot-password")
async def forgot_password(email: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    enviar_email(email)
    return {"msg": "E-mail de recuperação enviado"}

# Endpoint para redefinir senha
@app.post("/auth/reset-password")
async def reset_password(email: str, nova_senha: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.password_hash = get_password_hash(nova_senha)
    db.commit()
    return {"msg": "Senha redefinida com sucesso"}
# Perfil do usuário logado
@app.get("/users/me", response_model=User)
async def get_me(current_user: Usuario = Depends(get_current_user)):
    return current_user

# Atualizar perfil do usuário logado
@app.put("/users/me", response_model=User)
async def update_me(user_update: UserCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    for attr, value in user_update.dict(exclude_unset=True).items():
        setattr(current_user, attr, value)
    db.commit()
    db.refresh(current_user)
    return current_user

# Atualizar foto de perfil
@app.put("/users/me/profile-picture")
async def update_profile_picture(file: UploadFile = File(...), current_user: Usuario = Depends(get_current_user)):
    # Exemplo: salvar arquivo e atualizar campo no banco
    filename = f"profile_{current_user.id_usuario}.jpg"
    with open(filename, "wb") as f:
        f.write(await file.read())
    # current_user.profile_picture = filename
    # db.commit()
    return {"msg": "Foto de perfil atualizada"}

# Buscar usuário específico
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
# Endpoints de projetos
@app.get("/projects")
async def list_projects():
    return []

@app.get("/projects/search")
async def search_projects(q: Optional[str] = None):
    return []

@app.get("/projects/{project_id}")
async def get_project(project_id: int):
    return {}

@app.post("/projects")
async def create_project():
    return {"msg": "Projeto criado"}

@app.put("/projects/{project_id}")
async def update_project(project_id: int):
    return {"msg": "Projeto atualizado"}

@app.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    return {"msg": "Projeto excluído"}

@app.get("/users/{user_id}/projects")
async def get_user_projects(user_id: int):
    return []
# Endpoints de blog
@app.get("/blog/posts")
async def list_blog_posts():
    return []

@app.get("/blog/posts/{post_id}")
async def get_blog_post(post_id: int):
    return {}
#LEMBRAR DE CONFERIR OS NOMES DAS ROTAS
@app.get("/usuarios/por_profissao/", response_model=List[User])
async def get_usuarios_por_profissao(profissao: str, db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).filter(Usuario.profissao == profissao).all()
    if not usuarios:
        raise HTTPException(status_code=404, detail=f"Nenhum usuário encontrado com a profissão: {profissao}")
    return usuarios