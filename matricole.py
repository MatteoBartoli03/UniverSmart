from functions import print_file, add_line_file, data_from_IdM

def matricola():
	while True:
		print()
		print("-----------------------------------------------------------------------------------------------------")
		print()
		print("MENU' MATRICOLE")
		print("1. stampa elenco matricole")
		print("2. inserisci un nuovo studente")
		print("3. stampa i dati di uno studente inserendo il numero di matricola")
		print("4. torna indietro")
		opt = input("cosa vuoi fare oggi? ")

		if opt == "1":
			print()
			print("Elenco matricole:")
			print_file("matricole.csv")
			input()
		elif opt == "2":
			add_line_file("matricole.csv")
			input()
		elif opt == "3":
			data_from_IdM()
			input()
		elif opt == "4":
			break
		else:
			print()
			print("Ritenta sarai più fortunato")
			input()