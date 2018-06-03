a='Hello, world!'
b=""
for i in range(len(a)):
    b+=a[::-1][i]*2
print b

a=list(raw_input("Enter text: "))
a=a[::-1]
s=""
for i in a:
    s+=i*2
print s
