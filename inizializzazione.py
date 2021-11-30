file = open("MATERIE.csv", "w")
file.write("IdMateria, Materia, Prezzo_Esame")
file.close()

file = open("MATRICOLE.csv", "w")
file.write("IdMatricola, Cognome, Nome")
file.close()

file = open("ESAMI.csv", "w")
file.write("IdEsame, IdMatricola, IdMateria, PagamentoEffettuato, EsitoEsame, timestamp")
file.close()