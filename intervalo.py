num = int(input('digite um número inteiro: '))
if (-100 <= num <= -1 or 1 <= num <= 100):
    print('o número está dentro dos parâmetros')

## outra forma de escrever --> if (num <= 100 and num >= -1 or num >= 1 and num <= 100):