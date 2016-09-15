            #dictionaries
#un diccionario permite tener definidas varios valores para una variable
#list...linear collection of values that stay in order
#dictionary...a "bag" of values , each with its own label
#los diccionarios necesitan una etiqueta, como no hay un orden, no los puedes llamar como el 3er lugar o posicion etc..se les llama key/value...key=label y el value es el valor
#el diccionario es muy poderoso, es como una base de datos.

purse=dict()
purse["money"]=2
purse ["candy"]=3
purse["tissues"]=75
print purse
#>>>{'money': 2, 'tissues': 75, 'candy': 3}
print purse ["candy"]
#>>>3
purse["candy"]=purse["candy"]+2
print purse
#{'money': 2, 'tissues': 75, 'candy': 3}
#{'money': 2, 'tissues': 75, 'candy': 5}

#dictionary literals (constants)
#they use curly braces and have a list of key:value pairs
#you can make an empty dictionary using curly braces {}
#si mandas print del diccionario cuando no existe la palabra dentro del diccionario te manda error de traceback.
#lo que tienes que hacer para que no te mande error es buscar con "in"..
#lo que hace es preguntar is the string csev in the dictionary ccc?
#con esto ya tenemos un mini codigo que nos puede decir si existe el key dentro del dictionary
#ccc=dict()
#print "csev" in ccc
#>>>False


            #when we see a new name
#counts=dict()
#names=["csev","cwen","csev","zqian","cwen"]
#for name in names:
#    if name not in counts:
#        counts[name]=1
#    else:
#        counts[name]=counts[name]+1
#print counts
#abres el diccionario
#haces una lista llamada names
#haces un for...el for es un loop que corre por cierto numero definido de veces...le dices cuantas veces y con que valores quieres que corra despues del "in"
#dentro del lopp le dices...si el valor de la lista name que estas corriendo no esta en el diccionario, entonces asignale 1
#si esta dentro del diccionario, entonces significa que ya tiene asignado un valor y entonces lo que te dice es sumale a ese valor 1


#this pattern of checking to see if a "key" is already in a dictionary and assuming a default value if the key is not there is so common, that there is a method called "get()" that does this for us

#Los diccionarios tienen un metodo llamado get que toma una clave y un valor por defecto. Si la clave aparece en el diccionario, get devuelve el valor correspon- diente; si no, devuelve el valor por defecto. Por ejemplo:
#>>> contadores = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
#>>> print contadores.get('jan', 0)
#>>> 100
#>>> print contadores.get('tim', 0)
#>>>0

#Podemos usargetpara escribir nuestro bucle de histograma de forma mas concisa. Como el metodo get gestiona automaticamente el caso de que la clave no este en el diccionario, podemos reducir cuatro l ́ıneas a una sola y eliminar la sentencia if
#palabra = 'brontosaurio'
#d = dict()
#for c in palabra:
#d[c] = d.get(c,0) + 1
#print d

#if name in counts:
#    print counts[name]
#else:
#    print 0
#print counts.get(name,0)

#se utilizan 2 parametros para el get(key name, valor para que se regrese si el nombre no existe dentro del diccionario)
#osea....print counts.get(name,0)...counts es el nombre del dictionary, get es la funcion, name es la etiqueta que va a buscar dentro del diccionario y el 0 es el valor que le va a dar a la variable si no encuentra lo que viene en el diccionario
#default value if key does not exist(and no traceback)


#SIMPLIFIED COUNTING WITH A GET
#We can use get and provide a default value of 0 when the key is not yet in the dictionary-and then just add one

counts=dict()
names=["csev","cwen","csev","zqian","cwen"]
for name in names:
    counts[name]=counts.get(name,0)+1 #counts diccionario, [name] la iteration variable, si no la encuentra asigna el valor de 0
print counts

#abres el diccionario
#declaras tu lista
#haces un for para leer/usar cada palabra dentro de la lista
#dentro del for llamas al diccionario con la variable de la palabra dentro de ese loop del for
#lo que hace el get es buscar la palabra especifica del loop en el diccionario, si la encuentra te regresa su valor, si no la encuentra la mete al diccionario y le pone un valor de 0
#despues le sumas 1 para hacer el conteo y que se cree o que se le sume 1 al valor de cada palabra
#imprimes el diccionario para ver que valor tiene ahi adentro
