valores = [1,2,3,4,5]

print(valores)

x = 0

while x < 5:
    numero = int(input('Digite um número: '))
    valores[x] = numero
    x = x + 1

print(valores)