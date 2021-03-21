numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(numero1)
print(numero2)
multiplicacao = numero1 * numero2
print(multiplicacao)

if multiplicacao == 100:
    print('%d é o número que precisamos.' % multiplicacao)
elif multiplicacao > 100:
    print('O número %d é muito alto.' % multiplicacao)
elif multiplicacao < 100:
    print('O número %d é muito baixo.' % multiplicacao)