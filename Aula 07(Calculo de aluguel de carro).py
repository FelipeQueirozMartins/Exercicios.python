D = int(input('Quantos dias o carro foi alugado? '))
K = float(input('Quantos KMs o veiculo percorreu? '))
PD = D * 60 
PK = K * 0.15
S = PK + PD
print('O total a pagar é de R${:.2f}'.format(S))
