f=open("input.txt", "r")
print "#"*24
while True:
    a=f.read(20)
    if a=='': break
    a=a.replace("/n", " ")
    a=a+" "*(20-len(a))
    print "#",a,"#"
print "#"*24
print "Good Bye"
