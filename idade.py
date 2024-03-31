anoAtual = int(input('em que ano estamos? '))
anoNas = int(input('em que ano você nasceu? '))

idade = anoAtual - anoNas

print('você nasceu em {}, por isso tem {} anos'.format(anoNas, idade))

if (idade >= 18):
    print('você pode tirar a CNH')
else:
    print('você ainda não pode tirar CNH por ter menos de 18 anos')