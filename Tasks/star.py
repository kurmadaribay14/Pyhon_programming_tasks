str = input('a: ')
nstr = ""

for str in range(5,10):    
    for i in str:
        if i=='m':
            nstr=nstr+'*'
        else:
            nstr=nstr+i
print (nstr)
