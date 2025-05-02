# 🏥 Vida-Plus-SGHSS- Sistema de Gestão Hospitalar e de Serviços de Saúde
Este projeto tem como objetivo oferecer uma solução completa para a gestão de pacientes, profissionais de saúde, consultas, leitos, prontuários, telemedicina e notificações em instituições hospitalares, clínicas ou postos de saúde.

---

## 🚀 Funcionalidades

- 🔐 Autenticação com controle de acesso (admin, profissional, paciente)
- 👩‍⚕️ Cadastro e gerenciamento de **pacientes** e **profissionais**
- 📅 Agendamento e controle de **consultas**
- 📂 Registro e edição de **prontuários**
- 🛏️ Controle de **leitos hospitalares**
- 💻 **Telemedicina** com links para atendimento remoto
- 🔔 Sistema de **notificações** por usuário
- 📊 API RESTful com documentação automática via Swagger

---

## 📁 Estrutura do Projeto

```
app/
│
├── principal.py               # Ponto de entrada da aplicação
├── banco.py                   # Configuração e conexão com o banco de dados
├── config.py                  # Configurações sensíveis (JWT, etc)
│
├── rotas/                     # Endpoints da API
│   ├── autenticacao.py
│   ├── pacientes.py
│   ├── profissionais.py
│   ├── consultas.py
│   ├── prontuarios.py
│   ├── telemedicina.py
│   ├── leitos.py
│   └── notificacoes.py
│
├── modelos/                   # Modelos do banco (SQLAlchemy)
│   ├── autenticacao.py
│   ├── pacientes.py
│   ├── profissionais.py
│   ├── consultas.py
│   ├── prontuarios.py
│   ├── telemedicina.py
│   ├── leitos.py
│   └── notificacoes.py
├── esquemas/                  # Schemas de entrada e saída (Pydantic)
│   ├── autenticacao.py
│   ├── pacientes.py
│   ├── profissionais.py
│   ├── consultas.py
│   ├── prontuarios.py
│   ├── telemedicina.py
│   ├── leitos.py
│   └── notificacoes.py

└── servicos/                  # Lógicas internas e autenticação
```

---

## ⚙️ Como Executar Localmente

### ✅ Pré-requisitos

- Python 3.10 ou superior
- Git
- Postman (para testar)

### 📥 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sghss.git
cd sghss
```

### 🧪 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 📦 3. Ative o ambiente virtual

- No **Windows**:
```bash
.venv\Scripts\activate
```

- No **Linux/macOS**:
```bash
source .venv/bin/activate
```

### 📚 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### ▶️ 5. Execute a aplicação

```bash
uvicorn app.principal:app --reload
```

### 🌐 Acesse no navegador:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testes com o Postman

- Importe o arquivo `SGHSS_Postman_Grupo_Completo.json` fornecido
- Faça login com o endpoint `/auth/login`
- Copie o `access_token` retornado e cole na variável `{{token}}` da coleção
- Teste os demais endpoints agrupados por funcionalidade

---

## 📜 Licença

Este projeto é de uso acadêmico e educacional. Modificações são bem-vindas!

---

## ✍️ Conclusão

O SGHSS foi desenvolvido com carinho, foco na organização do código e compromisso com as boas práticas de desenvolvimento backend. Cada funcionalidade representa o esforço de unir a tecnologia à gestão da saúde de maneira prática, humana e eficiente.

---
