escala_imc = {
    'map': 'Muito abaixo do peso',
    'ap': 'Abaixo do peso',
    'pi': 'Peso ideal',
    'ac': 'Acima do peso',
    'o1': 'Obesidade 1',
    'o2': 'Obesidade 2',
    'o3': 'Obesidade 3',
}

def calcular_imc(peso_kg: float, 
                altura_m: float) -> tuple[float, str]:

    imc = peso_kg / altura_m ** 2
 
    if imc < 17:
        situacao = 'Map'
    elif imc < 18.5:
        situacao = 'Ap'
    elif imc < 25:
        situacao = 'Pi'
    elif imc < 30:
        situacao = 'Ap'
    elif imc < 35:
        situacao = 'O1'
    elif imc < 40:
        situacao = 'O2'
    else:
        situacao = 'O3'

    saida = (imc, situacao)
    return saida


def main():
    try:
        peso = input('Digite quantos quilos você pesa: ')
        peso = float(peso)
        altura = float(input('Digite sua altura: '))

    except ValueError:
        print('Valor inviável') #Caso o valor inserido não for um float, o código será finalizado.
        return

    resultado = calcular_imc(peso, altura)
    # imc = resultado[0]
    # referencia = resultado[1]
    (imc, referencia) = resultado

    situacao = escala_imc[referencia]

    print('O seu imc é', imc)
    print('A situação é de', situacao)

main()