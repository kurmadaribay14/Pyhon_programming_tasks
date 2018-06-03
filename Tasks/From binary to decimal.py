#Name: Daribay Kurma
#Group: 1EN04B
#Problem: 4
kl=input ("Enter binary number: ")
l=str(kl)
p=len(l)
total=0
for i in range (0,p):
      dec=int(l[i])*(2**(p-(i+1)))
      total = total+dec
print (total)

