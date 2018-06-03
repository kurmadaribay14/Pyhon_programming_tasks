print ("Convert from binary to decimal: ")
dec=0
bin=0
factor=1

print ("Enter binary number: ")
bin = input ()
while (bin>0):
    if ((bin%10)==1):
        dec += factor
    bin /= 10
    factor = factor * 2

print ("The decimal number is: ", dec)
