#Monster Maker, I guess
import json

#"name": "Minotaur",
#"type": "Beast",
#"description": "The Minotaur is a large man with a bull's head.",
#"inspection": "It seems as though its horns could be removed with sufficient force."
#"monval": "5",
#"primloot": "minotaur"
#"secloot": "man"

print("Welcome to Monster Maker v.1 for Dungeon Run: Python.")

while True:
	print("First, what monster are you making?")
	monName = input()

	print("Next, please define the type of monster. Beast, elemental, etc.")
	monType = input()

	print("Next, please apply the primary tag this monster should use. Horned, flying, etc.")
	monTag = input()

	print("Is this creature armed or unarmed?")
	print("Responses should be armed or unarmed.")
	armament = input()

	print("Next, define the rankVal of the monster. This determines the equipment and tags it might have.")
	rankVal = input()

	print("Write a short description of the monster.")
	description = input()

	print("Please write the inspection text, a short piece that explains a specific strategy to dealing with the monster.")
	inspect = input()

	print("Please write the amount of money that the monster should drop in gold pieces. e.g. '5'")
	monVal = input()

	print("Please define the primary loot pool this monster should pull from.")
	primLoot = input()

	print("Please define the secondary loot pool this monster should pull from.")
	secLoot = input()

	monster = {
		"name": monName,
		"type": monType,
		"tag": monTag,
		"armament": armament,
		"rankVal": rankVal,
		"description": description,
		"inspection": inspect,
		"monVal": monVal,
		"primLoot": primLoot,
		"secLoot": secLoot
	}

	#monName = casefold(monName)
	monName.casefold()
	filename = monName + ".json"

	f = open(filename, "a")
	monsterfile = json.dumps(monster, indent=3)
	f.write(monsterfile)
	f.close()
	print("Done. Starting again.")