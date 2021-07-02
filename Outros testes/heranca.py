class Veículos:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print('Vruuum!')

class Carro(Veículos):
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas, marca)
        self.teto_solar = teto_solar

f458 = Carro(4, 'Ferrari', False)

print(f458.rodas)

f458.ligar()

print(f458.teto_solar)

class Moto(Veículos):
    def __init__(self, rodas, marca, protec_lateral):
        super().__init__(rodas, marca)
        self.protec_lateral = protec_lateral

    def empinar(self):
        print('Empinando a moto!')


xj6 = Moto(2, 'Yamaha', True)

print(xj6.marca)

xj6.empinar()

xj6.ligar()