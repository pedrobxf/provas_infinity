import random as rd

def lancar_dados():
    d1 = rd.randint(1, 6)
    d2 = rd.randint(1, 6)
    soma = d1 + d2
    return soma

teste = lancar_dados()
print(teste)

