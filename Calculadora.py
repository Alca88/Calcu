from tkinter import *

root=Tk()

myFrame=Frame(root)

myFrame.pack()

operation=""

screenReset=False

result=0

#------------------pantalla--------------#

numScreen=StringVar()

screen=Entry(myFrame, textvariable=numScreen)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(bg="black", fg="#03f943", justify="right")

#------------------pulsaciones teclado--------#

def numPress(num):

	global operation

	global screenReset

	if screenReset!=False:

		numScreen.set(num)

		screenReset=False

	else:

		numScreen.set(numScreen.get() + num)

#------------------ función suma -------------#

def plus(num):

	global operation

	global result

	global screenReset

	result+=int(num)

	operation="plus"

	screenReset=True

	numScreen.set(result)

#------------------ función resta -------------#

num1=0

countRest=0

def rest(num):

	global operation

	global result

	global num1

	global countRest

	global screenReset

	if countRest==0:

		num1=int(num)

		result=num1

	else:

		if countRest==1:

			result=num1-int(num)

		else:

			result=int(result)-int(num)	

		numScreen.set(result)

		result=numScreen.get()


	countRest=countRest+1

	operation="rest"

	screenReset=True

#-------------funcion multiplicacion---------------------

countMulti=0

def multiply(num):

	global operation

	global result

	global num1

	global countMulti

	global screenReset
	
	if countMulti==0:

		num1=int(num)
		
		result=num1

	else:

		if countMulti==1:

			result=num1*int(num)

		else:

			result=int(result)*int(num)	

		numScreen.set(result)
		
		result=numScreen.get()


	countMulti=countMulti+1

	operation="multiply"

	screenReset=True

#-----------------funcion division---------------------

countDiv=0

def divide(num):

	global operation

	global result

	global num1

	global countDiv

	global screenReset
	
	if countDiv==0:

		num1=float(num)
		
		result=num1

	else:

		if countDiv==1:

			result=num1/float(num)

		else:

			result=float(result)/float(num)	

		numScreen.set(result)
		
		result=numScreen.get()


	countDiv=countDiv+1

	operation="division"

	screenReset=True


#------------------ función el resultado -------------#

def the_result():

	global result

	global operation

	global countRest

	global countMulti

	global countDiv
	

	if operation=="plus":

		numScreen.set(result+int(numScreen.get()))

		result=0

	elif operation=="resta":

		numScreen.set(int(result)-int(numScreen.get()))

		result=0

		countRest=0

	elif operation=="multiply":

		numScreen.set(int(result)*int(numScreen.get()))

		result=0

		countMulti=0

	elif operation=="division":

		numScreen.set(int(result)/int(numScreen.get()))

		result=0

		countDiv=0




#------------------fila 1---------------#

button7=Button(myFrame, text="7", width=3, command=lambda:numPress("7"))
button7.grid(row=2, column=1)
button8=Button(myFrame, text="8", width=3, command=lambda:numPress("8"))
button8.grid(row=2, column=2)
button9=Button(myFrame, text="9", width=3, command=lambda:numPress("9"))
button9.grid(row=2, column=3)
buttonDiv=Button(myFrame, text="/", width=3, command=lambda:divide(numScreen.get()))
buttonDiv.grid(row=2, column=4)

#------------------fila 2---------------#

button4=Button(myFrame, text="4", width=3, command=lambda:numPress("4"))
button4.grid(row=3, column=1)
button5=Button(myFrame, text="5", width=3, command=lambda:numPress("5"))
button5.grid(row=3, column=2)
button6=Button(myFrame, text="6", width=3, command=lambda:numPress("6"))
button6.grid(row=3, column=3)
buttonMult=Button(myFrame, text="*", width=3, command=lambda:multiply(numScreen.get()))
buttonMult.grid(row=3, column=4)

#------------------fila 3---------------#

button1=Button(myFrame, text="1", width=3, command=lambda:numPress("1"))
button1.grid(row=4, column=1)
button2=Button(myFrame, text="2", width=3, command=lambda:numPress("2"))
button2.grid(row=4, column=2)
button3=Button(myFrame, text="3", width=3, command=lambda:numPress("3"))
button3.grid(row=4, column=3)
buttonRest=Button(myFrame, text="-", width=3, command=lambda:rest(numScreen.get()))
buttonRest.grid(row=4, column=4)


#------------------fila 4---------------#

button0=Button(myFrame, text="0", width=3, command=lambda:numPress("0"))
button0.grid(row=5, column=1)
buttonPoint=Button(myFrame, text=".", width=3, command=lambda:numPress("."))
buttonPoint.grid(row=5, column=2)
buttonEquals=Button(myFrame, text="=", width=3, command=lambda:the_result())
buttonEquals.grid(row=5, column=3)
buttonPlus=Button(myFrame, text="+", width=3, command=lambda:plus(numScreen.get()))
buttonPlus.grid(row=5, column=4)

root.mainloop()