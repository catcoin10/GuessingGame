# Ghostbusting algorithm
from random import randint # use random data
print("Ghost game")
feeling_brave = True # default setting
score = 0 # nothing scored yet, coders count from 0
while feeling_brave:
	ghost_door = randint(1, 3)
	print("Three doors ahead...")
	print("There is a ghost in only one.")
	print("Which door do you open?")
	door = input("1, 2, or 3? ")
	door_num = int(door)
	if door_num == ghost_door:
		print("Ghost!")
		feeling_brave = False
	else:
		print("No ghost. Safe!")
		print("You enter the next room.")
		score = score + 1
print("Run away!")
print("GAME OVER! You scored", score)
