co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}!'.format(hi))
