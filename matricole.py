from functions import print_file, add_line_file, data_from_IdM, exam_from_Idm
import os

def matricola():
	os.system("CLS")
	while True:
		print()
		print("-----------------------------------------------------------------------------------------------------")
		print()
		print("MENU' MATRICOLE")
		print("1. stampa elenco matricole")
		print("2. inserisci un nuovo studente")
		print("3. stampa i dati di uno studente inserendo il numero di matricola")
		print("4. stampa gli esami dello studente inserendo il numero di matricola")
		print("5. torna indietro")
		opt = input("cosa vuoi fare oggi? ")

		if opt == "1":
			print()
			print("Elenco matricole:")
			print_file("matricole.csv") #stampare il contenuto di un file
			print()
			input("premi un tasto per continuare")
		elif opt == "2":
			add_line_file("matricole.csv")
			input("premi un tasto per continuare")
		elif opt == "3":
			data_from_IdM()
			print()
			input("premi un tasto per continuare")
		elif opt=="4":
			exam_from_Idm()
			print()
			input("premi un tasto per continuare")
		elif opt == "5":
			break
		else:
			print()
			print("Ritenta sarai più fortunato")
			input()