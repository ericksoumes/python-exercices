##Crie uma variável de string que receba uma
##frase qualquer. Crie uma segunda variável,
##agora contendo a metade da string digitada.
##Imprima na tela somente os dois últimos
##caracteres da segunda variável do tipo string

palavra = input('escreva uma palavra: ')
tamanho = len(palavra)
metade = palavra[:tamanho//2]
print(metade[-2:])