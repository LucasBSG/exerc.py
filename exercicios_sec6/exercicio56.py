def reune_dados(nome, idade, profissao, fnct):
    apresentacao = fnct(nome, idade, profissao)
    return apresentacao

def apresenta_dados(nome, idade, profissao):
    frase = 'O nome dele é %s, tem %d anos e é %s'% (nome, idade, profissao)
    return frase

print(reune_dados('Lucas', 17, 'Estudante', apresenta_dados))

apresentacao = reune_dados('Robson', 41, 'Programador', apresenta_dados)

print(apresentacao)