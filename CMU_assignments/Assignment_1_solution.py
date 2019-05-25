
from turtle import*

def drawLine(angle, length):
	left(angle)
	print "angle", angle
	forward(length)
	print "length", length
	return 

#drawLine(45, 50)


def drawStar(length):
	drawLine(80,length)
	drawLine(-160,length)
	drawLine(-140,length)
	drawLine(-140,length)
	drawLine(-130, length)
	
#drawStar(80)

def drawRectangle(x,y):
	drawLine(90,x)
	drawLine(90,y)
	drawLine(90,x)
	drawLine(90,y)
	

#drawRectangle(50,80)

def drawArch():
	drawLine(0,10)
	drawLine(90,30)
	circle(-10,180)
	drawLine(0,30)
	drawLine(90,10)
	drawLine(90,30)
	circle(20,180)
	drawLine(0,30)

#drawArch()

def drawMoon():
	circle(40,190)
	circle(35, -210)
	drawLine(-210,-18)

#drawMoon()
	
	
def drawPakistanFlag():
	fillcolor(0,0.5,0)
	begin_fill()
	drawRectangle(150,200)
	end_fill()
	#fillcolor('white')
	#begin_fill()
	#drawRectangle(150,50)
	#end_fill()
	penup()
	goto(-130,60)
	pendown()
	fillcolor('white')
	begin_fill()
	drawStar(30)
	end_fill()
	penup()
	goto(-160,100)
	pendown()
	fillcolor('white')
	begin_fill()
	drawMoon()
	end_fill()
	penup()
	goto(-200,0)
	pendown()
	fillcolor('white')
	begin_fill()
	drawRectangle(150,50)
	end_fill()
	
	

drawPakistanFlag()	


raw_input("\n\nPress the enter key to exit.")