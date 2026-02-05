def fibosum(n):
    res = 0
    a,b = 0,1
    for i in range(n):
        a, b = b, a + b
        res += a
    return res

print('Sum of the first 5 terms of the Fibonacci series:',fibosum(5))
print('Sum of the first 10 terms of the Fibonacci series:',fibosum(10))
