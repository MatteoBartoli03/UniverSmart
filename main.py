from matricole import matricola
from materie import materia

while True:
	print()
	print("-----------------------------------------------------------------------------------------------------")
	print("-----------------------------------------------------------------------------------------------------")
	print()
	print("MENU' GENERALE")
	print("1. matricole")
	print("2. materie")
	print("4. esci definitavemente dal programma")
	opt = input("cosa vuoi fare? ")

	if opt == "1":
		matricola()
	elif opt == "2":
		materia()
	elif opt == "4":
		print("Alla prossima...")
		break
	else:
		print()
		print("Ritenta sarai più fortunato")
		input()