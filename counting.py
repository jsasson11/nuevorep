#counts=dict()
#print "enter a line of text"
#line=raw_input("")
#words=line.split()
#print "words:",words
#print "counting..."
#for word in words:
 #   counts[word]=counts.get(word,0)+1
#print "Counts",counts
#abres el diccionario
#pides las palabras
#spliteas las palabras para que se haga una lista de strings
#despues haces el for para que corra cada una de las palabras
#y ya despues le pones el get para que haga lo que vimos en dictionaries.py


#la palabra mas repetida en un texto
name=raw_input("Enter a file name:")
handle=open(name)
text=handle.read()#no leo el archivo con un for porque este archivo es pequeno entonces no ocupa mucho espacio y lo puedo dejar guardado en una variable
words=text.split() #aqui ya converti el string a una lista de palabras


counts=dict() #abres un diccionario
for x in words: #le pides que corra tu iteration variable (word) dentro de la lista de words...osea que corra cada palabra de la lista
    counts[x]=counts.get(x,0)+1 #para la etiqueta x dame su valor, si la palabra x no esta en el diccionario ponle valor de 0...y despues sumale 1
#print counts
#aqui ya estoy contando cada palabra en esta lista


bigcount=None
bigword=None
for x,valor in counts.items():
    if bigcount is None or valor>bigcount:
        bigcount=valor
        bigword=x
print "La palabra: ", bigword, "se repite: ", bigcount, "veces"

#aqui lo que hice fue correr un for con dos iteration variables...
#para correr estos fors siempre tienes que decirle que al for que estas hablando de .items()
#un item es el conjunto de una etiqueta y un valor dentro del diccionario
#entonces, cuando haces un for de este tipo siempre la primer iteration variable es la etiqueta y la segunda es el valor de esa etiqueta
#el for corre esa iteration variable dentro del diccionario y lo que le dice es
#si bigcount es "none" o "valor" es mayor que "bigcount" entonces asignale a bigcount ese valor y a bigword asignale la etiqueta de ese valor
#lo que hace es que esta corriendo el for y cuando la cuenta esta en none o el valor de la iteration que esta corriento es mayor que la cuenta entonces
#asigna esos valores que son los mas altos hasta el momento a las variables. si no son mas altos no se cumple el if y no los asigna
