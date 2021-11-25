file = open("MATERIE.txt", "w")
file.write("IdMateria, Materia, Prezzo_Esame")
file.close()

file = open("MATRICOLE.txt", "w")
file.write("IdMatricola, Cognome, Nome")
file.close()

file = open("ESAMI.txt", "w")
file.write("IdEsame, IdMatricola, IdMateria, PagamentoEffettuato, EsitoEsame")
file.close()