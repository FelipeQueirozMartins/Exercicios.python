from random import randint
pc = randint(0, 5)
print ('-=-' * 20)
print ('Vou pensar em um número de 0 à 5, tente adivinhar!!!')
print ('-=-' * 20)
ply = int(input('Qual número eu pensei? '))
if ply == pc:
    print ('PARABÉNS!, eu pensei no número {}'.format(ply))
else:
    print ('GANHEI!, eu pensei no número {} e não no {}'.format(pc, ply))
