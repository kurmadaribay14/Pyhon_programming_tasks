def kurma():
    a=input()
    if ord(a)>=65 and ord(a)<=90:
        print("symbol is capital letter")
    if ord(a)>=97 and ord(a)<=122:
        print("symbol is small letter")
    if ord(a)>=48 and ord(a)<=57:
        print("symbol is digit")
kurma()
