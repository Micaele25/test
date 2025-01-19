from pydantic import BaseModel
from typing import List, Optional

class CursoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    alunos: List[str] = []

    class Config:
        from_attributes = True  # Atualização do Pydantic v2

class AlunoBase(BaseModel):
    nome: str
    email: str

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int
    curso_id: int

    class Config:
        from_attributes = True  # Atualização do Pydantic v2

class ProfessorBase(BaseModel):
    nome: str
    email: str

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int
    curso_id: int

    class Config:
        from_attributes = True  # Atualização do Pydantic v2
