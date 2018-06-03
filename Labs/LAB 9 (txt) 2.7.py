inp = open ("aim.txt", "r")
s = inp.readline ()
def Month(s):
    if (s=="January"):
        return "01"
    elif (s=="February"):
        return "02"
    elif (s=="March"):
        return "03"
    elif (s=="April"):
        return "04"
    elif (s=="May"):
        return "05"
    elif (s=="June"):
        return "06"
    elif (s=="July"):
        return "07"
    elif (s=="August"):
        return "08"
    elif (s=="September"):
        return "09"
    elif (s=="October"):
        return "10"
    elif (s=="November"):
        return "11"
    elif (s=="December"):
        return "12"
def withOf(a):
    m = Month(a[-1])
    d = a[-3][:-2]
    if(len(d)<2): d="0"+d
    go=""
    for i in a:
        if i=="on":break 
        go = go +i+" "
    st = str(d)+"."+str(m)+": "+str(go)
    return [m,d,st]
def withOutOf(a):
    m = a[-1][3:]
    d = a[-1][:-3]
    if (len(d)<2):d="0"+d
    go=""
    for i in a:
        if i=="on":break
        go = go + i+" "
    st = str(d)+"."+str(m)+": "+str(go)
    return [m,d,st]
def sort(a):
    exchange = True
    while (exchange):
        exchange = False
        for i in xrange (len(a)-1):
            if(int(a[i][0])>int(a[i+1][0])):
                exchange = True
                a[i],a[i+1]=a[i+1],a[i]
            elif(int(a[i][0])==int(a[i+1][0])):
                exchange = True
                a[i],a[i+1]=a[i+1],a[i]
    return a
life=[]
while(s!="the end"):
    me = s.split()
    if "of" in me:
        life.append(withOf(me))
    else:
        life.append(withOutOf(me))
    s=inp.readline()
a=sort(life)
for i in a:
    print i[2]

        
