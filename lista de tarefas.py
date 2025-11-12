tarefas = []

def cold_quintoB ():
    print("====== opções ======")
    print("[1] listar tarefas")
    print("[2] adicionar tarefas")
    print("[3] excluir tarefas")
    print("[4] sair")


def adicionar_tarefa ():
    tarefa = input("qual tarefa voc gostaria de adicionar?   ")
    ("tarefa adicionada com sucesso!")
    tarefas.append(tarefa)


def listar_tarefas():

        if len(tarefas)  > 0:
         print("estou listando suas tarefas! ")
         for posicao, tarefa in enumerate(tarefas):
              print(f"{posicao} - {tarefa}")
        else:
            print("não tem tarefas disponiveis")

def excluir_tarefas ():
    if len (tarefas) > 0:
        listar_tarefas ()
        tarefa_para_excluir = int(input("Qual tarefa voce deseja excluir? "))
        tarefas.pop(tarefa_para_excluir)








while True:
   
    cold_quintoB()
    opção = input ("qual o seu comando ?   ")

    print("=========================")

    if opção == "1":
         listar_tarefas()

    elif opção == "2":
        adicionar_tarefa()


    elif opção == "3":
         excluir_tarefas ()
         
    else:
         print("eu não conheço esse comando")

    print("=========================")