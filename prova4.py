print("Nesse programa iremos calcular a soma dos números pares em um intervalo")
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
soma = 0
for i in range(inicio, fim+1):
    if i % 2 == 0:
        soma += i
if soma != 0:
    print(f"A soma dos números pares no intervalo é {soma}")
else:
    print("Não há números pares no intervalo")