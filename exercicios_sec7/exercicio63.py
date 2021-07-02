class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome               #Classe Base, representa o ser humano normal.
        self.idade = idade

    def dizer(self):
        print('Olá todos!')

class Super_heroi(Pessoa):
    def __init__(self, nome, idade, super_poder):
        super().__init__(nome, idade)
        self.super_poder = super_poder  #classe heroi, poderes(caracteristicas) adicionados.

    def usar_poder(self):
        print('O herói usou sua habilidade de %s' %self.super_poder)


lucas = Pessoa('Lucas', 17)

lucas.dizer()

super_robson = Super_heroi('Robson', 41, 'engolir pessoas')

super_robson.dizer()

super_robson.usar_poder()