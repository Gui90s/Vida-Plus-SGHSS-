from pydantic import BaseModel

class PacienteBase(BaseModel):
    nome: str
    cpf: str
    endereco: str
    telefone: str
    historico_clinico: str = ""

class CriacaoPaciente(PacienteBase):
    pass

class PacienteAtendido(PacienteBase):
    id: int

    class Config:
        orm_mode = True
