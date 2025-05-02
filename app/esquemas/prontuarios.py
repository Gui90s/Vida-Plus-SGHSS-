from pydantic import BaseModel

class ProntuarioBase(BaseModel):
    paciente_id: int
    diagnosticos: str = ""
    prescricoes: str = ""

class CriacaoProntuario(ProntuarioBase):
    pass

class AtualizacaoProntuario(BaseModel):
    diagnosticos: str | None = None
    prescricoes: str | None = None

class ProntuariosFinalizado(ProntuarioBase):
    id: int

    class Config:
        orm_mode = True
