class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError("Saldo insuficiente para saque")
    
    def exibir_saldo(self):
        print(f"Saldo: R$ {self.__saldo:.2f}")

    def exibir_titular(self):
        print(f"Titular: {self.__titular}")

    def transferir(self, valor, conta_destino):
        try:
            self.sacar(valor)
        except ValueError as e:
            print(e)
        else:
            conta_destino.depositar(valor)


