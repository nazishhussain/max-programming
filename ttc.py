#tic tac toe

a = ['0','1','2','3','4','5','6','7','8','9','10']

#printing board
def print_board():
	print('\n************************\n')
	print(' *|||* '+ a[1] + ' *|||* ' + a[2] + ' *|||* ' + a[3] + ' *|||* ')
	print('\n*************************\n')
	print(' *|||* '+ a[4] + ' *|||* ' + a[5] + ' *|||* ' + a[6] + ' *|||* ')
	print('\n*************************\n ')
	print(' *|||* '+ a[7] + ' *|||* ' + a[8] + ' *|||* ' + a[9] + ' *|||* ')
	print('\n*************************\n')

#player 1 plays

p1=True
while(True):
	print_board()
	if p1:
		p=input("player 1, choose any empty space : ")
		if p in a:
			a[int(p)]= 'x'
			p1= not p1

#player 2 plays
	else:
		p=input("player 2, choose any empty space : ")
		if p in a:
			a[int(p)]= 'O'
			p1 = not p1

#rows
	for i in(1,4,7):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			print("game over ");
			print_board()
			exit()

#colum
	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			print("game over ");
			print_board()
			exit()

#diag l to r
	if(a[1]==a[3] and a[1]==a[7]):
		print("game over ");
		print_board()
		exit()

#diag r to l 
	if(a[1]==a[3] and a[1]==a[5]):
		print("game over ");
		print_board()
		exit()
	else:
		print("invalid position")

