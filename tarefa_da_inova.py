#tarefa_da_inovaa
#fazer em dicionarios
import uuid#gerador de ID
import html#ferramentas web
import hashlib#biblioteca de criptografia
import getpass#esquema da senha
from typing import Callable


def tela_inicial() -> bool:
    def acao_login():
        if fazer_login():
            return True
        return None
        
    def acao_cadastrar():
        cadastrar_usuario()
        return None
        
    def acao_sair():
        print("out of security system...")
        return False
        
    opcoes_inicio = {
        "1": acao_login,
        "2": acao_cadastrar,
        "0": acao_sair
    }

    while True:
        print("\n===BEM-VINDO===")
        print("1- Login | 2- registration | 0- out")
        escolha = input("Option: ")

        acao = opcoes_inicio.get(escolha)

        if acao:
            resultado = acao()
            if resultado is not None:
                return resultado
        else:
            print(" invalid option.")

def cadastrar_usuario():
    print("\n" + "=" *35);
    print("--registration screen--")
    print("=" * 35);
    novo_usuario = input("creaste a user name: ").strip().lower();
    if novo_usuario in usuarios_cadastrados:
        print("error: this user alrady exist...");
    nova_senha = getpass.getpass("create a password: ");
    hash_nova_senha = hashlib.sha256(nova_senha.encode()).hexdigest();#
    usuarios_cadastrados[novo_usuario] = hash_nova_senha;
    print(f"succes user {novo_usuario.capitalize()}, craete");

usuarios_cadastrados = {
    "admin" : "123"
}

class Task:

    def __init__(self, tittle: str, descripition : str):
        self.id = str(uuid.uuid4());
        self.tittle = tittle;
        self.descripition = descripition;
        self.status = "to do";
    
    def mostra_tarefa(self):
        print(f"[{self.status}] [{self.tittle}] (ID: {[self.id]})");
        print(f"  details: [{self.descripition}]")

class Task_Manager:
    
    def __init__(self):
        self.task = {};
    
    def create_task(self, tittle: str, descripition: str):      
        nova_tarefa = Task(tittle, descripition);
        self.task[nova_tarefa.id] = nova_tarefa;
        print(f"task creat!, ID gerate: {nova_tarefa.id}");
    
    def list_task(self):    
        if not self.task:
            print("not task found ");
            return;
        print("--work screen--");
        for task in self.task.values():
            task.mostra_tarefa();
    
    def update_task(self, id_alvo: str, novo_status : str):
        status_permitidos = ["to do", "in progress", "completed"];
        status_tratado = novo_status.lower().strip();
        if novo_status not in status_permitidos:
            self.task[id_alvo].status = status_tratado;
            print("invalid task.....");
            return;
        if id_alvo in self.task:
            self.task[id_alvo].status = novo_status;
            print("status updated");
        else:
            print("error: task not found");
    
    def delete_task(self, id_alvo: str):
        if id_alvo in self.task:
            del self.task[id_alvo];
            print(" task extinguish with succes!!");
        else:
            print("task not found");

def fazer_login() -> bool:
    print("\n" + "=" *35);
    print("login screen");
    usuario = input("user: ").strip().lower();
    senha_digitada = getpass.getpass("password: ");
    hash_da_tentativa = hashlib.sha256(senha_digitada.encode()).hexdigest();
    if usuario in usuarios_cadastrados:
        if usuarios_cadastrados[usuario] == hash_da_tentativa:
            print(f"\n access succeded, user: {usuario.capitalize()}. ");
            return True;
        else:
            print("acces deny, wrong password");
        return False;
    else:
        print("error: user not found or dont exist");
        return False

def main():
    sistema_ativo: True;
    while True: 
        autenticado = tela_inicial();
        gerenciador = Task_Manager();
        if not autenticado:
            print("System out");
            sistema_ativo = False;
        else:
            gerenciador = Task_Manager();
            rodando = True;
        #opcao = str;
        #titulo: str;
        #desc: str;
        #id_alvo = str;
        novo_st: str;
        rodando: bool = True;
        #acao: Callable[[], None] | None = opcao_menu.get(opcao);
        if not autenticado:
            print("quinting System");
            return;
        gerenciador = Task_Manager();
        rodando: bool = True;
        def menu_criar():
            titulo = input("type the tittle: ");
            titulo_seguro = html.escape(titulo);#limpar titulo da tarefa
            desc = input("type the description: ");
            gerenciador.create_task(titulo, desc);
    
        def menu_atualizar():
            id_alvo = input("type the ID of task: ").strip().replace("'", "").replace('"', '');
            novo_st = input("type a new status: ");
            gerenciador.update_task(id_alvo, novo_st);
    
        def menu_deletar():
            id_alvo = input("type the ID to delete: ");
            gerenciador.delete_task(id_alvo);
    
        opcao_menu =  {
                "1": menu_criar,
                "2": gerenciador.list_task,
                "3": menu_atualizar,
                "4": menu_deletar 
            }
        try:
            while rodando:
                print("\n --GERENCIADOR BOLADO 10.000--");
                print("1-create | 2- list | 3- update | 4. delete | 0. quit");
                opcao = input("chose: ");
                if opcao == "0":
                    print("quiting....");
                    rodando = False;
                else:
                    acao: Callable[[], None] | None = opcao_menu.get(opcao);
                    acao = opcao_menu.get(opcao);
                if acao:
                    acao();
                else:
                    print("invalid option");
        except Exception as e:
            print("error on the serv please contact suport");
        
if __name__ == "__main__":
    main();
        
