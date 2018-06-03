##Counting sort for numbers less than 100
n=input() #input
d=n.split() #splitting input numbers
for i in range(0,len(d)):
    d[i]=int(d[i]) #changing it from string to integer
sorted={} #new dictionary
for i in d:
    sorted [i]=sorted.get(i,0)+1 #increasing the count of i by 1
for i in range(0,100):
    for j in range(0,sorted.get(i,0)):
        print i, #in 3.4 print (i,end=" ") 
