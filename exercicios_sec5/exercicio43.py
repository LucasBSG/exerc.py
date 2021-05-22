l = ['Pão','Queijo','Ovo','Salsicha','Cenoura','Alface']

item1 = input('O que você procura? ')
item2 = input('O que você vai querer depois? ')

i = 0

while i < len(l):
    if l[i] == item1:
        print('O primeiro objeto, %s foi encontrado primeiro.' % item1)
        break
    elif l[i] == item2:
        print('O segundo objeto, %s foi encontrado primeiro.' % item2)
        break

    i = i + 1