import datetime
import os

def add_line_file(x):
    print()
    if x == "matricole.csv":
        file = open(x, "a")
        mat = str(len(array_file(x)))
        cog = input("Inserisci il cognome dello studente: ")
        nom = input("Inserisci il nome dello studente: ")
        file.write("\n"+ mat + ", " + cog.capitalize() + ", " + nom.capitalize())
        file.close()
        print("Il numero di matricola che verrà attribuito a " + cog + " " + nom + " e' " + mat)
        return 0

    elif x == "materie.csv":
        file = open(x, "a")
        num = str(len(array_file(x)))
        mat = input("Inserisci il nome della materia: ")
        cifra = input("Inserisci il prezzo dell'esame: ")
        file.write("\n"+ num + ", " + mat.capitalize() + ", " + cifra)
        file.close()
        print("La materia inserita e' " + mat + ", avrà il codice " + num + " e il suo esame costera' " + cifra + "€")
        return 0

    elif x== "esami.csv":
        file = open(x, "a")
        IdEsame = str(len(array_file(x)))
        matricola = input("Inserisci l'id della matricola che deve compiere l'esame: ")
        materia= input ("Inserisci l'id della materia argomento di esame: ")
        esito_Pagamento = False
        esito_Esame = "notPassed"
        timestamp = "null"

        file.write("\n"+ IdEsame +  ", " + matricola.capitalize() + ", " + materia.capitalize() +  ", " + str(esito_Pagamento) + ", " + str(esito_Esame) + ", " + str(timestamp))
        file.close()

        file1 = array_file("materie.csv")
        for i in file1:
            if (str(i[0]) == str(materia)):
                nome_materia = i[1]
                costo = i[2]

        print("La matricola " + matricola + " dovra' fare l'esame di " + nome_materia + ". L'esame avrà un costo di " + costo + "€.")

def array_file(x):
    f = open(x, "r")

    list_of_lists = []
    inner_list = []
    for line in f:
        for x in line.split(","):
            inner_list = inner_list + [x.strip()]
        list_of_lists.append(inner_list)
        inner_list = []
    return list_of_lists

def print_file(x):
    file = array_file(x)

    if x=="materie.csv":
        for line in file:
            if (file.index(line)==0):
                print(line[0] + " " + line[1] + " " + line[2])
            else:
                print(line[0] + " " + line[1] + " " + line[2]+"€")
    else:
        for line in file:
            if len(line) == 3:
                print(line[0] + " " + line[1] + " " + line[2])
            else:
                print(line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " " + line[4] + " " + line[5])
    return 0

def data_from_IdM():
    n = input("Inserisci il numero di matricola: ")

    file = array_file("matricole.csv")    
    for a in file:
        if (a[0] == str(n)):
            print("Lo studente avente come numero di matricola " + str(n) + " e' " + a[1] + " " + a[2] )

    return 0

def exam_from_Idm():

    num = input("Inserisci il numero di matricola: ")
    file = array_file("esami.csv")
    file1= array_file("materie.csv")
    print()
    print("Lo studente dovrà fare i seguenti esami: ")


    for a in file:
        if (a[1] == str(num)):

            for b in file1:
                if (b[0] == a[2] ):
                    print(b[1])
            

    return 0

