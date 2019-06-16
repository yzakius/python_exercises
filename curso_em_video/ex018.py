from math import sin,cos,tan,radians

ang = float(input('Digite um ângulo: '))

print('O seno do ângulo {} é {:.5f}'.format(ang, sin(radians(ang))))
print('O cosseno do ângulo {} é {:.5f}'.format(ang, cos(radians(ang))))
print('A tangente do ângulo {} é {:.5f}'.format(ang, tan(radians(ang))))

