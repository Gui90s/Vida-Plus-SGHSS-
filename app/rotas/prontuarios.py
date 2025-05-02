from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.prontuarios import Prontuario, Base
from app.esquemas.prontuarios import CriacaoProntuario, ProntuariosFinalizado, AtualizacaoProntuario

Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProntuariosFinalizado)
def criar_prontuario(dados: CriacaoProntuario, db: Session = Depends(get_db)):
    existe = db.query(Prontuario).filter(Prontuario.paciente_id == dados.paciente_id).first()
    if existe:
        raise HTTPException(status_code=400, detail="Paciente já possui prontuário.")
    prontuario = Prontuario(**dados.dict())
    db.add(prontuario)
    db.commit()
    db.refresh(prontuario)
    return prontuario


@router.get("/{id}", response_model=ProntuariosFinalizado)
def obter_prontuario(id: int, db: Session = Depends(get_db)):
    prontuario = db.query(Prontuario).filter(Prontuario.id == id).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado.")
    return prontuario


@router.put("/{id}", response_model=ProntuariosFinalizado)
def atualizar_prontuario(id: int, dados: AtualizacaoProntuario, db: Session = Depends(get_db)):
    prontuario = db.query(Prontuario).filter(Prontuario.id == id).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado.")

    update_data = dados.dict(exclude_unset=True)
    for chave, valor in update_data.items():
        setattr(prontuario, chave, valor)

    db.commit()
    db.refresh(prontuario)
    return prontuario
