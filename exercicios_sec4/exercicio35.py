saque = int(input('Quanto você deseja sacar agora? '))

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0

while saque >= 100:
    nota_100 = nota_100 + 1
    saque = saque - 100
while saque >= 50:
    nota_50 = nota_50 + 1
    saque = saque - 50
while saque >= 20:
    nota_20 = nota_20 + 1
    saque = saque - 20
while saque >= 10:
    nota_10 = nota_10 + 1
    saque = saque - 10

print('Você vai receber %d notas de R$100, %d notas de R$50, %d notas de R$20 e %d notas de R$10.' % (nota_100,nota_50,nota_20,nota_10))