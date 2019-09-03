import math
import string

def sidesInOrder(side_1,side_2,side_3):
    """[summary]
    
    Parameters
    ----------
    side_1 : [type]
        [description]
    side_2 : [type]
        [description]
    side_3 : [type]
        [description]
    """
    global small_side
    global large_side
    global medium_side
    small_side = min(side_1, side_2, side_3)
    large_side = max(side_1, side_2, side_3)
    medium_side = (side_1 + side_2 + side_3) - small_side - large_side
    print "Sides in sorted order: ", small_side,medium_side, large_side
    return(small_side,medium_side,large_side)

def getDecDigit(digit):
    """[summary]
    
    Parameters
    ----------
    digit : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x
            
def convertToBase(number, conversion_base):
    """[summary]
    
    Parameters
    ----------
    number : [type]
        [description]
    conversion_base : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    converted_num = []
    if number > 0:
        while number > 0:
            converted_num.append(number % conversion_base)
            number = number / conversion_base
    converted_num.reverse()
    return converted_num
  
def convertToHexa(numlist):
    """[summary]
    
    Parameters
    ----------
    numlist : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    hexalist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex_out = []
    for i in range(len(numlist)):
        hex_out.append(hexalist[numlist[i]])
    return hex_out 

def listConversion(inputList):
    """[summary]
    
    Parameters
    ----------
    inputList : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    var = "".join(str(x) for x in inputList)  
    return var 

def listToMat(inlist, numrows, numcolumns):
    """[summary]
    
    Parameters
    ----------
    inlist : [type]
        [description]
    numrows : [type]
        [description]
    numcolumns : [type]
        [description]
    """
    totalelements = numrows * numcolumns
    numlistelements = len(inlist)
    if (totalelements == numlistelements):
        matrix = []
        for i in range(numrows):
            row = []
            for l in range(numcolumns):
                row.append(inlist[l+(numcolumns*i)])
            matrix.append(row)
        return matrix
    else:
        print "Given list does not have correct dimensions"


def tranposeMatrixZero(inputlist, numcolumns, numrows):
    zerolist = [0] * len(inputlist)
    tempmatrix = []
    for i in range(numcolumns):
        row = []
        for l in range(numrows):
            row.append(zerolist[l+(numrows*i)])
        tempmatrix.append(row)
    return tempmatrix

def evenOddCheck(integer):
    output = integer % 2
    if (output == 1):
        print "Given integer is Odd"
        return integer
    else:
        print "Given integer is Even"
        return integer

def preCollatz(integer):
    evenOdd = integer % 2
    if (evenOdd == 0):
        result = integer / 2
        return result
    else:
        result = 3*integer + 1
        return result