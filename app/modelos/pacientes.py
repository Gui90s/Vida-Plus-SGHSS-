from sqlalchemy import Column, Integer, String, Text
from app.banco_de_dados import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    historico_clinico = Column(Text, default="")
