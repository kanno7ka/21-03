import math

print('')
print('ax^2 + bx + c = 0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = b ** 2 - 4 * a * c
print('discriminant D = ', discr)

if discr > 0:
   x1 = (-b + math.sqrt(discr)) / (2 * a)
   x2 = (-b - math.sqrt(discr)) / (2 * a)
   print('x1 = ', x1, 'x2 = ', x2)
elif discr == 0:
  x = -b / (2* a)
  print ('x = ', x)
else:
  print('no roots')