def change_esito_pagamento():

    import os
    file_esami_iniziale = array_file("esami.csv")
    print()
    matricola = str(input("inserisci il numero di matricola: "))
    materie = array_file("materie.csv")
    materia = str(input("inserisci l'id corrispondente alla materia d'esame: "))
    status = 0

    for esame in file_esami_iniziale:
        if (esame[1] == matricola):
            if (esame[2] == materia):
                if (status == 0):
                    idEsame = esame[0]
                    if esame[3] == 'False':
                        print()
                        print("Risulta che il pagamento non è stato ancora effettuato!")
                        print("- premere 1 per versare " + materie[int(esame[2])][2] + "€")
                        print("- premere un qualsiasi altro carattere per non effettuare il pagamento e tornare al menu precedente")
                        ris = input()
                        if ris == "1":
                            file_esami_iniziale[int(idEsame)][3] = 'True'
                            print()
                            print("Il pagamento è stato effettuato.")
                        else:
                            print("Pagamento non effettuato")
                        status = 1
                        break

                    if esame[3] == 'True':
                        print()
                        print("Risulta che il pagamento è già stato effettuato!")
                        print("Non è possibile essere rimborsati una volta che il pagamento è stato effettuato.")
                        status = 1
                        ''' questa parte è da reinserire e mettere a posto solo se è possibile essere rimborsati
                        print("- premere 1 se desideri annullare il pagamento ed essere rimborsato")
                        print("- premere un qualsiasi altro carattere per lasciare invariato invariato lo stato di pagamento e tornare al menu precedente")
                        ris = input()
                        if ris == "1":
                            file_esami_iniziale[int(idEsame)][3] = 'False'
                        print()
                        print("Il pagamento non è stato ancora effettuato")
                        '''
                        break

    if status == 0:
        print("non esiste un esame con tali matricola e materia")
            
    os.remove("ESAMI.csv")

    f = open("ESAMI.csv", "a")
    x = 0
    for e in file_esami_iniziale:
        f.write(e[0] + ", " + e[1] + ", " + e[2] + ", " + e[3] + ", " + e[4] + ", " + e[5])
        x += 1
        if int(x) != int(int(len(file_esami_iniziale))):
            f.write("\n")

def change_esito_esame():

    file_esami_iniziale = array_file("esami.csv")
    print()
    matricola = str(input("inserisci il numero di matricola: "))
    materia = str(input("inserisci il numero corrispondente alla materia d'esame: "))
    status = 0

    for esame in file_esami_iniziale:
        if (esame[1] == matricola):
            if (esame[2] == materia):
                if (status == 0):
                    idEsame = esame[0]
                    if esame[4] == 'notPassed':
                        if esame[3] == 'True':
                            print()
                            print("Risulta che l'esame non è ancora stato passato!")
                            print("- premere 1 per inserire l'esito")
                            print("- premere un qualsiasi altro carattere per tornare al menu precedente")
                            ris = input()
                            if ris == "1":
                                print()
                                ris2 = input("Digitare 1 se l'esame è stato passato, mentre digitare 2 se non è stato passato: ")
                                if ris2 == "1":
                                    file_esami_iniziale[int(idEsame)][4] = 'passed'
                                    ct = datetime.datetime.now()
                                    ts = ct.timestamp()
                                    file_esami_iniziale[int(idEsame)][5] = str(ts)
                                    print()
                                    print("L'esame è stato passato in questa data e ora: " + str(ct))
                                elif ris2 == "2":
                                    file_esami_iniziale[int(idEsame)][3] = "False"
                                    print()
                                    print("L'esame non è stato superato, per cui per rifarlo bisognerà rieffettuare il pagamento")
                                else:
                                    print("Esito esame non inserito")
                            status = 1
                            break
                        elif esame[3] == "False":
                            print("Risulta che l'esame non è ancora stato passato.")
                            print("Prima di passarlo dovrai pagarlo.")
                            status = 1

                    if esame[4] == 'passed':
                        print()
                        print("Risulta che l'esame è già stato passato!")
                        status = 1
                        break

    if status == 0:
        print()
        print("non esiste un esame con tali matricola e materia")
            
    os.remove("ESAMI.csv")

    f = open("ESAMI.csv", "a")
    x = 0
    for e in file_esami_iniziale:
        f.write(e[0] + ", " + e[1] + ", " + e[2] + ", " + e[3] + ", " + e[4] + ", " + e[5])
        x += 1
        if int(x) != int(int(len(file_esami_iniziale))):
            f.write("\n")