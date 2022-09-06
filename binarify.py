# Jeff Dickson
# Aug 2022

import sys

#get inputs from the launch arguments
#particularly we want an integer which we will convert to binary
inNum = sys.argv[1]
inNum = int(inNum)
print(inNum)

intSize = 8; #the bit representation of our integer, we will compare this to know params starting at 8 bit

if inNum < 0:
    print("Please input a positive number")
    exit()

if inNum > 255:
    while inNum > (2**(intSize-1)):
        intSize *= 2 #first pass convert intSize from 8 bit to 16 bit
        
    print("This is a " + str(intSize) + " bit integer")

i = intSize
while i > 0:
    currentBit = 2**(-1+i)
    #print(currentBit)
    if (currentBit > inNum):
        print("0", end='')
    else:
        inNum = inNum - currentBit
        print("1", end='')           
    i = i - 1
