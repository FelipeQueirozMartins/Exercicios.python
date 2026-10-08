ano = int(input('Qual ano deseja analisar? '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
s