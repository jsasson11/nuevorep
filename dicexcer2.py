#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest
#number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as
#the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count
#of the number of times they appear in the file. After the dictionary is produced, the program reads through the
#dictionary using a maximum loop to find the most prolific committer.

handle=open("mbox-short.txt") #abro el text
dict={} #abro el diccionario

for line in handle: #hago un for para leer el diccionario
    if not line.startswith("From "): continue #si la linea no empieza con From continua al siguiente loop
    line=line.split() #aqui significa que la linea si empieza con From, por lo que convertimos esa linea en una lista usando split
    line=line[1] #aqui borro todo lo que no me sirve de esa lista y nada mas quedo con el subindice 1 de la lista "que es el mail"
    dict[line]=dict.get(line,0)+1 #aqui pido el valor de mi variable, si lo encuentra me lo regresa y le suma 1. Si no lo encuentra me regresa 0 y le suma 1.

bigcount=None
bigword=None
for word,count in dict.items(): #aqui hago un for loop para que la iteration variable "word" y "count" se conviertan en los key y los values del diccionario.
    if bigword is None or bigcount < count: #si el bigword es None (para la 1era vez) entonces iguala ese key y ese value a los contadores (los contadores son las variables bigword y bigcount), Ó si el bigcount es menor al count(iteration variable) entonces ya pasamos el primer valor y encontramos un key con un valor mas alto
        bigcount=count
        bigword=word
    else:
     continue
print bigword,bigcount