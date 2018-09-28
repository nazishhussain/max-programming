#program for snake and ladder game
import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
		n=input("press r to roll a dice")
		if (n=='r'):
			r=myroll()
			count=count+r
			print("u got ",count)
			if(count==2):
				count=37
				print("i got the ladder")
			elif(count==11):
				count=2
				print("sorry , u got snake")
			elif(count==8):
				count=47
				print("i got the ladder")
			elif(count==25):
				count=5
				print("sorry , u got snake")
			elif(count==40):
				count=68
				print("i got the ladder")
			elif(count==38):
				count=9
				print("sorry , u got snake")
			elif(count==52):
				count=81
				print("i got the ladder")
			elif(count==65):
				count=46
				print("sorry , u got snake")
			elif(count==76):
				count=97
				print("i got the ladder")
			elif(count==89):
				count=70
				print("sorry , u got snake")
			
			elif(count==93):
				count=64
				print("sorry , u got snake")
			elif(count==2):
				count=37
				print("i got the ladder")
			elif(count==11):
				count=2
				print("sorry , u got snake")
			elif(count==2):
				count=37
				print("i got the ladder")
			elif(count==11):
				count=2
				print("sorry , u got snake")
			elif(count==2):
				count=37
				print("i got the ladder")
			elif(count==11):
				count=2
				print("sorry , u got snake")

			elif(count==100):
				print("you won the game")
				break
			elif(count>=100):
				count=count-r
				print("dice cant go back")