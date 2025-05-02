from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.consultas import Consulta, Base
from app.esquemas.consultas import CriacaoConsulta, ConsultaFinalizada

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ConsultaFinalizada)
def criar_consulta(consulta: CriacaoConsulta, db: Session = Depends(get_db)):
    nova = Consulta(**consulta.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/", response_model=list[ConsultaFinalizada])
def listar_consultas(db: Session = Depends(get_db)):
    return db.query(Consulta).all()

@router.get("/{id}", response_model=ConsultaFinalizada)
def obter_consulta(id: int, db: Session = Depends(get_db)):
    consulta = db.query(Consulta).filter(Consulta.id == id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada.")
    return consulta

@router.put("/{id}", response_model=ConsultaFinalizada)
def atualizar_consulta(id: int, dados: CriacaoConsulta, db: Session = Depends(get_db)):
    consulta = db.query(Consulta).filter(Consulta.id == id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada.")
    for chave, valor in dados.dict().items():
        setattr(consulta, chave, valor)
    db.commit()
    db.refresh(consulta)
    return consulta

@router.delete("/{id}")
def deletar_consulta(id: int, db: Session = Depends(get_db)):
    consulta = db.query(Consulta).filter(Consulta.id == id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada.")
    db.delete(consulta)
    db.commit()
    return {"ok": True, "mensagem": "Consulta cancelada com sucesso."}
