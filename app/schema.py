from pydantic import BaseModel
from typing import Optional

class AlunoBase(BaseModel):
    nome: str
    email: str
    curso_id: int

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class Config:
        orm_mode = True

class CursoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    professor_id: Optional[int] = None

    class Config:
        orm_mode = True

class ProfessorBase(BaseModel):
    nome: str
    email: str
    descricao: Optional[str] = None

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int

    class Config:
        orm_mode = True
