saldo = 359.56
deposito = float(input('Digite o valor que você deseja depositar à sua conta: '))
saldo = saldo + deposito
print(deposito)
print(saldo)
print('Referente a sua última compra, será subtraído um valor de R$125,98 de sua conta bancário.')
fatura_cartao = 125.98
saldo = saldo - fatura_cartao
print(saldo)
print('O saldo restante é de R$%.2f.'% saldo)