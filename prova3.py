senha = 7
cont = 0
print("-----JOGO DOS NÚMEROS-----")
print("Olá, seja bem vindo ao jogo dos números. Para vencer você deve adivinhar o número que pensei entrei 1 e 10. Você tem 3 tentativas, boa sorte!")
while cont < 3:
    tentativa = int(input("Qual número estou pensando? "))
    if tentativa == senha:
        print("Parabéns, você acertou, ótimo jogo!")
        break
    else:
        print("Número errado, tente novamente, você consegue!")
        cont += 1
else:
    print("Que pena, suas chances acabaram e você perdeu! O número era o 7.")
