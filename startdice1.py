#write a program to print random numbers speciying r to roll and q to quit
import random
while True:
	x=input("enter 'r' to roll a dice and 'q' to quit")
	if(x=='r') :
		print(random.randint(1,6))
	elif(x=='q'):
		print("end the program")
		break
	else:
		print("write 'r' or 'q'")