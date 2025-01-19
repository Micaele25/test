
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from app import crud, models, schemas


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    cursos = crud.get_cursos()
    return templates.TemplateResponse("index.html", {"request": request, "cursos": cursos})

@app.get("/form", response_class=HTMLResponse)
def form(request: Request, curso_id: int = None):
    curso = crud.get_curso(curso_id) if curso_id else None
    return templates.TemplateResponse("form.html", {"request": request, "curso": curso})

@app.post("/create")
def create(nome: str = Form(...), descricao: str = Form(None)):
    novo_curso = models.Curso(id=len(crud.cursos) + 1, nome=nome, descricao=descricao)
    crud.create_curso(novo_curso)
    return RedirectResponse("/", status_code=303)

@app.post("/update/{curso_id}")
def update(curso_id: int, nome: str = Form(...), descricao: str = Form(None)):
    crud.update_curso(curso_id, models.Curso(id=curso_id, nome=nome, descricao=descricao))
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{curso_id}")
def delete(curso_id: int):
    crud.delete_curso(curso_id)
    return RedirectResponse("/", status_code=303)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/cursos/", response_model=list[schemas.Curso])
def listar_cursos(skip: int = 0, limit: int = 100):
    return crud.get_cursos(skip=skip, limit=limit)

@app.get("/cursos/{curso_id}", response_model=schemas.Curso)
def buscar_curso(curso_id: int):
    db_curso = crud.get_curso(curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return db_curso

@app.post("/cursos/", response_model=schemas.Curso)
def adicionar_curso(curso: schemas.CursoCreate):
    db_curso = models.Curso(id=len(crud.cursos) + 1, nome=curso.nome, descricao=curso.descricao)
    return crud.create_curso(db_curso)

@app.put("/cursos/{curso_id}", response_model=schemas.Curso)
def atualizar_curso(curso_id: int, curso: schemas.CursoCreate):
    db_curso = crud.update_curso(curso_id, models.Curso(id=curso_id, nome=curso.nome, descricao=curso.descricao))
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return db_curso

@app.delete("/cursos/{curso_id}", response_model=schemas.Curso)
def remover_curso(curso_id: int):
    db_curso = crud.delete_curso(curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return db_curso

# Alunos
@app.post("/alunos/", response_model=schemas.Aluno)
def adicionar_aluno(aluno: schemas.AlunoCreate):
    db_aluno = models.Aluno(id=len(crud.alunos) + 1, nome=aluno.nome, email=aluno.email, curso_id=1)  # Definir curso_id de forma adequada
    return crud.create_aluno(db_aluno)

@app.get("/alunos/{curso_id}", response_model=list[schemas.Aluno])
def listar_alunos(curso_id: int):
    return crud.get_alunos(curso_id)

@app.put("/alunos/{aluno_id}", response_model=schemas.Aluno)
def atualizar_aluno(aluno_id: int, aluno: schemas.AlunoCreate):
    db_aluno = crud.update_aluno(aluno_id, models.Aluno(id=aluno_id, nome=aluno.nome, email=aluno.email, curso_id=aluno.curso_id))
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno

@app.delete("/alunos/{aluno_id}", response_model=schemas.Aluno)
def remover_aluno(aluno_id: int):
    db_aluno = crud.delete_aluno(aluno_id)
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno


# Professores
@app.post("/professores/", response_model=schemas.Professor)
def adicionar_professor(professor: schemas.ProfessorCreate):
    db_professor = models.Professor(id=len(crud.professores) + 1, nome=professor.nome, email=professor.email, curso_id=1)
    return crud.create_professor(db_professor)

@app.put("/professores/{professor_id}", response_model=schemas.Professor)
def atualizar_professor(professor_id: int, professor: schemas.ProfessorCreate):
    db_professor = crud.update_professor(professor_id, models.Professor(id=professor_id, nome=professor.nome, email=professor.email, curso_id=professor.curso_id))
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_professor

@app.delete("/professores/{professor_id}", response_model=schemas.Professor)
def remover_professor(professor_id: int):
    db_professor = crud.delete_professor(professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_professor

@app.get("/professores/{curso_id}", response_model=list[schemas.Professor])
def listar_professores(curso_id: int):
    # Retorna todos os professores de um curso específico
    return crud.get_professores(curso_id)

@app.get("/professores/{professor_id}", response_model=schemas.Professor)
def buscar_professor(professor_id: int):
    # Retorna um professor específico com base no ID
    db_professor = crud.get_professor(professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_professor
