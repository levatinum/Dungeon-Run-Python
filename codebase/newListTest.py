print("This is what the new dictionary name is going to be.")
newName = input()

nameList = {
	"name": "Garrett",
	"name2": "Sean",
}

nameList2 = {
	"name": "Ed",
	"name2": "Juan",
}

newList = {
	"nameList": nameList,
	"nameList2": nameList2,
}

print(newList)

newList[newName]=newList.pop("nameList")
#del newList["nameList"]

print(newList)