frase = 'testando o começo da string'

print(frase.startswith('testando'))     # startswith: serve para checar se há a palavra no começo da frase

print(frase.endswith('começo'))     # endswith: serve para checar se há alguma palavra presente no fim da frase.


if(frase.endswith('começo')):
    print('Encontramos a palavra!')
else:
    print('A palavra não foi encontrada.')