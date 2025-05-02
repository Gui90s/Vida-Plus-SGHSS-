from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.banco_de_dados import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    tipo = Column(String, nullable=False)  # presencial ou telemedicina

    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)

    # Relacionamentos (opcional para uso com ORM)
    paciente = relationship("Paciente", backref="consultas")
    profissional = relationship("Profissional", backref="consultas")
