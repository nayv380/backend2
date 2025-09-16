
class Usuario(Model):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    data_nascimento = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

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
