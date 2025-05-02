from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.modelos.notificacoes import Notificacao, Base
from app.banco_de_dados import SessionLocal, engine
from app.esquemas.notificacoes import CriacaoNoificacao, NotificacaoFinalizada
from app.servicos.autenticacao_servico import get_current_user

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NotificacaoFinalizada)
def criar_notificacao(nova: CriacaoNoificacao, db: Session = Depends(get_db)):
    notificacao = Notificacao(**nova.dict())
    db.add(notificacao)
    db.commit()
    db.refresh(notificacao)
    return notificacao

@router.get("/", response_model=list[NotificacaoFinalizada])
def listar_notificacoes(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Notificacao).filter(Notificacao.usuario_id == user.id).all()

@router.put("/{id}/lido", response_model=NotificacaoFinalizada)
def marcar_como_lida(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    notificacao = db.query(Notificacao).filter(Notificacao.id == id, Notificacao.usuario_id == user.id).first()
    if not notificacao:
        raise HTTPException(status_code=404, detail="Notificação não encontrada")
    notificacao.lido = True
    db.commit()
    db.refresh(notificacao)
    return notificacao
