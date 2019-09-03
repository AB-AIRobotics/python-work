import math
import string
from a_3_helpfunction import*

def whichTriangle(side_1, side_2, side_3):
    """
    [summary]
    
    Parameters
    ----------
    side_1 : [type]
        [description]
    side_2 : [type]
        [description]
    side_3 : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """


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
    """[summary]
    
    Parameters
    ----------
    num : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    if '.' in float_num:
        print "The number enter is floating point number"
        return True
    else:
        print "The number is not a floating point number"
        return False



def toDecimal(number,base):
    """[summary]
    
    Parameters
    ----------
    number : [type]
        [description]
    base : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """

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
    """[summary]
    
    Parameters
    ----------
    number : [type]
        [description]
    num_base : [type]
        [description]
    conversion_base : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    
    if (num_base == 2 and conversion_base == 10):
        binary_decimal = toDecimal(number,num_base)
        return binary_decimal

    elif(num_base == 2 and conversion_base == 8):
        octal_decimal = toDecimal(number,num_base)
        numlist = convertToBase(octal_decimal, conversion_base)
        return numlist

    elif(num_base == 2 and conversion_base == 16):
        hex_decimal = toDecimal(number,num_base)
        numlist = convertToBase(hex_decimal,conversion_base)
        anslist = convertToHexa(numlist)
        return anslist 
        
    elif(num_base == 2 and conversion_base == 2):
        return number

    elif(num_base == 10 and conversion_base == 10):
        return num_base
    elif(num_base == 10 and conversion_base == 8):
        num = convertToBase(number , conversion_base)
        return num 
    elif (num_base == 10 and conversion_base == 16):
        num = convertToBase(number, conversion_base)
        anslist = convertToHexa(num)
        ans = listConversion(anslist)
        return ans

    elif (num_base == 10 and conversion_base == 2):
        num = convertToBase(number, conversion_base)
        ans = listConversion(num)
        return ans 

def collatz(integer):
    
    count = 0
    output = 0
    if (integer >= 1):
        while (output != 1):
            output = preCollatz(integer)
            count += 1
            integer = output 
        return count
    elif((integer < 1) or (integer == 0)):
        return -1
    

def transpose(inputlist, numrows, numcolumns):
    """[summary]
    
    Parameters
    ----------
    inputlist : [type]
        [description]
    numrows : [type]
        [description]
    numcolumns : [type]
        [description]
    """
    matrix = listToMat(inputlist,numrows,numcolumns)
    print "Original matrix: ",matrix
    zeromatrix = tranposeMatrixZero(inputlist,numcolumns,numrows)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            zeromatrix[j][i] = matrix[i][j]

    final_matrix = []
    for r in zeromatrix:
         final_matrix.append(r)

    output_list = []
    for x in final_matrix:
        for y in x:
            output_list.append(y)
    return output_list        
    
def nearestWords(wordlist, word):
    """[summary]
    
    Parameters
    ----------
    wordlist : [type]
        [description]
    word : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    for i in range(len(wordlist)):
        tempwordlist = []
        for i in word:
            tempwordlist.append(i)
        mainlist = []
        for i in range(len(wordlist)):
            temp = wordlist[i]
            temporiginallist = []
            for i in temp:
                temporiginallist.append(i)
            mainlist.append(temporiginallist)
            
    for matching_list in mainlist:
        score = 0
        index = 0
        for c in tempwordlist:
            min_dist = 10000
            temp_score = 0
            for y in range(len(matching_list)):
                mc = matching_list[y]
                distance = abs(index-y) + 0.01
                if c == mc and distance < min_dist:
                    temp_score = 1
                    min_dist = distance
            score += temp_score/(min_dist**2)
            index += 1
        
        print(matching_list)
        print(score)




    
    

# print nearestWords(templist,'as')

def solveCryptarithm(puzzle, solution):
    """[summary]
    
    Parameters
    ----------
    puzzle : [type]
        [description]
    solution : [type]
        [description]
    """
    pass 

def convertUnits(fromQuantity, fromUnits, toUnits, category):
    """[summary]
    
    Parameters
    ----------
    fromQuantity : [type]
        [description]
    fromUnits : [type]
        [description]
    toUnits : [type]
        [description]
    category : [type]
        [description]
    """
    
    pass 
