class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return 'O nome do usuário é %s, tem %d anos e é %s'% (self.nome, self.idade, self.profissao)


lucas = Pessoa('Lucas', 17, 'Estudante')

print(lucas.__str__())