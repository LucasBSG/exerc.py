class Carro:

    rodas = 4   #valor constante

    def __init__(self,marca):
        self.marca = marca     #valor variável

ferrari = Carro('Ferrari')

print(ferrari.marca)
print(ferrari.rodas)