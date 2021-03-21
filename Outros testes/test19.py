salario = int(input('Quanto você recebe por mês? '))

print('Hoje ele recebe R$%d por mês'% salario)

if (salario < 1000):
    salario_com_aumento = (salario * 0.10) + salario
    print('Menor Salario, Com o aumento ele virá a receber R$%d por mês'% salario_com_aumento)
elif (salario >= 1000 and salario <= 1299):
    salario_com_aumento = (salario * 0.05) + salario
    print('No salario medio, ele virá a receber R$%d por mês'% salario_com_aumento)
elif (salario > 1300 and salario <= 1500):
    salario_com_aumento = (salario * 0.03) + salario
    print('No maior salario, ele virá a receber R$%d por mês'% salario_com_aumento) 
else:
    print('Esse salario é maior do que o teto, logo ele não receberá aumento')