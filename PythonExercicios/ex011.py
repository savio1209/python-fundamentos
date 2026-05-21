larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área de {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisa de {}l de tinta'.format(tinta))
