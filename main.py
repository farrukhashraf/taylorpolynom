import math as m
import numpy as l
def sin(x, n=10):
 sine = 0
 for i in range (0, n ,1):
   sign = ((-1)**(i+1))
   y = x%3.14159265359
   sine = sine+(((y**(2.0*i+1))/m.factorial(2*i+1))*sign)
 return sine
 
 
x = float(input('Enter the value of x:'))


print(m.sin(x))
print(sin(x, 10))

def cos (x, n=10):
  cosine = 0
  for i in range (0, n, 1):
    sign=((-1)**(i+1))
    y = x%3.14159265359
    cosine = (cosine+(((y**(2*i+0))/m.factorial(2*i+0))*sign))
  return cosine
  
x  = float(input('Enter the value of x :'))

print(m.cos(x))
print(cos(x, 10))


def ln(x, n=1):
  loge = 0
  for i in range (1, 1000, 1):
    y =x
    loge = loge+((((-1)**(i-1))*((y-(m.exp(0)))**i))/(i))

  return loge

x = float(input('Enter the value of x:'))

print(l.log(x))
print(ln(x, 1))
