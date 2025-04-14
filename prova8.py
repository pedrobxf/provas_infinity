print("---Agenda de contatos---")
agenda = {}
resp = input("Deseja salvar um novo contato? (S/N): ") 
if resp.upper() == "S":
    agenda["Nome"] = input("Digite o nome do contato: ") 
    agenda["Telefone"] = input("Digite o telefone do contato: ") 
    agenda["E-mail"] = input("Digite o e-mail do contato: ")

    print("Contato adicionado com sucesso!")
    print("Nome:", agenda["Nome"])
    print("Telefone:", agenda["Telefone"])
    print("E-mail:", agenda["E-mail"])
else:
    print("Nenhum contato foi adicionado.")

