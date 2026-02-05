def fibon(n):
    a, b = 0,1
    for n in range(n):
        a, b = b, a + b
    return a

print('5th Fibonacci term:' , fibon(5))
print('10th Fibonacci term:' , fibon(10))
print('15th Fibonacci term:' , fibon(15))