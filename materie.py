from functions import print_file, add_line_file

def materia():
	while True:
		print()
		print("-----------------------------------------------------------------------------------------------------")
		print()
		print("MENU' MATERIE")
		print("1. stampa elenco materie")
		print("2. inserisci una nuova materia e prezzo del relativo esame")
		print("3. torna indietro")
		print()
		opt = input("cosa vuoi fare? ")

		if opt == "1":
			print()
			print("Elenco materie:")
			print_file("materie.txt")
			print()
			input("premi un tasto per continuare")
		elif opt == "2":
			add_line_file("materie.txt")
			print()
			input("premi un tasto per continuare")
		elif opt == "3":
			break
		else:
			print()
			print("Ritenta sarai più fortunato")
			print()
			