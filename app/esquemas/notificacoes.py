from pydantic import BaseModel

class NotificacaoBase(BaseModel):
    mensagem: str
    usuario_id: int

class CriacaoNoificacao(NotificacaoBase):
    pass

class NotificacaoFinalizada(NotificacaoBase):
    id: int
    lido: bool

    class Config:
        from_attributes = True
