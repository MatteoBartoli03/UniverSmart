file = open("MATERIE.txt", "w")
file.write("IdMateria, Materia")
file.close()

file = open("MATRICOLE.txt", "w")
file.write("IdMatricola, Cognome, Nome")
file.close()

file = open("ESAMI.txt", "w")
file.write("IdMatricola, IdMateria")
file.close()