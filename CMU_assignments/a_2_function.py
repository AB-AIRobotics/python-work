import math


def populationEstimation(No, k ,t):
	x=k*t
	N=No*math.exp(x)
	print "Estimated population = ", N
	return N
	
#populationEstimation(1000,0.02,24)


def poolBalls(rows):
	x=range(rows+1)
	print x
	y=sum(x)
	print "Balls = ",y
	return y
	
#poolBalls(5)

def setKthDigit(n,k,d):
	print n
	x=(n // 10**k)%10
	print "Replace it",x
	print "With",d
	y=((n//10)*10)+d
	print y
	
	
#setKthDigit(468,0,5)
#setKthDigit(-468,0,5)

def distance(x1,y1,x2,y2):
	d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	print "length = ",d
	return d
#distance(1,1,5,8)

def triangleAreaFromSides(a,b,c):
	s = (a+b+c)/2.0
	a = math.sqrt(s*(s-a)*(s-b)*(s-c))
	print "Area",a
	return a
	
#triangleAreaFromSides(8,9,15)

def triangleAreaByCoordinates(x1,y1,x2,y2,x3,y3):
	x = distance(x1,y1,x2,y2)
	y = distance(x2,y2,x3,y3)
	z = distance(x3,y3,x1,y1)
	triangleAreaFromSides(x,y,z)
	
#triangleAreaByCoordinates(-5,1,6,-3,2,80)

def eulerPower(x):
	e= 1+x+(x**2/2)+(x**3/6)+(x**4/24)
	print e
	return e
	
#eulerPower(0.5)

def natLog(y):
	x=y-1
	a= x-(x**2/2)+(x**3/3)-(x**4/4)+(x**5/5)
	print a
	return a
	
#natLog(1.5)

raw_input("\n\nPress the enter key to exit.")