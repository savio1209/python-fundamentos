medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('{} metros equivale a {:.0f} centímetros e {:.0f} milímetros.'.format(medida, cm, mm))
