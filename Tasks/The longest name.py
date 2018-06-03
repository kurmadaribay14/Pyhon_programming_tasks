a=str(input ("name 1: "))
b=str(input ("name 2: "))
c=str(input ("name 3: "))
d=len(a)
e=len(b)
f=len(c)
if d>e and d>f:
    print "the longest name-"+a
if d>e and e>f:
    print "the longest name-"+b
if f>e and d>f:
    print "the longest name-"+c
