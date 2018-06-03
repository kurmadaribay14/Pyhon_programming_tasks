n=input()
def fact(n):
    if n==0:
        return 0
    else:
        print n
        return fact(n-1)
fact(n) 
