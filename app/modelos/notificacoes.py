from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.banco_de_dados import Base

class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(Integer, primary_key=True, index=True)
    mensagem = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    lido = Column(Boolean, default=False)

    usuario = relationship("Usuario", backref="notificacoes")
