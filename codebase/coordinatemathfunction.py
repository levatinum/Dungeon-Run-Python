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