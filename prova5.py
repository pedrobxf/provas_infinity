print("Seja bem vindo a calculadora de notas!")

qtd_alunos = int(input("Para começar digite a quantidade de alunos: "))
lista_alunos = []

for i in range(qtd_alunos):
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a 1° nota do aluno: "))
    nota2 = float(input("Digite a 2° nota do aluno: "))
    nota3 = float(input("Digite a 3° nota do aluno: "))
    media = (nota1 + nota2 + nota3) / 3
    aprovação = "Aprovado" if media >= 7 else "Reprovado"
    tupla = (nome, nota1, nota2, nota3, media, aprovação)
    lista_alunos.append(tupla)

medias_turma = []

print("Lista de alunos:")
for aluno in lista_alunos:
    medias_turma.append(aluno[4])
    print(f"Nome: {aluno[0]} - Nota 1: {aluno[1]} - Nota 2: {aluno[2]} - Nota 3: {aluno[3]} - Média: {aluno[4]:.2f} - Aprovação: {aluno[5]}")

media_turma = sum(medias_turma) / qtd_alunos
print(f"Média da turma: {media_turma:.2f}")

