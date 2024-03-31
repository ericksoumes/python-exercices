print('-----CALCULADORA------')
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - DIVISÃO')
print('4 - MULTIPLICAÇÃO')
operacao = int(input('qual operação deseja fazer? '))
num1 = float(input('digite um valor: '))
num2 = float(input('digite um segundo valor: '))
if (operacao == 1):
    resultado = num1 + num2
    print('a soma de {} com {} é igual a {}'.format(num1, num2, resultado))
elif (operacao == 2):
    resultado = num1 - num2
    print('a subtração de {} por {} é igual a {}'.format(num1, num2, resultado))
elif (operacao == 3):
    resultado = num1 / num2
    print('a divisão de {} por {} é igual a {}'.format(num1, num2, resultado))
elif (operacao == 4):
    resultado = num1 * num2
    print('a multiplicação de {} por {} é igual a {}'.format(num1, num2, resultado))