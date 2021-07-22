numero = '513'

print(numero.isdigit())     # isdigit: serve para checar se em uma função, há somente números

frase = 'oi'

print(frase.isdigit())

numero2 = '15.21'

print(numero2.replace('.', '').isdigit())       # normalmente essa função não funciona com float, porém se substituir o ponto por um espaço em branco, ela irá funcionar