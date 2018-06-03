def countDown(n):
    if n==0:
        print "Blastoff!"
    else:
        print n
        countDown(n-1)
