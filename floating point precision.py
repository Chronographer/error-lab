eps = 1.0
almostOne = 2.0
counter = 0
while almostOne != 1:
    eps = eps / 2.0
    almostOne = 1.0 + eps
    print("eps is: " + str(repr(eps)) + " almostOne is: " + str(repr(almostOne)))
    print("counter is: " + str(counter))
    counter = counter + 1
