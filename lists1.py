#una lista es como una coleccion
#una coleccion te permite cargar muchos valores en un "paquete"
#los elementos dentro de la lista van entre {} separados por ,
#cualquier objeto de python puede estar dentro de una lista, incluso otra lista
# ["joseph", "glenn", 24, 48.76,[5,6], "algo"]
#no se puede cambiar el contenido de una string, cuando cambias una string realmente se te esta regresando una copia en upper o en lower etc
#las listas si se pueden modificar (ve list practica para ejemplo)



                #average in a list
numlist=list()
while True:
    inp=raw_input("enter a number: ")
    if inp == "done": break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print average
#lo que hace es abrir una lista sin ningun elemento adentro
#despues pide datos y esos datos los convierte en floats
#esos floats los mete a la lista con "append" y ya despues le pides lo que necesites

#la diferencia de hacerlo de esta manera a hacerlo con un while y hacer la suma y un count es:
#la lista guarda todos los datos, entonces si te importa el espacio no es igual de eficiente ya que el otro metodo nada mas hace el calculo y no guarda mucha info
#con la lista puedes pedirle que haga varias cosas con menos codigo necesario por lo que puede simplificar la operacion


        #STRINGS and LISTS
#el split lo que hace es que agarra un string, busca los espacios en blanco dentro del string
#divide el split y te regresa una lista de items ya por separado definido por los espacios dentro del string
#el split toma muchos espacios juntos como si fuera uno solo
#el split puede dividir tambien por comas o por ;...solo tienes que decirle al split que asi quieres que lo divida poniendolo en el parentesis
abc="With three words"
stuff=abc.split()
print stuff
#["With", "three", "words"]
print len(stuff)
#[3]
print stuff[2]
#words


#a veces puedes necesitar hacer el split dos veces, namas le metes doble split y ya
#cuando quieres buscar dentro de un texto pueded utilizar el for (para leer todo el documento) y despues un if (para que busque tus requerimientos) y despues el split (para que parta y organice dependiendo de tus requerimientos) y ya despues las operaciones que necesitas
#es mas elegante hacer un double split para buscar que estar haciendo "slice" con el buscador de [:]
#split a thing of a list then you take it out and split it again
 

friends=('joseph','sally','molly')
print len(friends)
print range(len(friends))
print friends
print friends[0:1]

    
    
