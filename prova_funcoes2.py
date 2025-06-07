def maior_numero(n1, n2, n3):
    maior = n1 if n1 > n2 else n2
    maior = maior if maior > n3 else n3
    return maior

teste1 = maior_numero(15, 7, 25)
teste2 = maior_numero(12, 9, 6)
teste3 = maior_numero(81, 225, 13)

print(teste1, teste2, teste3)
#Teste deve retornar 25, 12, 225