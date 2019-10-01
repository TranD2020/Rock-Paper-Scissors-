# Name
# Rock Paper Scissors
# rps6.py
# added comment for github
import random 
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

# Welcome Message
# Print a welcome message
print("Welcome to Rock Paper Scissors")
# prompt for name
pName = input("What is your name? ")

# Score Tracker
# Make a function
def printScore():

	# print score:
	print("Score: ")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score
	print("Computer Score: " + str(cScore))
# Show how many ties
	print("Ties: " + str(ties))

# Game Loop
# loop until q is entered
while True:
	# prompt for player move (r, p, s, q)
	pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to quit ")
# print the score
	printScore()
# check if q is entered if so end the game
	if pMove == 'q':
		break
# get a computer move (random)
	cMove = random.choice(cMoves)
# compare player move with the computer move
	# player picks rock
	if pMove == "r":
		print(pName + " picked Rock")
		if (cMove == "rock"):
			print("Computer picks Rock")
			print("Tie")
			ties += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else:
			print("Computer pciks Scissors")
			print("Rock breaks scissors")
			pScore += 1
# player picks paper
	elif pMove == "p":
		pass
# player picks scissors
	elif pMove == "s":
		pass
# check if pMove is valid
	else:
		print("That is not an option")