from sqlalchemy import Column, Integer, String
from app.banco_de_dados import Base

class Leito(Base):
    __tablename__ = "Leitos"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)  # enfermaria ou UTI
    status = Column(String, default="disponível")  # disponível ou ocupado
