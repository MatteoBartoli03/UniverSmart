max_esami = 3
esami=int(input("Inserisci numero di esami da sostenere: "))

if esami > max_esami:
	print("superato numero massimo di esami possibili")
	exit()

file = open("ESAMI.txt", "w+")
file.write("IdMatricola, IdMateria")

esame=dict()

for b in range(esami):
	esame["IdMatricola"] = input("inserisci il numero di matricola: ")
	esame["IdMateria"] = input("inserisci il numero di materia: ")
	file.write("\n"+esame["IdMatricola"]+", "+esame["IdMateria"])
