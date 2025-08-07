class Veiculo:
    def __init__(self):
        return
    
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def __init__(self):
        return
    
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def __init__(self):
        return
    
    def movimentar(self):
        print("Moto está acelerando.")

veiculo1 = Veiculo()
veiculo2 = Carro()
veiculo3 = Moto()
veiculo1.movimentar()
veiculo2.movimentar()
veiculo3.movimentar()
