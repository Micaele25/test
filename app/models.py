from pydantic import BaseModel
from typing import Optional

class AlunoModel(BaseModel):
    id: int
    nome: str
    email: str
    curso_id: int
    email: Optional[str] = None

    class Config:
        orm_mode = True
