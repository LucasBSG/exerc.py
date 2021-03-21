produto = int(input('Você deseja um produto de qual categoria? '))

if produto == 1:
    print('Então você deseja uma bolsa.')
elif produto == 2:
    print('Então você deseja um tênis.')
elif produto == 3:
    print('Então você deseja uma mochila.')
else:
    print('Esse produto não se encontra na loja.')