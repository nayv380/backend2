from fastapi import FastAPI

class UserCreate(BaseModel):
    nome_completo: str
    cpf: str
    email: EmailStr
    password: str
    data_nascimento: datetime = None


class UserLogin(BaseModel):
    cpf: str
    password: str


@app.post("/register", status_code=201)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    if (
        db.query(Usuario)
        .filter((Usuario.cpf == user.cpf) | (Usuario.email == user.email))
        .first()
    ):
        raise HTTPException(status_code=409, detail="CPF ou email já cadastrado.")
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
    return {
        "id_usuario": novo_usuario.id_usuario,
        "nome_completo": novo_usuario.nome_completo,
        "cpf": novo_usuario.cpf,
        "email": novo_usuario.email,
        "data_nascimento": novo_usuario.data_nascimento,
        "is_active": novo_usuario.is_active,
        "is_admin": novo_usuario.is_admin,
        "data_criacao": novo_usuario.data_criacao,
    }
