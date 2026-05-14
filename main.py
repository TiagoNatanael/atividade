#sprint3
#de um script local para um servico web.
import html;
from fastapi import FastAPI;
from tarefa_da_inova import Task_Manager;

app = FastAPI(
    title = "gerenciador",
    description = "teste de API"
)

banco_de_dados = Task_Manager()

@app.get("/")
def raiz():
        return{"mensagem": "servidor gerenciador online"};

class tarefacreate:
    titulo: str;
    descricao: str;

@app.post("/tarefas ", status_code= 201)
def criarAtarefa(tarefa: tarefacreate):
    titulo_seguro = html.escape(tarefa.titulo);
    banco_de_dados.creat_task(titulo_seguro, tarefa.desccricao);
    return{ 
        "mensagem": "tarefa criada ",
        "titulo salvo": titulo_seguro
    }