from math import radians, sin, cos, tan
an = float(input('digite o angulo que voce deseja: '))
sen = sin(radians(an))
print(f'o angulo de {an} tem o seno de  {sen:.2f}')
cos = cos(radians(an))
print(f'o angulo de {an} tem o cosseno de {cos:.2f}')
tan = tan(radians(an))
print(f'o angulo de {an} tem o tangente de {tan:.2f}')
