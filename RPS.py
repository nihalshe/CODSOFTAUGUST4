import random
import os
import time
def clear():
	os.system("clear")
def rps_instructions():
	print("***********")
	print("Instructions for Rock-Paper-Scissors : ")
	print("***********")
	print("Rock crushes Scissors")
	print("Scissors cuts Paper")
	print("Paper covers Rock")
	print("***********")
def rps():
	global rps_table
	global game_map
	global name
	while True:
		print("--------------------------------------")
		print("\t\tMenu")
		print("--------------------------------------")
		print("Enter \"help\" for instructions")
		print("Enter \"rock\",\"paper\",\"scissors\" to play")
		print("Enter \"exit\" to quit")
		print("--------------------------------------")
		print("***********")
		inp =input("Enter your move : ")
		if inp == "help":
			clear()
			rps_instructions()
			continue
		elif inp == "exit":
			clear()
			break	
		elif inp == "rock":
			player_move = 0
		elif inp == "paper":
			player_move = 1		
		elif inp == "scissors":
			player_move = 2
		else:
			clear()
			print("Wrong Input!!")
			rps_instructions()	
			continue
		print("Computer making a move....")
		print("***********")
		time.sleep(2)
		comp_move = random.randint(0, 2)
		print("Computer chooses ", game_map[comp_move].upper())
		winner = rps_table[player_move][comp_move]
		if winner == player_move:
			print(name, "WINS!!!")
		elif winner == comp_move:
			print("COMPUTER WINS!!!")
		else:
			print("TIE GAME")
		print("***********")
		time.sleep(2)
		clear()
if __name__ == '__main__':
	game_map = {0:"rock", 1:"paper", 2:"scissors"}
	rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]	
	name =input("Enter your name: ")
	while True:
		print("***********")
		print("Let's Play!!!")
		print("Enter 1 to play Rock-Paper-Scissors")
		print("Enter 2 to quit")
		print("***********")
		try:
			choice = int(input("Enter your choice = "))
		except ValueError:
			clear()
			print("Wrong Choice")	
			continue
		if choice == 1:
			rps()
		elif choice == 2:
			break
		else:
			clear()
			print("Wrong choice. Read instructions carefully.")