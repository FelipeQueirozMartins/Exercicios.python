vc = float(input('Qual a velocidade do carro? '))
if (vc < 80):
    print ('Você está dentro do limite de velocidade! Dirija com cuidado e tenha um ótimo dia!!!!')
else:
    m = vc - 80
    vm = m * 7.0
    vt = vm + vc
    print ("""VOCÊ EXCEDEU O LIMITE DE VELOCIDADE!!!)
    SUA MULTA É DE R${}!!!""".format(vt))
