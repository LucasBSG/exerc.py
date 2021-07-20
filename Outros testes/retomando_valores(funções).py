def saudacao(nome):
    return 'Oi %s, como você vai?' % nome   #Quando se usa a função return o valor não é exibido diretamente na tela

sds = saudacao('Lucas')

print(sds + ' Você está bem?')    #Para o valor ser exibido, é necessário um comando de 'print'

def exponenciacao(a, b):
    return a ** b

def multiplicacao(a, b):
    return a * b

exp = exponenciacao(10, 2)
mul = multiplicacao(4, 32)

print(exp)

print(exp * 8)

print(exp + mul)

def profissao(nome):

    p = ''

    if nome == 'Lucas':
        p = 'Estudante'
    else:
        p = 'Não identificado'

    return p

prof = profissao('Kléber')

print(prof)

prof_l = profissao('Lucas')

print(prof_l)