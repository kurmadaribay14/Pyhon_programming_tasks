b = {}
a = {}
while True:
    c = list(map(str,input().split(":")))
    if c[0]=="end":
        break
    elif c[0] in b:
        a[c[0]]+=1
        b[c[0]][a[c[0]]]=c[1]
    else:
        b[c[0]]={}
        b[c[0]][1]=c[1]
        a[c[0]]=1

h=input().split()
for i in b.keys():
    for k in b[i]:
        if h[0] in i:
            print (b[i][k])
        
