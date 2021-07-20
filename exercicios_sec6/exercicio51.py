a = 13
b = 8
c = 11

def maior_que_dez(num):
    
    resultado = ''

    if num > 10:
        resultado = 'Maior que 10'
    elif num < 10:
        resultado = 'Menor que 10'
    else:
        resultado = 'Igual a 10'

    return resultado

res_um = maior_que_dez(a)

print(res_um)

res_dois = maior_que_dez(b)

print(res_dois)

res_tres = maior_que_dez(c)