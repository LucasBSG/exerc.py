idade = int(input('Qual é a sua idade? '))

if idade >= 18:
    print('Você pode entrar na balada.')

    metodo_de_pagamento = input('Como você vai pagar sua entrada? ')

    if metodo_de_pagamento == 'em dinheiro':
        print('A fila do dinheiro é a número 1.')
    else:
        print('Para formas de pagamento que não seja em dinheiro, vá até a fila 2.')

else:
    print('Você não pode entrar na balada.')