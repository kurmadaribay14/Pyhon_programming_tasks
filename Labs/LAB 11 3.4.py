def StripPunctuation(a):
    a = a.lower()
    for c in a:
        if c in '.,?!':
            a = a.strip(c)
    return a

'''def Reverse(s):
    answer=""
    for c in s:
        answer=c+answer
    return answer
    '''
def Palindrome(o):
    if o == o[::-1]:
        return True
    else:
        return False
    
F=open("file.txt","r")
w = {}
for line in F:
    for word in line.split():
        word = StripPunctuation(word)
        if Palindrome(word):
            w[word] = w.get(word,0)+1
for a, b in sorted(([b,a] for [a,b] in w.items()), reverse = True):
    print ("%s - %s"%(b,a))
