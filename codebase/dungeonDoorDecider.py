def dungeonDoorDecider(prevNewDoor):
	directions = ["North", "West", "East"]
	directions.remove(prevNewDoor)
	newDirection = random.choice(directions)
	return newDirection