#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest
#number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as
#the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count
#of the number of times they appear in the file. After the dictionary is produced, the program reads through the
#dictionary using a maximum loop to find the most prolific committer.

fhand=open("mbox-short.txt")
text=fhand.read().rstrip().split()

counts=dict() #abres un diccionario
for x in text: #le pides que corra tu iteration variable (word) dentro de la lista de words...osea que corra cada palabra de la lista
    counts[x]=counts.get(x,0)+1 #para la etiqueta x dame su valor, si la palabra x no esta en el diccionario ponle valor de 0...y despues sumale 1
#aqui ya estoy contando cada palabra en esta lista

if x =="From ":
    print x
else:
    print "else"


bigcount=None
bigword=None
for x,valor in counts.items():
    if bigcount is None or valor>bigcount:
        bigcount=valor
        bigword=x
print "La palabra: ", bigword, "se repite: ", bigcount, "veces"

