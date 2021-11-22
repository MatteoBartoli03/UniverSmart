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
        file.write("\n"+ num + ", " + mat.capitalize() )
        file.close()
        print("La materia inserita e' " + mat + " e avrà il codice " + num)
        return 0

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
            print(line[0] + " " + line[1])
    return 0

def data_from_IdM():
    n = input("Inserisci il numero di matricola: ")

    file = array_file("matricole.txt")    
    for a in file:
        if (a[0] == str(n)):
            print("Lo studente avente come numero di matricola " + str(n) + " e' " + a[1] + " " + a[2] )

    return 0