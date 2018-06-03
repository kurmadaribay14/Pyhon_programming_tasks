newInt = input ("Enter a decimal number: ")
newInt2 = int (newInt)
binStr = ""
while newInt2 > 0:
    binStr = str (newInt2 % 8) + binStr
    newInt2 = newInt2//8

print ("The octal number is: ", binStr)

newInt = input ("Enter a octal number: ")
temp = newInt
power = 0
number = 0

while len(temp) > 0:
    bit = int (temp[-1])
    number = number + bit*8**power
    power += 1
    temp = temp[:-1]

print ("The decimal number is: ", number)

newInt = input ("Enter a decimal number: ")
newInt2 = int (newInt)
binStr = ""
while newInt2 > 0:
    binStr = str (newInt2 % 2) + binStr
    newInt2 = newInt2//2

print ("The binary number is: ", binStr)

newInt = input ("Enter a binary number: ")
temp = newInt
power = 0
number = 0

while len(temp) > 0:
    bit = int (temp[-1])
    number = number + bit*2**power
    power += 1
    temp = temp[:-1]

print ("The decimal number is: ", number)

a=int(input("Enter a decimal number: "))
def ChangeHex(n):
    x = (n % 16)
    c = ""
    if (x < 10):
        c = x
    if (x == 10):
        c = "A"
    if (x == 11):
        c = "B"
    if (x == 12):
        c = "C"
    if (x == 13):
        c = "D"
    if (x == 14):
        c = "E"
    if (x == 15):
        c = "F"

    if (n - x != 0):
        return ChangeHex(n // 16) + str(c)
    else:
        return str(c)

print ("The hexadecimal number is:", ChangeHex(a))

