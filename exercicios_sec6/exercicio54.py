def calc_media(lista):
    media = 0
    soma = 0

    for n in lista:
        soma += n

    media = soma / len(lista)

    return media

notas = [7,3,10]

media_provas = calc_media(notas)

print(media_provas)