from pydantic import BaseModel

class LeitoBase(BaseModel):
    numero: str
    tipo: str
    status: str = "disponível"

class CriacaoLeito(LeitoBase):
    pass

class AtualizacaoLeito(BaseModel):
    tipo: str | None = None
    status: str | None = None

class RecebimentoAlta(LeitoBase):
    id: int

    class Config:
        orm_mode = True
