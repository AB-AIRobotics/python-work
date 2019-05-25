import math
import string
digs = string.digits + string.ascii_letters
#print digs
'''
Helper functions
'''

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
            
def getOctDigit(digit):
    digits = ['0','1','2','3','4','5','6','7']
    for x in range(len(digits)):
        pass

def gethexanum(decimal_digit):
    hexalist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for x in range(len(digit)):
        pass
    


    
def whichTriangle(side_1, side_2, side_3):
    sidesInOrder(side_1,side_2,side_3)
    if small_side+medium_side<large_side or small_side+medium_side==large_side:
        print "Sides cannot be triangle"
        return 0

    elif small_side==medium_side==large_side:
        print "Equilateral triangle"
        return 3
    elif small_side**2+medium_side**2==large_side**2:
        print "Right triangle"
        return 1
    elif small_side!=medium_side!=large_side:
        print "Scalene Triangle"
        if small_side**2+medium_side**2<large_side**2:
            print "Obtuse angled scalene triangle"
            return 4
        elif small_side**2+medium_side**2>large_side**2:
            print "Acute angled scalene triangle"
            return 6
    elif small_side == medium_side or small_side == large_side or medium_side == large_side:
        print "Isoceles Triangle"
        if small_side**2+medium_side**2<large_side**2:
            print "Obtuse angled Isoceles triangle"
            return 5
        elif small_side**2+medium_side**2>large_side**2:
            print "Acute angled Isoceles triangle"
            return 7
   

def isFloat(num):
    if '.' in float_num:
        print "The number enter is floating point number"
        return True
    else:
        print "The number is not a floating point number"
        return False



def toDecimal(number,base):

    if (base == 2):
        tempList = map(int , str(number))
        tempList.reverse()
        index = len(tempList)
        decimal=0
        for i in range(index):
            decimal += ((2**i)*tempList[i])
        return decimal

    elif(base == 8):
        octList = map(int , str(number))
        octList.reverse()
        index = len(octList)
        octal = 0
        for i in range(index):
            octal+=((8**i)*octList[i])
        return octal

    elif(base == 16):
        hexdecimal = 0
        power = 0
        for digit in range(len(number),0,-1):
            hexdecimal += ((16**power)*getDecDigit(number[digit-1]))
            power+=1
        return hexdecimal
        
    elif(base == 10):
        return number

def convertBase(number, num_base, conversion_base):
    
    if (num_base == 2 and conversion_base == 10):
        binary_decimal = toDecimal(number,num_base)
        return binary_decimal

    elif(num_base == 2 and conversion_base == 8):
        octal_decimal = toDecimal(number,num_base)
        converted_num = []
        if octal_decimal > 0:
            while octal_decimal > 0:
                converted_num.append(octal_decimal % conversion_base)
                octal_decimal = octal_decimal / conversion_base
        converted_num.reverse()
        for i in converted_num:
            print converted_num[i]
        return converted_num

    elif(num_base == 2 and conversion_base == 16):
        hex_decimal = toDecimal(number,num_base)
        converted_num = []
        if hex_decimal > 0:
            while hex_decimal > 0:
                converted_num.append(hex_decimal % conversion_base)
                hex_decimal = hex_decimal / conversion_base
        converted_num.reverse()
        hexalist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        hex_out = []
        for i in range(len(converted_num)):
            hex_out.append(hexalist[converted_num[i]])
        return hex_out

    elif(num_base == 2 and conversion_base == 2):
        return number

    elif(num_base == 10 and conversion_base == 10):
        return num_base
    elif(num_base == 10 and conversion_base == 8):
        hex_decimal = toDecimal(number,num_base)
        converted_num = []
        if hex_decimal > 0:
            while hex_decimal > 0:
                converted_num.append(hex_decimal % conversion_base)
                hex_decimal = hex_decimal / conversion_base
        converted_num.reverse()
        return converted_num
