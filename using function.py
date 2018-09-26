#using function

a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))

#addition
def add():
	c=a+b
	return c
print("total sum of a&b =",add())

#substraction
def sub():
	c=a-b
	return c
print("sum of a&b =",sub())

#multiplication
def mul():
	c=a*b
	return c
print("product of a&B =",mul())

#division
def div():
	c=a/b
	return c
print("remainder of a&b =",div())

