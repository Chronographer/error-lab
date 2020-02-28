x = 10.0
N = 100.0

n = 0
sn = 1
exponent = sn

while n < N:
    n = n + 1
    sn = sn * x / n
    exponent = exponent + sn
    print(exponent)
print(exponent)

