def printNumber() :
    a="0123456789"
    b="qwertyuiopasdfghjklzxcvbnm"
    c="QWERTYUIOPASDFGHJKLZXCVBNM"
    r=input()
    q=0
    w=0
    e=0
    for i in xrange (0,9):
        if r==a[i]:
            q=1
    if q==1:
        print "digit"
    for i in xrange (0,26) :
        if r==c[i]:
            w=1
    if w==1:
        print "capital letter"
    for i in xrange (0,26):
        if r==b[i]:
            e=1
    if e==1:
        print "small letter"
printNumber()
