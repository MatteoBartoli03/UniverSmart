max_materie = 3
materie=int(input("Inserisci numero di materie: "))

if materie > max_materie:
	print("superato numero massimo di materie possibili")
	exit()

file = open("MATERIE.csv", "w+")
file.write("IdMateria, Materia")

array_materie = []

for a in range(materie):
	materia=dict()
	materia["IdMateria"] = input("inserisci il numero di materia: ")
	materia["Materia"] = input("inserisci la materia: ")
	array_materie.append(materia)
	file.write("\n"+materia["IdMateria"]+", "+materia["Materia"])

for i in range(num):
	print(array_materie[i])