from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.leitos import Leito, Base
from app.esquemas.leitos import CriacaoLeito, RecebimentoAlta, AtualizacaoLeito

Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=RecebimentoAlta)
def cadastrar_leito(dados: CriacaoLeito, db: Session = Depends(get_db)):
    existente = db.query(Leito).filter(Leito.numero == dados.numero).first()
    if existente:
        raise HTTPException(status_code=400, detail="Número do leito já cadastrado.")
    leito = Leito(**dados.dict())
    db.add(leito)
    db.commit()
    db.refresh(leito)
    return leito


@router.get("/", response_model=list[RecebimentoAlta])
def listar_leitos(db: Session = Depends(get_db)):
    return db.query(Leito).all()


@router.get("/{id}", response_model=RecebimentoAlta)
def obter_leito(id: int, db: Session = Depends(get_db)):
    leito = db.query(Leito).filter(Leito.id == id).first()
    if not leito:
        raise HTTPException(status_code=404, detail="Leito não encontrado.")
    return leito


@router.put("/{id}", response_model=RecebimentoAlta)
def atualizar_leito(id: int, dados: AtualizacaoLeito, db: Session = Depends(get_db)):
    leito = db.query(Leito).filter(Leito.id == id).first()
    if not leito:
        raise HTTPException(status_code=404, detail="Leito não encontrado.")

    update_data = dados.dict(exclude_unset=True)
    for chave, valor in update_data.items():
        setattr(leito, chave, valor)

    db.commit()
    db.refresh(leito)
    return leito


@router.delete("/{id}")
def excluir_leito(id: int, db: Session = Depends(get_db)):
    leito = db.query(Leito).filter(Leito.id == id).first()
    if not leito:
        raise HTTPException(status_code=404, detail="Leito não encontrado.")
    db.delete(leito)
    db.commit()
    return {"ok": True, "mensagem": "Leito removido com sucesso."}
