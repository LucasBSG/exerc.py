renda = int(input('Quantos reais você recebe por mês? '))
print(renda)

limite = 0

if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 6000:
    limite = 3000
elif renda < 8000:
    limite = 4000
elif renda < 10000:
    limite = 5000
elif renda > 10000:
    print('Consulte o gerente do banco para mais informações.')
    limite = 7000

print('Parabéns, seu cartão foi aprovado com um limite de R$%d.' % limite)