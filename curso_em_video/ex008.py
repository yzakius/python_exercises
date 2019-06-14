metro = float(input('Digite o valor em metros: '))
dec = metro * 10
cent = metro * 100
mm = metro * 1000
dam = metro / 10
hm = metro / 100
km = metro / 1000
print('{} metros equivale a {} decímetros'.format(metro, dec))
print('{} metros equivale a {} centímetros'.format(metro, cent))
print('{} metros equivale a {} milímetros'.format(metro, mm))
print('{} metros equivale a {} decâmetros'.format(metro, dam))
print('{} metros equivale a {} hectômetros'.format(metro, hm))
print('{} metros equivale a {} kilômetros'.format(metro, km))
