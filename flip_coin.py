import turtle as tu
import random as ra

global numOfPlayers
global playerList
playerList = ["None", "None", "None", "None", "None"]

def welcome():
	print('''\
	Welcome to the Coin Flip Game\n\
	-----------------------------\n\
	Description:\n\
	\t* First you enter how many players are playing up to 5\n\
	\t* Then you enter the names of those players\n\
	\t* Then the computer will choose who drives. by:\n\
	\t\t~Flipping one coin for each player\n\
	\t\t~The last person to flip a heads is chosen\n\
	\t\t~If there's a tie, the computer reflips for the people who tied\n\
	\t* Then the computer will choose who pays the same way\n\
	''')

	void = input("\t--Press Enter--")


def playerCount():
	mNumOfPlayers = input("\nEnter the number of players in an integer form : ")
	print(f"                                        You have {mNumOfPlayers} players")

	try:
		mNumOfPlayers = int(mNumOfPlayers)
	except ValueError:
		print("Please Enter a Number!!")
		mNumOfPlayers = 0

	if mNumOfPlayers < 1:
		print("Not enough Players!!\n")
		playerCount()
	elif mNumOfPlayers > 5:
		print("Too many Players!!\n")
		playerCount()
	else:
		global numOfPlayers
		numOfPlayers = mNumOfPlayers


def playerNames(mNumOfPlayers = 1):
	for x in range(mNumOfPlayers):
		playerList[x] = input(f"Enter Name for Player {x+1} : ")
	
	print(f"Player names are: P1({playerList[0]}); P2({playerList[1]}); P3({playerList[2]}); P4({playerList[3]}); P5({playerList[4]})")
	
	
def main():
	welcome()
	playerCount()
	playerNames(numOfPlayers)


if __name__ == '__main__':
	main()