nomes = ['Lucas', 'Robson']
nomes.append('Carlos')

nomes2 = []
nomes2.append('Leandro')
nomes2.append('Jean')
nomes2.append('Douglas')

nomes3 = nomes2
nomes.clear()
nomes2.append('Thiago')
print(nomes)
print(nomes2)
print(nomes3)