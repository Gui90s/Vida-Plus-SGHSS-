from pydantic import BaseModel
from datetime import date, time

class ConsultaBase(BaseModel):
    data: date
    hora: time
    tipo: str  # presencial ou telemedicina
    paciente_id: int
    profissional_id: int

class CriacaoConsulta(ConsultaBase):
    pass

class ConsultaFinalizada(ConsultaBase):
    id: int

    class Config:
        orm_mode = True
