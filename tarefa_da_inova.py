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
        print("Saindo do sistema de segurança...")
        return False
        
    opcoes_inicio = {
        "1": acao_login,
        "2": acao_cadastrar,
        "0": acao_sair
    }

    while True:
        print("\n===BEM-VINDO===")
        print("1- Login | 2- Cadastrar | 0- Sair")
        escolha = input("Opção: ")

        acao = opcoes_inicio.get(escolha)

        if acao:
            resultado = acao()
            if resultado is not None:
                return resultado
        else:
            print(" Opção invalida.")

def cadastrar_usuario():
    print("\n" + "=" *35);
    print("--tela de cadastro--")
    print("=" * 35);
    novo_usuario = input("crie um nome de usuario: ").strip().lower();
    if novo_usuario in usuarios_cadastrados:
        print("erro: esse usario ja existe...");
    nova_senha = getpass.getpass("crie uma senha: ");
    hash_nova_senha = hashlib.sha256(nova_senha.encode()).hexdigest();#
    usuarios_cadastrados[novo_usuario] = hash_nova_senha;
    print(f"sucesso usario {novo_usuario.capitalize()}, cadastrado");

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
        print(f"  detalhes: [{self.descripition}]")

class Task_Manager:
    
    def __init__(self):
        self.task = {};
    
    def create_task(self, tittle: str, descripition: str):      
        nova_tarefa = Task(tittle, descripition);
        self.task[nova_tarefa.id] = nova_tarefa;
        print(f"tarefa criada!, ID gerado: {nova_tarefa.id}");
    
    def list_task(self):    
        if not self.task:
            print("nenhuma terafa encontrada");
            return;
        print("--lista de terafas--");
        for task in self.task.values():
            task.mostra_tarefa();
    
    def update_task(self, id_alvo: str, novo_status : str):
        status_permitidos = ["to do", "in progress", "completed"];
        status_tratado = novo_status.lower().strip();
        if novo_status not in status_permitidos:
            self.task[id_alvo].status = status_tratado;
            print("tarefa invalida...caloteiro");
            return;
        if id_alvo in self.task:
            self.task[id_alvo].status = novo_status;
            print("status atualizado");
        else:
            print("erro: tarefa nao encontrada");
    
    def delete_task(self, id_alvo: str):
        if id_alvo in self.task:
            del self.task[id_alvo];
            print("terafa expurgada com sucesso!!");
        else:
            print("tarefa nao encontrada");

def fazer_login() -> bool:
    print("\n" + "=" *35);
    print("tela de login");
    usuario = input("usuario: ").strip().lower();
    senha_digitada = getpass.getpass("senha: ");
    hash_da_tentativa = hashlib.sha256(senha_digitada.encode()).hexdigest();
    if usuario in usuarios_cadastrados:
        if usuarios_cadastrados[usuario] == hash_da_tentativa:
            print(f"\n acesso concedido, usario: {usuario.capitalize()}. ");
            return True;
        else:
            print("acesso negado, senha encorreta");
        return False;
    else:
        print("erro: usuariio não encotrado ou não existe");
        return False

def main():
    sistema_ativo: True;
    while True: 
        autenticado = tela_inicial();
        gerenciador = Task_Manager();
        if not autenticado:
            print("sistema encerrrado");
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
            print("encerrando o sistema");
            return;
        gerenciador = Task_Manager();
        rodando: bool = True;
        def menu_criar():
            titulo = input("digito o titulo: ");
            titulo_seguro = html.escape(titulo);#limpar titulo da tarefa
            desc = input("degite a descricao: ");
            gerenciador.create_task(titulo, desc);
    
        def menu_atualizar():
            id_alvo = input("digite o ID da tarefa: ").strip().replace("'", "").replace('"', '');
            novo_st = input("digite o novo status: ");
            gerenciador.update_task(id_alvo, novo_st);
    
        def menu_deletar():
            id_alvo = input("digite o ID para deletar: ");
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
                print("1-criar | 2- listar | 3- atualizar | 4. deletar | 0. sair");
                opcao = input("escolha: ");
                if opcao == "0":
                    print("saindo.....bixo caloteiro");
                    rodando = False;
                else:
                    acao: Callable[[], None] | None = opcao_menu.get(opcao);
                    acao = opcao_menu.get(opcao);
                if acao:
                    acao();
                else:
                    print("opcao invalida");
        except Exception as e:
            print("erro no servido contade ao suporte");
        
if __name__ == "__main__":
    main();
        
