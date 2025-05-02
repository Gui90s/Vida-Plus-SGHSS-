from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.banco_de_dados import Base

class Telemedicina(Base):
    __tablename__ = "telemedicina"

    id = Column(Integer, primary_key=True, index=True)
    consulta_id = Column(Integer, ForeignKey("consultas.id"), nullable=False, unique=True)
    link_videochamada = Column(String, nullable=False)
    status = Column(String, default="iniciada")  # iniciada ou finalizada

    consulta = relationship("Consulta", backref="telemedicina")
