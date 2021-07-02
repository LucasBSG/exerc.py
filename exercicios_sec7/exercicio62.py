class Banco():
    def __init__(self, nome, saldo):
        self.nome = nome             #definição dos valores da classe banco
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transferencia(self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor

conta_lucas = Banco('Lucas', 5000)

print(conta_lucas.nome)

conta_lucas.deposito(5000)

print(conta_lucas.saldo)

conta_lucas.saque(1500)

print(conta_lucas.saldo)

conta_paulo = Banco('Maria', 100)

conta_lucas.transferencia(conta_paulo, 300)

print(conta_paulo.saldo)

print(conta_lucas.saldo)