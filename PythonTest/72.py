def func(a):
    if len(a)==0:
        return
    return a+func(a[:len(a)-2])
print "Hello"
