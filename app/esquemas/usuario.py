from pydantic import BaseModel

class CriacaoUsuario(BaseModel):
    username: str
    password: str
    role: str

class UsuarioDeletado(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True

class TokenAcesso(BaseModel):
    access_token: str
    token_type: str
