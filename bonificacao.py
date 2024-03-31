anoAtual = int(input('em que ano estamos? '))
anoAdmissao = int(input('digite o ano da sua admissão: '))
salario = float(input('digite seu salário: '))

tempo = anoAtual - anoAdmissao

print('seu salário é de R${}'.format(salario))

if (tempo > 5):
    bonus = salario * 0.2
    novoSalario = salario + bonus
    print('você recebeu um bônus de 20%, ou seja, R${}'.format(bonus))
    print('salário final: R${}'.format(novoSalario))
else:
    bonus = salario * 0.1
    novoSalario = salario + bonus
    print('você recebeu um bônus de 10%, ou seja, R${}'.format(bonus))
    print('salário final: R${}'.format(novoSalario))