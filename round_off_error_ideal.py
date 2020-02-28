import matplotlib.pyplot as plt
import numpy as np
import math
x = 1.0
n = 0
sn = 1.0
exponent = sn
fraction = np.abs(sn/exponent)
epsilon = 0.00000000000000000000000000001
errorList = []
nList = []

while fraction > epsilon:
    #print("fraction is: " + str(repr(fraction)))
    n = n + 1.0
    sn = sn * x / n
    exponent = exponent + sn
    nList.append(n)
    absError = np.abs((exponent - math.exp(x))/math.exp(x))
    errorList.append(absError)
    if exponent != 0:
        fraction = np.abs(sn/exponent)

print("n is: " + str(n))
print("format:\ncalculated exponent value\nmath library exponent value\nabsolute error")
print(exponent)
print(math.exp(x))
print(absError)
plotLabel = "x = " + str(x)
plt.plot(nList, errorList, label=plotLabel)
plt.grid()
plt.legend()
plt.xlabel("n")
plt.ylabel("absolute relative error")
plt.suptitle("Absolute relative error between\nmath library and manual calculation of exponential")
#plt.yscale('log')
#plt.xscale('log')

plt.show()
