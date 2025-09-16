# Backend Hackathon

Este projeto é uma API backend desenvolvida em Python utilizando FastAPI, SQLAlchemy e autenticação JWT. O objetivo é fornecer endpoints seguros para cadastro, login e gerenciamento de usuários, ideal para aplicações web e mobile que precisam de autenticação e persistência de dados.

## Funcionalidades

- Cadastro de usuários com validação de CPF, e-mail e senha
- Login de usuários com geração de token JWT
- Autenticação de rotas protegidas via Bearer Token
- Consulta de dados do usuário autenticado
- Hash de senha seguro com bcrypt
- Integração com banco de dados MySQL

## Estrutura do Projeto

```
BackendHackaton/
├── db.py           # Configuração do banco de dados e sessão
├── main.py         # Endpoints da API FastAPI
├── models.py       # Modelos ORM (SQLAlchemy)
├── schemas.py      # Schemas Pydantic para validação
├── security.py     # Funções de autenticação e geração de token
├── README.md       # Documentação do projeto
└── __pycache__/    # Arquivos de cache Python
```

## Endpoints Principais

- `POST /register` — Cadastro de novo usuário
- `POST /login` — Login e geração de token JWT
- `GET /users/me` — Consulta de dados do usuário autenticado

## Autenticação

A autenticação é feita via Bearer Token (JWT). Após o login, o usuário recebe um token que deve ser enviado no header `Authorization` para acessar rotas protegidas.

## Banco de Dados

O projeto utiliza MySQL, mas pode ser facilmente adaptado para SQLite ou outros bancos suportados pelo SQLAlchemy. A string de conexão está definida em `db.py`.

## Como rodar o projeto

1. Instale as dependências:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic passlib bcrypt pyjwt mysql-connector-python
   ```
2. Configure o banco de dados em `db.py`.
3. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Observações

- Certifique-se de definir uma chave secreta forte para o JWT em `security.py`.
- O projeto está pronto para ser expandido com novos endpoints e regras de negócio.

## Autor

Desenvolvido por mariac1995,Nayara ventura, Lucas,Pablo Marcelino,Vitor anastácio,Paula tejando, Kelly guiça, Bruna silva,Ricardo Wemerson e nossos mentores João Pedro Sales e Marcola Violento SImôes, Davi professor, WalTI professor e Gabriel Professor para o Hackathon.
