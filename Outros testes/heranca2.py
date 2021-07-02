class Pessoas:
    def dizer(self):            #Criação de classe pai
        print('Olá todos!')

class Lucas(Pessoas):
    def dizer(self):            #Classes filhas(lucas e Roberto)
        print('Sou o Lucas')

class Roberto(Pessoas):
    pass

lucas = Lucas()

lucas.dizer()

roberto = Roberto()

roberto.dizer()