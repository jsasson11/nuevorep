#tuples

#tuples son muy parecidos a las listas, solo que las listas si se pueden alterar y los tuples no. (como una string)
#acuerdate que listas van entre [] y tuples van entre ()

#list=["joe","juan","pedro"]
#list[1]="pepe"
#print list >>> ['joe', 'pepe', 'pedro']

#a los tuples no les puedes aplicar el x.sort() ni el x.append("hola") ni x.reverse()

#los tuples son mas eficientes, como no se pueden modificar entonces python los puede procesar mas rapido. Son mas eficientes en memoria y performance
#cuando estamos haciendo variables temporales que no vamos a modificar preferimos usar tuples

#se pueden meter en la parte izquierda de un assignment statement
#(x,y)= (4, "fred")
#print y
#a,b=(99,98)
#print a

#el metodo de .items() te regresa una lista de tuples, en los tuples encuentras del lado izquierdo el key y del derecho el value

#d=dict()
#d["hola"]=2
#d["bye"]=4
#for k,v in d.items():
#    print k,v
#>>>>bye 4
#>>>>hola 2
#tups=d.items()
#print tups
#>>>> [('bye', 4), ('hola', 2)]

#tuples are comparable

#(0,1,2)<(3,4,5) ; true
#compara el primero contra el primero y si eso cumple ya ni revisa los demas valores...aqui compara el 0 contra el 3 y si se cumple entonces ya no revisa que se cumplan los demas.
#(0,1,20000000)<(0,3,4); true
#compara el 0 contra el 0 que empatan, entonces se va contra el 1 y el 3 y eso si se cumple, entonces ya ni revisa el 2millones con el 4

#("jones", "sally")<("jones","fred") ; false
#jones y jones empatan entonces pasa con sally y fred, la S no es menor que la F en orden alfabetico y por eso es false
#("jones", "sally")>("adams","sam") ; true
#jones si es mas grande que adams, entonces ni siquiera ve los valores de sally y sam

#si lo puedes comparar entonces lo puedes ordenar; de la sig manera
#dic={"a":10,"b":1, "c":22} #tienes un diccionario
#t=dic.items() #lo metes a una variable y lo haces un tuple
#print t
#[('a', 10), ('c', 22), ('b', 1)]
#t.sort() #ese variable la aplicas un sort
#print t


#puedes usar la funcion SORTED que toma como parametro una lista y te regresa una version ordenada de esa lista
#dic={"a":10,"b":1, "c":22}
#print dic.items # [("a":10),("c":22), ("b":1)]
#t=sorted(dic.items()):
#print t #[('a', 10), ('c', 22), ('b', 1)]

#lo puedes hacer directo con
#for k,v in sorted(dic.items()):
#    print k,v
#a 10
#b 1
#c 22

#cuales son las 5 palabras mas comunes? #organizariamos por orden descendiente a los values no las keys
#c={"a":10,"b":1, "c":22} #abro el diccionario con los keys and values
#tmp=list() #abro una lista
#for k,v in c.items(): #volver el diccionario en una lista de tuples 
#    tmp.append((v,k)) #quiero incluir en la lista todos los values y keys del diccionario en orden de primero los values y luego los keys. Estos ya se encuentran separados por tuples en una lista
    #se tiene que construir la lista segun como se quiera ordenar mas abajo
#print tmp
#tmp.sort(reverse=True) #ya que tengo todos los values y keys bien ordenados en la lista, ya lo puedo organizar con sort y poniendo el parametro reverse=True para que sea de mayor a menor.
#print tmp


file=open("romeo.txt") #open a file
count=dict() #open a dictionary
for line in file: #read each line in the file
    line=line.split() #convert each line into a list of "words"
    for word in line: #loop through each word inside the list
        count[word]=count.get(word,0)+1 #look if the word is in the dictionary, if it is, bring me the value, if it is not assign it to 0...then add 1

lst=list() #open a list
for k,v in count.items(): #vuelve
    lst.append((v,k))
lst.sort(reverse=True)

for v,k in lst[:10]:
    print v,k











