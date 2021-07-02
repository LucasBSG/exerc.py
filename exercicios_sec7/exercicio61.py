class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastecer(self, litros):
        if self.tanque == 100:
            print('O tanque está cheio')
        else:
            self.tanque += litros
            if self.tanquetanque > 100:
                self.tanque = 100

def dirigir(self, km):
    km_litro = 10
    self.tanque -= (km / km_litro)

beetle = Carro('VW', 20000, 4, 100)

beetle.abastecer(100)

print(beetle.tanque)

beetle.dirigir(100)

print(beetle.tanque)

beetle.abastecer(10)

print(beetle.tanque)