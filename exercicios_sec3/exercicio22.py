numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))


print(numero1)
print(numero2)

if numero1 > numero2:
    print('O primeiro número é maior que o segundo número.')
elif numero2 > numero1:
    print('O segundo número é maior que o primeiro número.')
else:
    print('Os dois numeros possuem o mesmo valor.')