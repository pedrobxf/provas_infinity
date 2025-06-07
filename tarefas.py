import os

tarefas = {}

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = int(input("Digite a prioridade da tarefa (1 a 5): "))
    categoria = input("Digite a categoria da tarefa: ")
    tarefas[nome] = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria
    }

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print(tarefas.keys())

def concluir_tarefa():
    nome = input("Digite o nome da tarefa concluída: ")
    if nome in tarefas:
        del tarefas[nome]
        print(f"Tarefa '{nome}' concluída e removida da lista.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def buscar_tarefa():
    nome = input("Digite o nome da tarefa a ser buscada: ")
    if nome in tarefas:
        print(tarefas[nome])
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def listar_tarefas_por_categoria():
    categoria = input("Digite a categoria para listar as tarefas: ")
    tarefas_categoria = {k: v for k, v in tarefas.items() if v["categoria"] == categoria}
    if tarefas_categoria:
        print(tarefas_categoria)
    else:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")

def ordenar_tarefas_por_prioridade():
    tarefas_ordenadas = sorted(tarefas.values(), key=lambda x: x["prioridade"])
    if tarefas_ordenadas:
        for tarefa in tarefas_ordenadas:
            print(tarefa["nome"], tarefa["prioridade"])
    else:
        print("Nenhuma tarefa cadastrada.")

def menu():
    while True:
        os.system('cls')
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Buscar tarefa")
        print("5. Listar tarefas por categoria")
        print("6. Ordenar tarefas por prioridade")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                adicionar_tarefa()
            case "2":
                listar_tarefas()
            case "3":
                concluir_tarefa()
            case "4":
                buscar_tarefa()
            case "5":
                listar_tarefas_por_categoria()
            case "6":
                ordenar_tarefas_por_prioridade()
            case "7":
                break
            case _:
                print("Opção inválida, tente novamente.")

        input('Tecle <ENTER> para continuar! ')


if __name__ == "__main__":
    menu()

