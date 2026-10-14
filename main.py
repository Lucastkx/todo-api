from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TarefaNova(BaseModel):
    titulo: str


class Tarefa(BaseModel):
    id: int
    titulo: str
    concluido: bool =False


tarefas: list[Tarefa] = []
proximo_id = 1

@app.post("/tarefas", response_model=Tarefa,status_code=201)
def criar(dados: TarefaNova):
    global proximo_id
    tarefa = Tarefa(id=proximo_id, titulo=dados.titulo)
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa

@app.get("/tarefas")
def listar():
    return tarefas

@app.put("/tarefas/{id}")
def concluir(id:int):
    for t in tarefas:
        if t.id == id:
            t.concluido = True
            return t
    raise HTTPException(404, "Tarefa não encontrada")

@app.delete("/tarefas/{id}")
def apagar(id:int):
    for t in tarefas:
        if t.idd == id:
            tarefas.remove(t)
            return
    raise HTTPException(404, "Tarefa não encontrada")

    