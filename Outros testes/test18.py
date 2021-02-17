iogurte = input('Quanto está custando? ')

print(iogurte)

preco_sem_imposto = float(iogurte)

imposto = preco_sem_imposto * 0.30

preco_final = imposto + preco_sem_imposto

print(preco_final)

mais_3 = input('Você quer mais 3 iogurtes? ')

if (mais_3) == 'sim' or 'por favor':
    print('Então dará 18.20 reais' % mais_3)