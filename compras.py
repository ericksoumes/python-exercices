opcao = int(input('escola o que quer comprar: (1) MAÇA, (2) LARANJA ou (3) BANANA '))
quantidade = int(input('digite a quantidade que deseja comprar: '))

if (opcao == 1):
    preco = quantidade * 2.3
    print('{} maçã(s) custa(m) R${}'.format(quantidade, preco))
elif (opcao == 2):
    preco = quantidade * 3.6
    print('{} laranja(s) custa(m) R${}'.format(quantidade, preco))
elif(opcao == 3):
    preco = quantidade * 1.85
    print('{} banana(s) custa(m) R${}'.format(quantidade, preco))