frase = 'frase teste para checar a ocorrência de determinada palavra nesse frase'

print(frase.count('frase'))     # count: vê quantas vezes determinada palavra aparece em uma string

if frase.count('frase') == 2:
    print('Definitivamente, essa palavra aparece duas vezes nessa oração')

print(frase.count('checar'))