a=int(input("a:"))
b=[]
c=0
while a!=0:
    c=a%2
    b.append(c)
    a=a//2

for i in range (len(b)) :
    print(b[i], end="")
