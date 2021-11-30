def add_line_file(x):
    print()
    if x == "matricole.txt":
        file = open(x, "a")
        mat = str(len(array_file(x)))
        cog = input("Inserisci il cognome dello studente: ")
        nom = input("Inserisci il nome dello studente: ")
        file.write("\n"+ mat + ", " + cog.capitalize() + ", " + nom.capitalize())
        file.close()
        print("Il numero di matricola che verrà attribuito a " + cog + " " + nom + " e' " + mat)
        return 0

    elif x == "materie.txt":
        file = open(x, "a")
        num = str(len(array_file(x)))
        mat = input("Inserisci il nome della materia: ")
        cifra = input("Inserisci il prezzo dell'esame: ")
        file.write("\n"+ num + ", " + mat.capitalize() + ", " + cifra)
        file.close()
        print("La materia inserita e' " + mat + ", avrà il codice " + num + " e il suo esame costera' " + cifra + "€")
        return 0

    elif x== "esami.txt":
        file = open(x, "a")
        IdEsame = str(len(array_file(x)))
        matricola = input("Inserisci l'id della matricola che deve compiere l'esame: ")
        materia= input ("Inserisci l'id della materia argomento di esame: ")
        esito_Pagamento = False
        esito_Esame = False

        file.write("\n"+ IdEsame +  ", " + matricola.capitalize() + ", " + materia.capitalize() +  ", " + str(esito_Pagamento) + ", " + str(esito_Esame))
        file.close()

        file1 = array_file("materie.txt")
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

    for line in file:
        if len(line) == 3:
            print(line[0] + " " + line[1] + " " + line[2])
        else:
            print(line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " " + line[4])
    return 0

def data_from_IdM():
    n = input("Inserisci il numero di matricola: ")

    file = array_file("matricole.txt")    
    for a in file:
        if (a[0] == str(n)):
            print("Lo studente avente come numero di matricola " + str(n) + " e' " + a[1] + " " + a[2] )

    return 0

def exam_from_Idm():

    num = input("Inserisci il numero di matricola: ")
    file = array_file("esami.txt")
    file1= array_file("materie.txt")
    print()
    print("Lo studente dovrà fare i seguenti esami: ")


    for a in file:
        if (a[0] == str(num)):

            for b in file1:
                if (b[0] == a[1] ):
                    print(b[1])
            

    return 0

def change_esito_pagamento():
    file = open()