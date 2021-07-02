class Pessoa:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

lucas = Pessoa('Lucas', 17, 'Camanducc')

print(lucas)

print(type(lucas))

print(lucas.nome)
print(lucas.idade)
print(lucas.sobrenome)

if lucas.nome == 'Lucas':
    print('O nome é Lucas')

nome = lucas.nome

print(nome)