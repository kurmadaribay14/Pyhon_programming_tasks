def myFactorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

N=int(input("Enter N: "))
K=int(input("Enter K: "))
print myFactorial(N)/myFactorial(N-K)
    
