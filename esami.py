from functions import print_file, add_line_file, change_esito_pagamento, change_esito_esame
import os

def esame():
	while True:
		os.system("CLS")
		print()
		print("-----------------------------------------------------------------------------------------------------")
		print()
		print("MENU' ESAMI")
		print("1. stampa elenco esami per idMatricola-idMateria")
		print("2. inserisci un nuovo esame")
		print("3. versare pagamento della quota esame")
		print("4. inserisci esito esame")
		print("5. torna indietro")
		opt = input("cosa vuoi fare? ")

		if opt == "1":
			print()
			print("Elenco esami")
			print_file("esami.csv")
			print()
			input("premi un tasto per continuare")
		elif opt == "2":
			add_line_file("esami.csv")
			print()
			input("premi un tasto per continuare")
		elif opt == "3":
			change_esito_pagamento()
			print()
			input("premi un tasto per continuare")
		elif opt == "4":
			change_esito_esame()
			print()
			input("premi un tasto per continuare")
		elif opt == "5":
			break
		else:
			print()
			print("Ritenta sarai più fortunato")
			print()
			
