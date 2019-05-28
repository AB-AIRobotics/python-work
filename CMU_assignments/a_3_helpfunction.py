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

    sample_list = [12,3,-2,5,1,24,7,15,3,9,5,-13]
    sample_rows = 3
    sample_columns = 4
    numlistelements = len(sample_list)
    matrix = []
    for i in range(sample_rows):
        row = []
        for l in range(sample_columns):
            row.append(sample_list[l+i])
        matrix.append(row)
    print matrix

listToMat(1,1,1)