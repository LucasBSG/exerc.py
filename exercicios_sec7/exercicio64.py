class Mamiferos:                                #Classe pai
    def __init__(self, orelhas, patas):
        self.orelhas = orelhas
        self.patas = patas

    def comer(self):
        print('Agora o mamífero está comendo!')

class Cachorro(Mamiferos):                                 #classe filha
    def __init__(self, orelhas, patas, cor_do_pelo):
        super().__init__(orelhas, patas)               #características vindas da classe pai
        self.cor_do_pelo = cor_do_pelo

    def latir(self):
        print('Au au!')


class Gato(Mamiferos):
    def __init__(self, orelhas, patas, bigode):
        super().__init__(orelhas, patas)
        self.bigode = bigode

    def miar(self):
        print('Miauu!')


buster = Cachorro(2,4,'caramelo')

buster.comer()
buster.latir()

print(buster.orelhas)

thor = Gato(2, 4, True)

thor.comer()

thor.miar()

print(thor.bigode)