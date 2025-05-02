from pydantic import BaseModel

class ProfissionalBase(BaseModel):
    nome: str
    cpf: str
    especialidade: str
    agenda: str = ""

class CriacaoProfissional(ProfissionalBase):
    pass

class ProfissionalDispensado(ProfissionalBase):
    id: int

    class Config:
        orm_mode = True
