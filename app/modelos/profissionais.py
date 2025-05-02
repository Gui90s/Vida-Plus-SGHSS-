from sqlalchemy import Column, Integer, String
from app.banco_de_dados import Base

class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    especialidade = Column(String, nullable=False)
    agenda = Column(String, default="")  # JSON string ou estrutura simplificada de agenda
