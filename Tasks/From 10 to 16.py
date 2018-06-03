newInt = input ("Enter a decimal number: ")
newInt2 = int (newInt)
binStr = ""
while newInt2 > 0:
    binStr = str (newInt2 % 16) + binStr
    newInt2 = newInt2//16

print ("The hexadecimal number is: ", binStr)
