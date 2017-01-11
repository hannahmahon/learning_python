# Example Function
def exampleFunction():
	print("hi")

#exampleFunction()

def anotherFunction():
	exampleFunction()

#anotherFunction()

# No optional parameters
def yetAnotherFunction(num1, fastAndLoose):
	if type(num1) == int: 
		print("you have a number. yay types")

	elif fastAndLoose:
		print("anything goes")

	#else:
		#print("You suck at entering parameters")

#yetAnotherFunction("1", True)

"""
Exercise 3  

Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

>>> right_justify('allen')
"""

def right_justify(stringVar):
	length = len(stringVar)
	extra_space = 70 - int(length)
	print((" "*extra_space) + stringVar)

# right_justify("allen")








