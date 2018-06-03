def BinaryToDecimal(aim) :
    aim = aim[::-1]
    dream = 0
    for i in range(len(aim)):
        dream += int (aim[i]) * (2 ** i)
    return (dream)

def OctalToDecimal(aim) :
    aim = aim[::-1]
    dream = 0
    for i in range(len(aim)) :
        dream += int (aim[i]) * (8 ** i)
    return (dream)

def HexdecimalToDecimal(aim) :
    aim = aim[::-1]
    dream = 0
    for i in range(len(aim)) :
        if ((aim[i]) == 'A') :
            dream += 10 * (16 ** i)
        elif ((aim[i]) == 'B') :
            dream += 11 * (16 ** i)
        elif ((aim[i]) == 'C') :
            dream += 12 * (16 ** i)
        elif ((aim[i]) == 'D') :
            dream += 13 * (16 ** i)
        elif ((aim[i]) == 'E') :
            dream += 14 * (16 ** i)
        elif ((aim[i]) == 'F') :
            dream += 15 * (16 ** i)
        else :
            dream += int (aim[i]) * (16 ** i)
    return (dream)    

def DecimalToBinary(aim) :
    result = []
    dream = int(aim)
    while (dream != 0) :
        result.append(dream % 2)
        dream //= 2
    result = result[::-1]
    return (result)

def DecimalToOctal(aim) :
    result = []
    dream = int(aim)
    while (dream != 0) :
        result.append(dream % 8)
        dream //= 8
    result = result[::-1]
    return (result)

def DecimalToHexdecimal(aim) :
    result = []
    dream = int(aim)
    while (dream != 0) :
        if (dream % 16 == 10) :
            result.append('A')
        elif (dream % 16 == 11) :
            result.append('B')
        elif (dream % 16 == 12) :
            result.append('C')
        elif (dream % 16 == 13) :
            result.append('D')
        elif (dream % 16 == 14) :
            result.append('E')
        elif (dream % 16 == 15) :
            result.append('F')
        else :
            result.append(dream % 16)
        dream //= 16    
    result = result[::-1]
    return (result)                                              

S = input("Please, enter the numeral system: ")
N = input("Please, enter the number: ")

if (S == "Binary") :
    a = BinaryToDecimal(N)
    aim = DecimalToOctal(a)
    print ("The octal value is: ", end="") 
    for i in aim :
        print (i, end="") 
    print ()
    print ("The decimal value is: "+str(a))
    print ("The hexdecimal value is: ", end="")
    aim = DecimalToHexdecimal(a)
    for i in aim :
        print (i, end="")  
    print ()
if (S == "Octal") :
    a = OctalToDecimal(N)
    print ("The binary value is: ", end="")
    aim = DecimalToBinary(a)
    for i in (aim) :
        print (i, end="") 
    print ()
    print ("The decimal value is: "+str(a))
    print ("The hexdecimal value is: ", end="")
    aim = DecimalToHexdecimal(a)
    for i in (aim) :
        print (i, end="") 
    print ()
if (S == "Decimal") :
    print ("The binary value is: ", end="")
    aim = DecimalToBinary(N)
    for i in aim :
        print (i, end="") 
    print()     
    print ("The octal value is: ", end="")
    aim = DecimalToOctal(N)
    for i in aim :
        print (i, end="") 
    print()   
    print ("The hexdecimal value is: ", end="")
    aim = DecimalToHexdecimal(N)
    for i in aim :
        print (i, end="")  
    print()   
if (S == "Hexdecimal") :
    a = HexdecimalToDecimal(N)
    print ("The binary value is: ", end="")
    aim = DecimalToBinary(a)
    for i in aim :
        print (i, end="")  
    print ()   
    print ("The octal value is: ", end="")
    aim = DecimalToOctal(a)
    for i in aim :
        print (i, end="") 
    print ()
    print ("The decimal value is: "+str(a))
    
