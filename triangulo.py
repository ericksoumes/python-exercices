lado1 = float(input('digite o primero lado '))
lado2 = float(input('digite o segundo lado '))
lado3 = float(input('digite o terceiro lado '))

if (lado1 == 0 or lado2 == 0 or lado3 == 0):
    print('um dos lados tem o valor 0, por isso não é um triângulo')
elif((lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado1 + lado3) < lado2):
    print('não é um triângulo, pois um dos lados é maior que a soma dos outros dois')
elif(lado1 == lado2 == lado3):
    print('este é um triângulo EQUILÁTERO')
elif(lado1 == lado2 or lado3 == lado1 or lado2 == lado3):
    print('este é um triângulo ISÓSCELES')
else:
    print('este é um triângulo ESCALENO')