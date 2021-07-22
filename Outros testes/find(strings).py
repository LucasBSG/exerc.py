frase = 'Como você acordou hoje? Feliz, ou triste?'

print(frase.find('Feliz'))      # find: vê em que indice determinada palavra começa

if frase.find('Feliz') >= 0:
    print('Palavra feliz encontrada!')


print(frase.find('bem'))

if frase.find('bem') == -1:
    print('Não há a palavra bem na frase.')
else:
    print('Há a palavra tubarão na frase!')