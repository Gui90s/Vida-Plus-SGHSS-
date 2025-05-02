from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.banco_de_dados import Base

class Prontuario(Base):
    __tablename__ = "Prontuarios"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)

    diagnosticos = Column(Text, default="")
    prescricoes = Column(Text, default="")

    paciente = relationship("Paciente", backref="prontuario")
