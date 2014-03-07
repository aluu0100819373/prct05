n=int(raw_input('Valor de n: '))
sumatorio=0.0
for i in range(1,n+1):
  x=(i-0.5)/float(n)
  print x
  b=i/float(n)
  a=(i-1)/float(n)
  fx=4.0/(1+x**2)
  print 'Subintervalos[%.3f  %.3f] x_i:%.3f fx_i:%.3f' % (a, b, x,fx)
  sumatorio=sumatorio+fx
p=(sumatorio/n)
print 'El valor aproximado de pi con 35 decimales es:%.35f' % p
from math import pi
print 'El valor de pi es: %.35f' % pi
