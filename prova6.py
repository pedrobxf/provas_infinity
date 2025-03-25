usuario = "pedrobxf"  
senha = "123456"
i = 0

print('Para logar no sistema informe o usuário e a senha, você tem 3 tentativas.')
while i<3:
    input_usuario = input('Digite o usuário: ')
    input_senha = input('Digite a senha: ')
    if input_usuario == usuario and input_senha == senha:
        print('Acesso permitido, seja bem vindo!')
        break
    else:
        i += 1
        print(f'Acesso negado, restam {3-i} tentativas')
else:
    for n in range(3):
        print('Acesso bloqueado, tente novamente mais tarde!')


