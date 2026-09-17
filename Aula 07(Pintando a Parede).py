L = float(input('Qual a largura da sua parede em metros? '))
A = float(input('Qual a altura da sua parede em metros?'))
AR = L * A 
P = AR / 2
print('Sua parede tem a dimensão de {}x{} e sua área de {:.3f}m².'.format(L, A, AR))
print('Considerando que você gaste aproximadamente 1l a cada 2m², para pintar sua parede, você precisará de {:.1f}L de tinta'.format(P))
