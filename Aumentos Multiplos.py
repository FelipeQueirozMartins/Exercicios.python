aoud = str(input('Você deseja calcular o acréscimo ou o desconto do salário? [A / D]')).upper()
slb = float(input('Qual o valor do salário que deseja calcular? '))
pdc = float(input('Qual o valor da porcentagem que vai calcular? '))
if aoud == 'A':
    r1 = slb * (1 + pdc / 100)
    print ('O salário que antes valia R${} com o acréscimo agora vale R${:.2f}! '.format(slb, r1))
else: 
    r2 = slb * (1 - pdc / 100)
    print ('O salário que antes valia R${} com o desconto agora vale R${:.2f}! '.format(slb, r2))
