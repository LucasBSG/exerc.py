class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def ligar(self):
        print('Ligando os motores')

    def mudar_preco(self, novo_preco):
        self.preco = novo_preco

i8 = Carro('BMW', 500000)

print(i8.marca)

print(i8.preco)

i8.ligar()

i8.mudar_preco(420000)

print(i8.preco)