#Selection sort
def sort (d):
    for i in range (len(d)-1,0,-1):
        pmax=0
        for l in range(1,i+1):
            if d[1]>d[pmax]:
                pmax = 1

        temp = d[i]
        d[i] = d[pmax]
        d[pmax] = temp

n=input() #input
d=n.split() #splitting our input
for i in range(0,len(d)): 
    d[i]=int(d[i]) #changing type of array d from str to int
sort(d) #our algorithm
for i in range(0,len(d)):
    print d[i], #in 3.4 (d[i],end=' ')
