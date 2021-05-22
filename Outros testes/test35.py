l = ['Sofá','Televisão','Rádio','Ac','Poltrona'] #lista

i = 0 #elemento para rodar o código

item_procurado = input('O que deseja buscar na casa? ')
achou = False

while i < len(l):
    if l[i] == item_procurado:
        print('Encontramos um %s!' % item_procurado)
        achou = True
    i = i + 1

if achou == False:
    print('Não encontramos o objeto %s' % item_procurado)