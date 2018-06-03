def printNumber (a):
    for i in xrange (1,a):
        if (i%2==0) :
            print (i)
    for i in xrange (1,a):
        if (i%2==1) :
            print (i)

a = int(input())
printNumber (a)
