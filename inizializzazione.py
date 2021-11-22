file = open("MATERIE.csv", "w")
file.write("IdMateria, Materia")
file.close()

file = open("MATRICOLE.csv", "w")
file.write("IdMatricola, Cognome, Nome")
file.close()

file = open("ESAMI.csv", "w")
file.write("IdMatricola, IdMateria")
file.close()