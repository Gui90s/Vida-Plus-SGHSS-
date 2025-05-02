from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco_de_dados import SessionLocal, engine
from app.modelos.profissionais import Profissional, Base
from app.esquemas.profissionais import CriacaoProfissional, ProfissionalDispensado

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProfissionalDispensado)
def criar_profissional(profissional: CriacaoProfissional, db: Session = Depends(get_db)):
    existente = db.query(Profissional).filter(Profissional.cpf == profissional.cpf).first()
    if existente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")
    novo = Profissional(**profissional.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[ProfissionalDispensado])
def listar_profissionais(db: Session = Depends(get_db)):
    return db.query(Profissional).all()

@router.get("/{id}", response_model=ProfissionalDispensado)
def obter_profissional(id: int, db: Session = Depends(get_db)):
    profissional = db.query(Profissional).filter(Profissional.id == id).first()
    if not profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado.")
    return profissional

@router.put("/{id}", response_model=ProfissionalDispensado)
def atualizar_profissional(id: int, dados: CriacaoProfissional, db: Session = Depends(get_db)):
    profissional = db.query(Profissional).filter(Profissional.id == id).first()
    if not profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado.")
    for chave, valor in dados.dict().items():
        setattr(profissional, chave, valor)
    db.commit()
    db.refresh(profissional)
    return profissional

@router.delete("/{id}")
def deletar_profissional(id: int, db: Session = Depends(get_db)):
    profissional = db.query(Profissional).filter(Profissional.id == id).first()
    if not profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado.")
    db.delete(profissional)
    db.commit()
    return {"ok": True, "mensagem": "Profissional removido com sucesso."}
