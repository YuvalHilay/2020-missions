
from math import sqrt,pow
#fibs
place = int(input("which fib element do you want? >"))
num = 0
for num in range(place+1):
    fib = ((pow((1 + sqrt(5)), num) - pow(1 - sqrt(5), num)) / ((pow(2, num) * sqrt(5))))
print(int(fib))