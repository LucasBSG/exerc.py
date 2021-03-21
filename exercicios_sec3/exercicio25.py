numero = int(input('Digite um número: '))
print(numero)

if numero > 10:
    print('A operação será continuada.')
    if numero > 20:
        print('O número é maior que 20')
        print(numero * 2)
    else:
        print('O número é menor que 20')
        print(numero * 5)

else:
    print('O número não é alto o suficiente e a operação será encerrada.')