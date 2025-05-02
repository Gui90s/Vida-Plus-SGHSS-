from fastapi import FastAPI
from app.rotas import autenticacao, pacientes, profissionais, consultas, prontuarios, telemedicina, leitos, notificacoes

app = FastAPI(title="SGHSS - Sistema de Gestão Hospitalar")

app.include_router(autenticacao.router, prefix="/auth", tags=["Autenticação"])
app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(profissionais.router, prefix="/profissionais", tags=["Profissionais de Saúde"])
app.include_router(consultas.router, prefix="/consultas", tags=["Consultas"])
app.include_router(prontuarios.router, prefix="/prontuarios", tags=["Prontuários"])
app.include_router(telemedicina.router, prefix="/telemedicina", tags=["Telemedicina"])
app.include_router(leitos.router, prefix="/leitos", tags=["Leitos"])
app.include_router(notificacoes.router, prefix="/notificacoes", tags=["Notificações"])
