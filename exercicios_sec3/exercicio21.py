rodas = int(input('Quantas rodas o veículo possui? '))
print(rodas)

if rodas > 2:
    print('Pague o pedágio.')
elif rodas == 2:
    print('Não precisa pagar pedágio.')