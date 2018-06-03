a=int(input("a:"))
b=[]
c=0
while a!=0:
    c=a%8
    b.append(c)
    a=a//8

for i in range (len(b)) :
    print(b[i],end = "")



