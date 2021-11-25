from functions import print_file, add_line_file

def esame():
	while True:
		print()
		print("-----------------------------------------------------------------------------------------------------")
		print()
		print("MENU' ESAMI")
		print("1. stampa elenco esami per idMatricola-idMateria")
		print("2. inserisci un nuovo esame")
		print("3. inserisci esito pagamento di un esame indicando il suo id")
		print("4. inserisci esito esame indicando il suo id")
		print("5. torna indietro")
		print()
		opt = input("cosa vuoi fare? ")

		if opt == "1":
			print()
			print("Elenco esami")
			print_file("esami.txt")
			print()
			input("premi un tasto per continuare")
		elif opt == "2":
			add_line_file("esami.txt")
			print()
			input("premi un tasto per continuare")
		elif opt == "3":
			change_esito_pagamento()
		elif opt == "5":
			break
		else:
			print()
			print("Ritenta sarai più fortunato")
			print()
			