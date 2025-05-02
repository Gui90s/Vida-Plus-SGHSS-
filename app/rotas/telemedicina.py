from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.telemedicina import Telemedicina, Base
from app.esquemas.telemedicina import CriacaoTelemedicina, TelemedicinaFinalizada, AtualizacaoTelemedicina

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TelemedicinaFinalizada)
def iniciar_teleconsulta(dados: CriacaoTelemedicina, db: Session = Depends(get_db)):
    existente = db.query(Telemedicina).filter(Telemedicina.consulta_id == dados.consulta_id).first()
    if existente:
        raise HTTPException(status_code=400, detail="Teleconsulta já criada para esta consulta.")
    nova = Telemedicina(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/{id}", response_model=TelemedicinaFinalizada)
def obter_teleconsulta(id: int, db: Session = Depends(get_db)):
    teleconsulta = db.query(Telemedicina).filter(Telemedicina.id == id).first()
    if not teleconsulta:
        raise HTTPException(status_code=404, detail="Teleconsulta não encontrada.")
    return teleconsulta

@router.put("/{id}", response_model=TelemedicinaFinalizada)
def atualizar_status_teleconsulta(id: int, dados: AtualizacaoTelemedicina, db: Session = Depends(get_db)):
    teleconsulta = db.query(Telemedicina).filter(Telemedicina.id == id).first()
    if not teleconsulta:
        raise HTTPException(status_code=404, detail="Teleconsulta não encontrada.")
    teleconsulta.status = dados.status
    db.commit()
    db.refresh(teleconsulta)
    return teleconsulta

@router.delete("/{id}")
def finalizar_teleconsulta(id: int, db: Session = Depends(get_db)):
    teleconsulta = db.query(Telemedicina).filter(Telemedicina.id == id).first()
    if not teleconsulta:
        raise HTTPException(status_code=404, detail="Teleconsulta não encontrada.")
    db.delete(teleconsulta)
    db.commit()
    return {"ok": True, "mensagem": "Teleconsulta finalizada com sucesso."}
