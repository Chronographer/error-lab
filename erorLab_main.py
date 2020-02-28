import numpy as np
underFlow = 1.0
overFlow = 1.0
n = 10000.0
counter = 0
underFlowTime = -1  # the value for counter at which underFlow/overFlow actually under or over flowed.
overFlowTime = -1

while (counter < n):
    if underFlow == 0:
        underFlowTime = counter
        break
    else:
        underFlow = underFlow / 2
    counter = counter + 1
counter = 0
while counter < n:
    if overFlow == np.inf:
        overFlowTime = counter
        break
    else:
        overFlow = overFlow * 2
    counter = counter + 1

print("overflowed at: " + str(overFlowTime) + " underFlowed at: " + str(underFlowTime))
print("overflow value is: " + str(overFlow) + " underflow value is: " + str(underFlow))


