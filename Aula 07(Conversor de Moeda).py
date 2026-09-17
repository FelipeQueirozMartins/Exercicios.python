R = float(input('Quantos reais você deseja converter? '))
US = R / 5.15
EU = R / 5.91
print('Com R${} você tera USD {:.2f} e EUR {:.2f}'.format(R, US, EU))
