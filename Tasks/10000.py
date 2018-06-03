def printNumber():
    a=int(input("Input the number less than 10000: "))
    for i in xrange (1,a+1):
        if i%2==0:
            print i
    for k in xrange (1,a+1):
        if k%2!=0:
            print k
printNumber()
