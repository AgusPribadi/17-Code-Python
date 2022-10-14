#ax**2 + bx + c = 0

import cmath

a = int(input('Tulis A: '))
b = int(input('Tulis B: '))
c = int(input('Tulis C: '))

d = (b**2) - (4 * a * c)

x1 = (-b - cmath.sqrt(d)) / (2 * a)
x2 = (-b - cmath.sqrt(d)) / (2 * a)

print('Hasil Persamaaan Kuadrat adalah {0} dan {1}'.format(x1, x2))