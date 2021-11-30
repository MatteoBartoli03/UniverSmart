from matricole import matricola
from materie import materia  
from esami import esame
#con i from si importano delle funzioni da altri file, in questo caso matricola() da matricole.py

while True:
	print()
	print("-----------------------------------------------------------------------------------------------------")
	print("-----------------------------------------------------------------------------------------------------")
	print()
	print("MENU' GENERALE")
	print("1. matricole")
	print("2. materie")
	print("3. esami")
	print("4. esci definitavemente dal programma")
	print()
	opt = input("cosa vuoi fare? ")


	if opt == "1":
		matricola()
	elif opt == "2":
		materia()
	elif opt == "3":
		esame()
	elif opt == "4":
		print("Alla prossima!")
		break
	else:
		print()
		print("Ritenta sarai più fortunato")
		input()