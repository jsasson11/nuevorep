#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#Desired Output
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

file=open("mbox-short.txt") #abres el texto
counts=dict() #abres el diccionario
lst=list() #abres una lista

for line in file: #lees cada linea del texto
    if not line.startswith("From "): continue #si la linea no empieza con From continua a la siguiente linea
    line=line.split() #la linea que empezo con From, conviertela en una lista de de palabras en el mismo orden
    line=line[5] #traeme unicamente el subindice 5 (es donde se encuentra la hora, minutos y segundo)
    line=line.split(":") #esa misma string vuelvela a dividir en una lista de 3 elementos. Hora minutos y segundos
    line=line[0] #traeme el elemento subindice 0 (la hora)
    counts[line]=counts.get(line,0)+1 #busca esta hora en el diccionario, si la encuentras regresame el valor, si no asignale valor de 0...sumale 1

#ya tienes el diccionario con la cuenta de cada hora, ahora hay que organizarlo.
for k,v in counts.items(): #vuelve el diccionario una lista de tuples, sobre esa lista ahora loopea con las 2 iteration variables y jala el key y el value de cada elemento dentro de la lista de tuples. 
    lst.append((k,v)) #ya que tienes el key y el value insertalo a una nueva lista
lst.sort() #organiza esta lista por orden segun los keys
for k,v in lst:
    print k,v #imprime cada valor de esa lista ya ordenada.

    
