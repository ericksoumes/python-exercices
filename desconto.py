print('--- CALCULA DESCONTO ---')
valor = float(input('digite o valor do produto: '))
porcentagem = float(input('digite o valor da porcentagem %: '))

desconto = valor * porcentagem / 100
final = valor - desconto

print('seu produto custa R${:.2f}, mas com {}% de desconto, que representa R${:.2f}  ele passa a ser R${:.2f}'.format(valor, porcentagem, desconto, final))