from typing import List, Optional
from app.models import Curso, Aluno, Professor

# Inicializando listas em memória
cursos = []
alunos = []
professores = []

# Funções CRUD para Cursos
def get_cursos(skip: int = 0, limit: int = 100) -> List[Curso]:
    return cursos[skip: skip + limit]

def get_curso(curso_id: int) -> Optional[Curso]:
    return next((curso for curso in cursos if curso.id == curso_id), None)

def create_curso(curso: Curso) -> Curso:
    cursos.append(curso)
    return curso

def update_curso(curso_id: int, curso: Curso) -> Optional[Curso]:
    db_curso = get_curso(curso_id)
    if db_curso:
        db_curso.nome = curso.nome
        db_curso.descricao = curso.descricao
        return db_curso
    return None

def delete_curso(curso_id: int) -> Optional[Curso]:
    db_curso = get_curso(curso_id)
    if db_curso:
        cursos.remove(db_curso)
        return db_curso
    return None

# Funções CRUD para Alunos
def get_alunos(curso_id: int) -> List[Aluno]:
    return [aluno for aluno in alunos if aluno.curso_id == curso_id]

def create_aluno(aluno: Aluno) -> Aluno:
    alunos.append(aluno)
    return aluno

def update_aluno(aluno_id: int, aluno: Aluno) -> Optional[Aluno]:
    db_aluno = next((a for a in alunos if a.id == aluno_id), None)
    if db_aluno:
        db_aluno.nome = aluno.nome
        db_aluno.email = aluno.email
        db_aluno.curso_id = aluno.curso_id
        return db_aluno
    return None

def delete_aluno(aluno_id: int) -> Optional[Aluno]:
    db_aluno = next((a for a in alunos if a.id == aluno_id), None)
    if db_aluno:
        alunos.remove(db_aluno)
        return db_aluno
    return None

# Funções CRUD para Professores
def get_professores(curso_id: int) -> List[Professor]:
    return [professor for professor in professores if professor.curso_id == curso_id]

def create_professor(professor: Professor) -> Professor:
    professores.append(professor)
    return professor

def update_professor(professor_id: int, professor: Professor) -> Optional[Professor]:
    db_professor = next((p for p in professores if p.id == professor_id), None)
    if db_professor:
        db_professor.nome = professor.nome
        db_professor.email = professor.email
        db_professor.curso_id = professor.curso_id
        return db_professor
    return None

def delete_professor(professor_id: int) -> Optional[Professor]:
    db_professor = next((p for p in professores if p.id == professor_id), None)
    if db_professor:
        professores.remove(db_professor)
        return db_professor
    return None