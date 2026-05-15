#sprint3
#de um script local para um servico web.
from fastapi import FastAPI;
from fastapi import HTTPExeption;
from fastapi.encoders import jsonable_encoder;
from pydantic import BaseModel;
from tarefa_da_inova import Task_Manager;
import html;

class Update_task(BaseModel):
    status: str
    
class tarefacreate(BaseModel):
    titulo: str;
    descricao: str;

app = FastAPI(
    title = "gerenciator",
    description = "test of API"
)

banco_de_dados = Task_Manager()

@app.get("/")
def raiz():
    return{"message":"serv of gerenciator online"}

@app.get("/tarefas", status_code = 200)
def listarTarefa():
    if not banco_de_dados.task:
        raise HTTPExeption (status_code = 204);
    return jsonable_encoder(banco_de_dados.task);
        
@app.post("/tarefas", status_code = 201)
def criarAtarefa(tarefa: tarefacreate):
    titulo_seguro = html.escape(tarefa.titulo);
    banco_de_dados.create_task(titulo_seguro, tarefa.descricao);
    return{ 
        "message": "task created ",
        "tittle saved": titulo_seguro
    }

@app.patch("/tarefas/{task_id}", status_code = 200)
def atualizarTarefa(task_id: str, atualizacao : Update_task):
    if task_id not in banco_de_dados.task:
        raise HTTPExeption (status_code =404, detail="task not found or dont exist");
    banco_de_dados.update_task(task_id, atualizacao.status);
    return{"message": "Status updated!"};

@app.delete("/tarefas/{task_id}", status_code = 200)
def deletartarefa(task_id: str):
    if task_id not in banco_de_dados.task:
        raise HTTPExeption (status_code =404, detail="task not found or dont exist");
    banco_de_dados.delete_task(task_id);
    return {"message": "task deletede!"}