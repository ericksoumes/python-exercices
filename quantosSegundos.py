print('descobrir quantos segundos')
d = int(input('quantos dias?: '))
h = int(input('quantas horas?: '))
m = int(input('quantos minutos?: '))
s = int(input('quantos segundos?: '))

res = (d * 86400) + (h * 3600) + (m * 60) + s

print('{} dias, {} horas, {} minutos e {} segundos são exatamente {} segundos'.format(d, h, m, s, res))