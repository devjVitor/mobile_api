# 📱 Mobile API com FastAPI + MongoDB

Este é um projeto backend para um aplicativo mobile. Desenvolvido com **FastAPI**, ele fornece uma API para cadastro, login de usuários e envio de formulários, com armazenamento em **MongoDB**.

---

## 🚀 Tecnologias usadas

- **FastAPI** – framework web assíncrono e rápido
- **MongoDB** – banco de dados NoSQL na nuvem
- **Pymongo** – driver de comunicação com MongoDB
- **Uvicorn** – servidor ASGI para rodar o FastAPI
- **Passlib + Bcrypt** – hash de senhas
- **JWT (via python-jose)** – autenticação por token

---

## 📦 Funcionalidades

- [x] Cadastro de usuários
- [x] Login com validação de senha
- [x] Proteção de rotas com JWT
- [ ] Envio de formulário
- [ ] Integração com app mobile (Kivy)

---

## 🏗️ Estrutura do projeto

mobile_api/
├── main.py
├── database.py
├── models.py
├── auth.py
├── utils.py
├── routers/
│ ├── user_routes.py
│ └── form_routes.py
└── README.md



---

## 📌 Como rodar

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

pip install -r requirements.txt


uvicorn main:app --reload



---

### ✅ Enviar para o GitHub

Após salvar o arquivo:

```bash
git add README.md
git commit -m "Adiciona README com informações do projeto"
git push origin main
