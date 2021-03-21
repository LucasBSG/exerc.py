poupanca = 13125.21

saque = int(input('Quanto você deseja sacar? '))

if saque <= poupanca:
    print('Você sacou %d reais.' % saque)
else:
    print('Você não tem saldo para sacar %d reais.' % saque)
    print('Sua poupança tem no momento %.2f reais.' % poupanca)