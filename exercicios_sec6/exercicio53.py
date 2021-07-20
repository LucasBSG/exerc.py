def return_lista_par(l):
    nova_lista = []

    for numero in l:
        if numero % 2 == 0:             #resto 0 = par
            nova_lista.append(numero)

    return nova_lista

lista = [1,2,3,4,5,6,7,8,9]

lista_par = return_lista_par(lista)

print(lista_par)

lista2 = [32,53,26,2,8,3,4,82,63,75]

print(return_lista_par(lista2))