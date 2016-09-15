fhand=open('texto.txt')
for line in fhand:
    print line

#primero declaras que necesitas dirigirte a un texto
#el comando open solamente es para abrirlo, despues necesitas el "handle" para decirle a python que quieres que 
#le haga a ese texto...que lo lea nada mas pones , 'r', que escriba 'w' etc
#ahorita esta implicito que lo va a leer porque si no pones la r eso es lo que entiende
#entonces, el fhand hace que me refiera a ese texto
#el for ya le esta diciendo que lea "line" dentro del texto y despues que imprima cada una de las lineas

                    #counting the lines in a file
fhand=open('texto.txt')
count=0
for line in fhand:
    count=count+1
print 'line count',count

#abrimos el file
#declaramos el count en 0
#le dices que haga un for con el texto
#hacemos que cada vez que de vuelta el for para todas las lineas vaya sumando 1
#ya nada mas imprimes esa variable

#open the file
#for loop to read each line
#count the lines and print out the number of lines
#handle es como un access point
#file handle is a special kind of a sequence (of lines, of text etc) tienes que ver el texto como una secuencia


          #reading a whole file
fhand=open('texto.txt')
inp=fhand.read()
print len(inp)
print inp[:32]

#it isnot broken into lines
#no lo quieres hacer si el archivo es muy grande porque lo va a guardar en la memoria ram y se te va a alentar la cpu
#abrimos el handle del texto
#le damos read y declaramos la variable inp para que te lo de como una string
#como ya tienes el formato en string ya le puedes decir a python que te de el len
#ya despues le dices que te imprima desde el "0" hasta el caracter "32" (sin incluir el 32) para que te de "Existe el bando del buen gobierno"


            #searching through a file
fhand=open('texto.txt')
for line in fhand:
    if line .startswith('DF'):
        print line

#we can put an if statement in our for loop to only print lines that meet some criteria 
#el for va a hacer que busque dentro de todo el texto
#el if va a buscar cada vez que se haga el for cual de las lineas empieza con DF y va a imprimir la que empiece con DF
#como el if se va a repetir varias veces por el for puede ser que se cumpla mas de una vez la busqueda y lo puede imprimir varias veces


            #searching through a file 2
#siempre que se acaba la linea tiene un "new line" implicito  /n
#siempre que le pides a python un print le pone implicito un /n
#entonces cuando estas leyendo varias lineas, las lineas tienen doble espacio entre ellas
#el new line es considerado como white space
#entonces para lidear con este doble espacio tienes que quitar solo 1 de ese white space
#we can strip the whitespace from the right using rstrip () from the string library

fhand=open('texto.txt')
for line in fhand:
    line=line.rstrip()
    if line .startswith('DF'):
        print line

#ahora lo que va a salir de new lines es lo que viene del print, no los new lines que estaban implicitos en el texto



                #skipping with continue

fhand=open('texto.txt')
for line in fhand:
    line=line.rstrip()
#skip uninteresting lines
    if not line.startswith('from:'):
        continue
    #process our interesting line
    print line

#acuerdate que el continue dice aqui se acabo esta iteracion, vuelvete para arriba sin mirar lo que sigue
#entonces abres el texto, enlazas el texto con el for, le quitas lo blanco a las lineas
#si la linea no empieza con "from" continua, si si empieza con from imprime la linea
#puedes usar este metodo o el de arriba dependiendo de la complejidad que quieras


        #using in to select lines
#we can look for a string anywhere in a line as our selection criteria
fhand=open('texto.txt')
for line in fhand:
    line=line.rstrip()
    if not 'DF' in line:
        continue
    print line

#si el texto "df" no esta en la linea, entonces continue. Si si esta, entonces imprime.
#es una manera de saltar todas las lineas que no tengan lo que te interesa
            
            
            
            #PROMPT FOR A FILE NAME
fname=raw_input("Enter the file name: ")
fhand=open(fname)
count=0
for line in fhand
    if line .startswith('subject:'):
        count=count+1
print "there were", count, "subject lines in", fname


            #DATE CUENTA CON TRY EXCEPT SI EL FILE NAME ES CORRECTO
fname=raw_input("Enter the file name: ")
try:
fhand=open(fname)
except:
    print "File cant be opened:",fname
    exit()  
count=0
for line in fhand
    if line .startswith('subject:'):
        count=count+1
print "there were",count,"subject lines in:",fname


    
 
















