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
├── banco_de_dados.py          # Configuração e conexão com o banco de dados
├── configuracoes.py           # Configurações sensíveis (JWT, etc)
│
├── rotas/                     # Endpoints da API
│   ├── autenticacao.py
│   ├── consultas.py
│   ├── leitos.py
│   ├── notificacoes.py
│   ├── pacientes.py
│   ├── profissionais.py
│   ├── prontuarios.py
│   └── telemedicina.py
│
├── modelos/                   # Modelos do banco (SQLAlchemy)
│   ├── consultas.py
│   ├── leitos.py
│   ├── notificacoes.py
│   ├── pacientes.py
│   ├── profissionais.py
│   ├── prontuarios.py
│   ├── telemedicina.py
│   └── usuario.py
│
├── esquemas/                  # Schemas de entrada e saída (Pydantic)
│   ├── consultas.py
│   ├── leitos.py
│   ├── notificacoes.py
│   ├── pacientes.py
│   ├── profissionais.py
│   ├── prontuarios.py
│   ├── telemedicina.py
│   └── usuario.py
│
└── servicos/                  # Lógicas internas e autenticação
│   └── autenticacao_servico.py

```

---

## ⚙️ Como Executar Localmente

### ✅ Pré-requisitos

- Python 3.10 ou superior
- Git
- Postman (para testar)

### 🧪 1. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 📦 2. Ative o ambiente virtual

- No **Windows**:
```bash
.venv\Scripts\activate
```

- No **Linux/macOS**:
```bash
source .venv/bin/activate
```

### 📚 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### ▶️ 4. Execute a aplicação

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
