print('Bem-vindo(a) ao conversor de moeda! \nA cotação de hoje é US$ 1.00 = R$ 3.27')
s = float(input('Qual o seu saldo? R$ '))
print(' ' * 12)
print('Seu saldo é de R${}'.format(s))
cot = s / 3.27
print('O equivalente em dólar é US${:.2f}'.format(cot))
