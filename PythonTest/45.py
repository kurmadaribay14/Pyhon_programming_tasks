a=['a','b','c']
b=a[:]
a[0]='d'
for i in b[::-1]:
    print i,
