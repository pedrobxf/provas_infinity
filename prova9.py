print("---Carrinho de Compras---")

carrinho = {}

for i in range(5):
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    carrinho[produto] = valor

total = sum(carrinho.values())
print(f"O total da compra é: R$ {total:.2f}")