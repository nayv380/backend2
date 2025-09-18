

# Backend - API FastAPI

Este projeto é uma API robusta desenvolvida com FastAPI, SQLAlchemy e autenticação JWT, voltada para autenticação, gerenciamento de usuários, projetos e blog. Ideal para aplicações web/mobile que exigem segurança e persistência de dados.

## Funcionalidades

- Cadastro e login de usuários (validação de CPF, e-mail e senha)
- Recuperação e redefinição de senha por e-mail
- Perfil do usuário (GET, PUT, upload de foto)
- Gerenciamento de projetos (CRUD)
- Endpoints de blog
- Busca de usuários por profissão
- Autenticação de rotas protegidas via Bearer Token
- Hash de senha seguro com bcrypt
- Integração com banco de dados MySQL

## Estrutura do Projeto

```
backend2/
├── db.py           # Configuração do banco de dados e sessão
├── main.py         # Endpoints da API FastAPI
├── models.py       # Modelos ORM (SQLAlchemy)
├── schemas.py      # Schemas Pydantic para validação
├── security.py     # Funções de autenticação e geração de token
├── utils.py        # Funções auxiliares de e-mail
├── utils2.py       # Funções auxiliares de e-mail (HTML)
├── requirements.txt# Dependências do projeto
├── README.md       # Documentação do projeto
└── __pycache__/    # Arquivos de cache Python
```

## Dependências

Instale todas as dependências com:
```bash
pip install -r requirements.txt
```

Principais pacotes:
- fastapi
- uvicorn
- sqlalchemy
- pydantic
- passlib
- bcrypt
- pyjwt
- python-dotenv
- python-multipart
- sqlalchemy-utils
- email-validator

## Variáveis de Ambiente

Crie um arquivo `.env` (base em `.env.example`) com:
```
SECRET_KEY="sua_chave_secreta"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL="mysql+mysqlconnector://usuario:senha@localhost:3306/hackathon"
```

## Como rodar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure o banco de dados em `db.py` e as variáveis de ambiente.
3. Execute o servidor:
   ```bash
   uvicorn main:app --reload --port 8001
   ```


## Endpoints Principais

- `POST /auth/register` — Cadastro de novo usuário
- `POST /auth/login` — Login e geração de token JWT
- `GET /users/me` — Consulta de dados do usuário autenticado
- `PUT /users/me` — Atualização do perfil do usuário
- `PUT /users/me/profile-picture` — Upload de foto de perfil
- `POST /auth/forgot-password` — Recuperação de senha por e-mail
- `POST /auth/reset-password` — Redefinição de senha
- `GET /usuarios/por_profissao/` — Busca de usuários por profissão

### Endpoints de Projetos
- `GET /projects` — Listar todos os projetos
- `GET /projects/search?q=termo` — Buscar projetos por termo
- `GET /projects/{project_id}` — Detalhes de um projeto
- `POST /projects` — Criar novo projeto
- `PUT /projects/{project_id}` — Atualizar projeto
- `DELETE /projects/{project_id}` — Excluir projeto
- `GET /users/{user_id}/projects` — Listar projetos de um usuário

### Endpoints de Blog
- `GET /blog/posts` — Listar posts do blog
- `GET /blog/posts/{post_id}` — Detalhes de um post

## Modelos do Banco

### Usuário
- nome_completo, cpf, email, password_hash, profissao, data_nascimento, is_active, is_admin, data_criacao, data_atualizacao

### Projeto
- titulo, descricao, tecnologias, link, imagem, data_inicio, data_conclusao, usuario_id, data_criacao, data_atualizacao

### BlogPost
- titulo, conteudo, autor_id, data_publicacao, imagem

## Migração do Banco
Para atualizar as tabelas após mudanças nos modelos, recomenda-se usar Alembic:
```bash
pip install alembic
alembic init alembic
# Configure alembic.ini e env.py
alembic revision --autogenerate -m "Criação inicial"
alembic upgrade head
```

## Exemplo de Uso

### Cadastro de Projeto
```http
POST /projects
{
  "titulo": "Meu Portfólio",
  "descricao": "Site pessoal com projetos",
  "tecnologias": "Python, FastAPI, SQLAlchemy",
  "link": "https://meuportifolio.com",
  "imagem": "https://meuportifolio.com/img.png",
  "data_inicio": "2025-01-01T00:00:00",
  "data_conclusao": "2025-02-01T00:00:00"
}
```

### Cadastro de Post no Blog
```http
POST /blog/posts
{
  "titulo": "Como usar FastAPI",
  "conteudo": "FastAPI é um framework moderno...",
  "imagem": "https://meublog.com/img.png"
}
```

## Dicas de Deploy
- Use serviços como Heroku, Vercel, Railway ou servidores próprios.
- Configure variáveis de ambiente no serviço de hospedagem.
- Use HTTPS em produção.
- Gere e mantenha backups do banco de dados.

## Observações Técnicas
- O envio de e-mail utiliza SMTP do Gmail (veja `utils2.py`).
- As variáveis de ambiente são carregadas automaticamente com `python-dotenv`.
- O projeto está pronto para deploy e integração com frontend.
- Expanda facilmente com novos endpoints e regras de negócio.

## Autores

Desenvolvido por mariac1995, Nayara Ventura, Lucas, Pablo Marcelino, Vitor Anastácio, Paula Tejando, Kelly Guiça, Bruna Silva, Ricardo Wemerson e nossos mentores João Pedro Sales, Marcos Simões, Davi professor, WalTI professor e Gabriel professor para o Hackathon.

## Autenticação

Após o login, o usuário recebe um token JWT. Para acessar rotas protegidas, envie o token no header:
```
Authorization: Bearer <seu_token>
```

## Banco de Dados

O projeto utiliza MySQL, mas pode ser adaptado para SQLite ou outros bancos suportados pelo SQLAlchemy. Configure a string de conexão em `db.py`.

## Exemplo de Uso

### Cadastro de Usuário
```http
POST /auth/register
{
  "nome_completo": "João Silva",
  "cpf": "12345678901",
  "email": "joao@email.com",
  "password": "senha123",
  "profissao": "Desenvolvedor",
  "data_nascimento": "1990-01-01T00:00:00"
}
```

### Login
```http
POST /auth/login
{
  "cpf": "12345678901",
  "password": "senha123"
}
```

### Recuperação de Senha
```http
POST /auth/forgot-password?email=joao@email.com
```

### Redefinição de Senha
```http
POST /auth/reset-password?email=joao@email.com&nova_senha=novasenha123
```

## Observações Técnicas

- O envio de e-mail utiliza SMTP do Gmail (veja `utils2.py`).
- As variáveis de ambiente são carregadas automaticamente com `python-dotenv`.
- O projeto está pronto para deploy e integração com frontend.
- Expanda facilmente com novos endpoints e regras de negócio.

## Autores

Desenvolvido por mariac1995, Nayara Ventura, Lucas, Pablo Marcelino, Vitor Anastácio, Paula Tejando, Kelly Guiça, Bruna Silva, Ricardo Wemerson e nossos mentores João Pedro Sales, Marcos Simões, Davi professor, WalTI professor e Gabriel professor para o Hackathon.
