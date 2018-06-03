A=int(input('Input A: '))
B=int(input('Input B: '))
C=int(input('Input C: '))
if A<B and A<C:
    print(A)
elif A<B and A>C:
    print(C)
else:
    print(B)
