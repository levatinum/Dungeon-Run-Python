import random
import json

room = {
	"sequence": roomNumber,
	"xCoordinate": xCoordinate,
	"yCoordinate": yCoordinate,
	"roomType": roomType,
	"entryDoor": oldDoor,
	"exitDoor": newDoor,
	"description": description,
}

#roomType refers to a key in another file that defines what kinds of monsters can spawn there, and what kinds of treasure can spawn there
#squence determines the order that rooms were generated in. Sequence 1 is always at (0,0).
#x and yCoordinate explain where on a map different rooms are, and which doors connect to which rooms.
#entryDoor is the direction that the previous room is in.
#exitDoor is the direction that the next room is in.

print("How many rooms should we generate?")
numRooms = input()
numRooms = numRooms.int()

dungeonSet = {
	
}

roomNumber = 0

while numRooms >= 0:
	roomNumber = roomNumber + 1

	if roomNumber == 1:
		xCoordinate = 0
		yCoordinate = 0
		roomType = 0
		oldDoor = "South"
		newDoor = "North"
		description = "This is the entrance room to the dungeon. There is a door ahead of you."
	else