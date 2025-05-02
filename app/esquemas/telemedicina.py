from pydantic import BaseModel

class TelemedicinaBase(BaseModel):
    consulta_id: int
    link_videochamada: str
    status: str = "iniciada"

class CriacaoTelemedicina(TelemedicinaBase):
    pass

class AtualizacaoTelemedicina(BaseModel):
    status: str

class TelemedicinaFinalizada(TelemedicinaBase):
    id: int

    class Config:
        orm_mode = True
