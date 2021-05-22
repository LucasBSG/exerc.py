produto1 = ['Camisa', 'Azul', 42.32]
produto2 = ['Chinelo', 'Preto', 2.76]
produto3 = ['Boné', 'Rosa', 25.31]

lista_de_compras = [produto1, produto2, produto3]

for produto in lista_de_compras:
    print('O produto é: %s, tem a cor %s e custa R$%.2f' % (produto[0], produto[1], produto[2]))