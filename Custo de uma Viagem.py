km = float(input('Qual a distancia em km da sua viagem? '))
print ('Você esta prestes a começar uma viagem de {}km'.format(km))
if km > 200:
    r1 = km * 0.45
    print ('E o preço da sua viagem sera de R${}'.format(r1))
else:
    r2 = km * 0.50
    print ('E o preço da sua viagem sera de R${}'.format(r2))
