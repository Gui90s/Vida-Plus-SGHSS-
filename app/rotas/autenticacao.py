from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.usuario import Usuario, Base
from app.esquemas.usuario import CriacaoUsuario, TokenAcesso
from app.servicos.autenticacao_servico import (
    hash_password, verify_password, create_access_token,
    get_current_user, is_admin, is_profissional, is_paciente
)

# Criar tabelas no banco, se ainda não existirem
Base.metadata.create_all(bind=engine)

# Criar o roteador
router = APIRouter()


# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint para registrar um novo usuário
@router.post("/registrar", response_model=TokenAcesso)
def registrar(usuario: CriacaoUsuario, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.username == usuario.username).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuário já existe.")

    novo_usuario = Usuario(
        username=usuario.username,
        hashed_password=hash_password(usuario.password),
        role=usuario.role
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    token = create_access_token({"sub": novo_usuario.username})
    return {"access_token": token, "token_type": "bearer"}


# Endpoint para login de usuário
@router.post("/login", response_model=TokenAcesso)
def login(usuario: CriacaoUsuario, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.username == usuario.username).first()
    if not db_usuario or not verify_password(usuario.password, db_usuario.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")

    token = create_access_token({"sub": db_usuario.username})
    return {"access_token": token, "token_type": "bearer"}
