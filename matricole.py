max_record = 10
num=int(input("Inserisci numero di matricole: "))

if num > max_record:
	print("superato numero massimo di matricole possibili")
	exit()

file = open("MATRICOLE.txt", "a")

array_matricole = []

for persona in range(num):
	matricola=dict()
	matricola["IdMatricola"] = input("inserisci il numero di matricola: ")
	matricola["Cognome"] = input("inserisci il cognome della matricola: ")
	matricola["Nome"] = input("inserisci il nome della matricola: ")
	array_matricole.append(matricola)
	file.write("\n"+matricola["IdMatricola"]+", "+matricola["Cognome"]+", "+matricola["Nome"])

file.close()
file = open("MATRICOLE.txt", "r")


for i in range(num):
	print(array_matricole[i])

while True:
	opt = input("Scrivi 1 se vuoi conoscere i dati di uno studente altrimenti premi un altro tasto: ")
	if (opt == "1"):
		n = input("inserisci il numero di matricola: ")
		for i in array_matricole:
			if (i["IdMatricola"] == n):
				print(i)
	else:
		break