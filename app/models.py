from typing import List, Optional

class Curso:
    def __init__(self, id: int, nome: str, descricao: Optional[str] = None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.alunos: List[Aluno] = []

class Aluno:
    def __init__(self, id: int, nome: str, email: str, curso_id: int):
        self.id = id
        self.nome = nome
        self.email = email
        self.curso_id = curso_id

class Professor:
    def __init__(self, id: int, nome: str, email: str, curso_id: int):
        self.id = id
        self.nome = nome
        self.email = email
        self.curso_id = curso_id