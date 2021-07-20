class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco

civic = Carro(4, 1.0, True, 'Honda', 50000)

idea = Carro(3, 1.0, True, 'Fiat', 200000)

print(idea.teto_solar)

print(civic.preco)

if civic.teto_solar == True:
    print('O carro tem teto solar')
else:
    print('O carro não tem teto solar')


F40_Competizione = Carro(2, 2.0, False, 'Ferrari', 3000000)

print(F40_Competizione.preco)