numeros = [100,150,200,300,400]

busca = int(input('Que número deseja buscar? '))

encontrado = False

for n in numeros:
    if n == busca:
        print('O número %d foi encontrado!'% n)
        encontrado = True


if encontrado == False:
    print('Não encontramos o determinado número.')