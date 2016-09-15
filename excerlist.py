#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
#the split() function. The program should build a list of words. For each word on each line check to see if the
#word is already in the list and if not append it to the list. When the program completes, sort and print the
#resulting words in alphabetical order.

text=open("romeo.txt")
list1=list()
for x in text:
    line=x.rstrip().split()
    for word in line:
        if word in list1:
            continue
        else:
            list1.append(word)
list1.sort()
print list1

#abres el texto
#abres la lista en 0
#con un for haces que x se convierta en cada palabra del texto
#despues limpias esa linea con rstrip...como tiene enter igual queda 1 /n
#despues spliteas esa linea en listas de palabras y te queda una lista por cada enter

    #despues le haces un for a esa lista de palabras...lo que el for hace es revisar cada palabra en la linea
    #si la palabra ya esta entonces continua con la proxima
    #si no esta en la lista se agrega 
#ordenas la lista
#imprimes la lista una vez que ya se le agregaron todas las lineas...no importa si la linea se repite
