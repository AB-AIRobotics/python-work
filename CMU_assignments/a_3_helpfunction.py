import math
import string

def sidesInOrder(side_1,side_2,side_3):
    global small_side
    global large_side
    global medium_side
    small_side = min(side_1, side_2, side_3)
    large_side = max(side_1, side_2, side_3)
    medium_side = (side_1 + side_2 + side_3) - small_side - large_side
    print "Sides in sorted order: ", small_side,medium_side, large_side
    return(small_side,medium_side,large_side)

def getDecDigit(digit):
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x
            
def convertToBase(number, conversion_base):
    converted_num = []
    if number > 0:
        while number > 0:
            converted_num.append(number % conversion_base)
            number = number / conversion_base
    converted_num.reverse()
    return converted_num
  
def convertToHexa(numlist):
    hexalist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex_out = []
    for i in range(len(numlist)):
        hex_out.append(hexalist[numlist[i]])
    return hex_out 

def listConversion(inputList):
    var = "".join(str(x) for x in inputList)  
    return var 

