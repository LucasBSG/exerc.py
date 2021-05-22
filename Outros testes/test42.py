dicionario = {
    'testando': 2,
    'nome': 'Lucas',
    'idade': 16
}

print(dicionario)

print('nome' in dicionario)
print('sobrenome' in dicionario)

if 'nome' in dicionario:
    print('O meu nome é %s' % dicionario['nome'])