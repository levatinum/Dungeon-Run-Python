import random
import json
import random

def coordinateCreator(newDirection, xCoordinate, yCoordinate):
	coordinateResult = {
		"xCoordinate": xCoordinate,
		"yCoordinate": yCoordinate,
	}
	if newDirection == "North":
		yCoordinate = yCoordinate + 1
		coordinateResult["yCoordinate"] = yCoordinate
	elif newDirection == "West":
		xCoordinate = xCoordinate - 1
		coordinateResult["xCoordinate"] = xCoordinate
	elif newDirection == "East":
		xCoordinate = xCoordinate + 1
		coordinateResult["xCoordinate"] = xCoordinate
	return coordinateResult

def dungeonDoorDecider(prevNewDoor):
	directions = ["North", "West", "East"]
	if prevNewDoor == "South":
		newDirection = random.choice(directions)
	else:
		directions.remove(prevNewDoor)
		newDirection = random.choice(directions)
	return newDirection

def directionReverser(direction):
	if direction == "North":
		output = "South"
	elif direction == "South":
		output = "North"
	elif direction == "West":
		output = "East"
	else:
		output = "West"
	return output
#room = {
#	"sequence": roomNumber,
#	"xCoordinate": xCoordinate,
#	"yCoordinate": yCoordinate,
#	"roomType": roomType,
#	"entryDoor": oldDoor,
#	"exitDoor": newDoor,
#	"description": description,
#}
#roomType refers to a key in another file that defines what kinds of monsters can spawn there, and what kinds of treasure can spawn there
#squence determines the order that rooms were generated in. Sequence 1 is always at (0,0).
#x and yCoordinate explain where on a map different rooms are, and which doors connect to which rooms.
#entryDoor is the direction that the previous room is in.
#exitDoor is the direction that the next room is in.

print("How many rooms should we generate?")
numRooms = input()
numRooms = int(numRooms)
dungeonSet = {
	
}

roomNumber = 0
totalRooms = numRooms
while numRooms >= 0:
	roomNumber = roomNumber + 1

	if roomNumber == totalRooms + 1:
		print("ez game ez life")
		dungeonsetJson = json.dumps(dungeonSet, indent=4)
		f = open("currentDungeon.json", "w")
		f.write(dungeonsetJson)
		numRooms = numRooms - 1
		f.close()
		print("Done!")

	elif roomNumber == 1:
		xCoordinate = 0
		yCoordinate = 0
		roomType = 0
		oldDoor = "South"
		newDoor = "North"
		description = "This is the entrance room to the dungeon. There is a door ahead of you."

		room = {
			"sequence": roomNumber,
			"xCoordinate": xCoordinate,
			"yCoordinate": yCoordinate,
			"roomType": roomType,
			"entryDoor": oldDoor,
			"exitDoor": newDoor,
			"description": description,
		}
		dungeonSet[roomNumber] = room
		#print(dungeonSet)
		print(numRooms)
		numRooms = numRooms - 1

	elif roomNumber == 2:
		xCoordinate = 0
		yCoordinate = 1
		roomType = 0
		oldDoor = "South"
		newDoor = dungeonDoorDecider(oldDoor)
		description = "Piss and cum."

		room = {
			"sequence": roomNumber,
			"xCoordinate": xCoordinate,
			"yCoordinate": yCoordinate,
			"roomType": roomType,
			"entryDoor": oldDoor,
			"exitDoor": newDoor,
			"description": description,
		}
		dungeonSet[roomNumber] = room
		#print(dungeonSet)
		print(numRooms)
		numRooms = numRooms - 1

	else:
		coordinateResult = coordinateCreator(newDoor, xCoordinate, yCoordinate)
		xCoordinate = coordinateResult["xCoordinate"]
		yCoordinate = coordinateResult["yCoordinate"]
		oldDoor = newDoor
		oldDoor = directionReverser(oldDoor)
		newDoor = dungeonDoorDecider(oldDoor)
		roomType = 0
		description = "I ran out of ideas to create random descriptions. I will come back to this."
		room = {
			"sequence": roomNumber,
			"xCoordinate": xCoordinate,
			"yCoordinate": yCoordinate,
			"roomType": roomType,
			"entryDoor": oldDoor,
			"exitDoor": newDoor,
			"description": description,
		}
		dungeonSet[roomNumber] = room
		#print(dungeonSet)
		print(numRooms)
		numRooms = numRooms - 1