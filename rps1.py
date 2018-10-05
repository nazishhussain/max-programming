import random
	
s1=0
s2=0
print("Hello! Welcome to the Rock Paper Scissors Program!")
	

boss = False
	
while boss == False:
	    print("")
	    print("Press 1 for Rock.")
	    print("Press 2 for Paper.")
	    print("Press 3 for Scissors.")
	

	    UserInput = int(input("What would you like to play? : "))
	    ComputerInput = random.randrange(1,3)
	

	    if (UserInput == 1) and (ComputerInput == 1):
	        boss = False
	        print("It's a draw; you both played Rock!")
	        
	        
	    if (UserInput == 2) and (ComputerInput == 1):
	        boss == True
	        s1=s1+1
	        print("you won ",s1,"times")
	        
	

	    if (UserInput == 3) and (ComputerInput == 1):
	        boss == True
	        s1=s1-1
	        print("You lose! The computer played Rock!",s1,"times")

	        
	    if (UserInput == 1) and (ComputerInput == 2):
	        boss = True
	        print("You lose! The computer played Paper!")
	        
	    if (UserInput == 2) and (ComputerInput == 2):
	        boss == False
	 
	        print("It's a draw; the computer played Paper!")
	

	    if (UserInput == 3) and (ComputerInput == 2):
	        boss == True
	        s1=s1+1
	        print("You win! The computer played Paper!",s1,"times")
	        
	    if (UserInput == 1) and (ComputerInput == 3):
	        boss = True
	        s1=s1+1
	        print("You win! The computer played Scissors!",s1,"times")
	        
	    if (UserInput == 2) and (ComputerInput == 3):
	        boss == True
	        s1=s1-1
	        print("You lose! The computer played Scissors!")
	        if (UserInput == 3) and (ComputerInput == 3):
	        	boss == False
	        print("It's a draw; the computer played Scissors!")
	    else:
	    	if(s1==3 or s2==3):
	    		if(s1==3):
	    			print("computer won")
	    		else:
	    			print("good job,you win")
	    			break
