from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.pacientes import Paciente, Base
from app.esquemas.pacientes import CriacaoPaciente, PacienteAtendido

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PacienteAtendido)
def criar_paciente(paciente: CriacaoPaciente, db: Session = Depends(get_db)):
    db_paciente = db.query(Paciente).filter(Paciente.cpf == paciente.cpf).first()
    if db_paciente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")
    novo = Paciente(**paciente.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[PacienteAtendido])
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(Paciente).all()

@router.get("/{id}", response_model=PacienteAtendido)
def obter_paciente(id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    return paciente

@router.put("/{id}", response_model=PacienteAtendido)
def atualizar_paciente(id: int, dados: CriacaoPaciente, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    for chave, valor in dados.dict().items():
        setattr(paciente, chave, valor)
    db.commit()
    db.refresh(paciente)
    return paciente

@router.delete("/{id}")
def deletar_paciente(id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    db.delete(paciente)
    db.commit()
    return {"ok": True, "mensagem": "Paciente removido com sucesso."}
