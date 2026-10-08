a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
maior = a

if b < menor:
    menor = b
if c < menor:
    menor = c

if b > maior:
    maior = b
if c > maior:
    maior = c  

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))