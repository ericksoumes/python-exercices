valor = float(input('digite o valor final de sua compra: '))
print('1 - pagamento a vista com 5% de desconto')
print('2 - pagamento em 3x sem juros')
print('3 - pagamento em 5x com 2% de juros')
print('4 - pagamento em 10x com 8% de juros')
formaDePagamento = int(input('qual a forma de pagamento? '))
if(formaDePagamento == 1):
    final = valor - (valor * 0.05)
    print('valor a pagar: R${} a vista'.format(final))
elif (formaDePagamento == 2):
    final = valor / 3
    print('valor a pagar: 3x de R${}'.format(final))
elif (formaDePagamento == 3):
    final = (valor * 0.02 + valor) / 5
    print('valor a pagar: 5x de R${}'.format(final))
elif (formaDePagamento == 4):
    final = (valor * 0.08 + valor) / 10
    print('valor a pagar: 10x de R${}'.format(final))