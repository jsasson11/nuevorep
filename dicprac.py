#dic={}
#text=raw_input("Enter a line of text: ")
#text=text.split()
#for i in text:
#    dic[i]=dic.get(i,0)+1
#print dic

#abro el dic
#pido un texto
#spliteo ese texto para hacerlo una lista
#hago el for para pasar por toda esa lista
#voy a buscar en el dic cada "key" que tome la iteration variable, si lo encuentra me va a regresar el valor, o le va a asignar valor de 0
#a ese valor le sumo 1 para ir haciendo la cuenta
#imprimo dic para ver todos los keys con sus values

#dic={"joe":1 , "churly":2, "mich":3}
#for i in dic:
#    print "el key es:", i, "el Value es:",dic[i]

#el for te trae de regreso el key por default, si quieres que traiga el label se lo tienes que pedir


#dic={"joe":1 , "churly":2, "mich":3}
#print list(dic) #para convertir el dic en lista / solo agarra los valores del key
#print dic.keys() #para jalar los keys del diccionario unicamente y convertirlos en lista
#print dic.values()#para jalar los values del diccionario unicamente y convertirlos en lista
#cuando jalas unicamente los keys o unicamente los values por separado / los dos se acomodan en el mismo orden / no sabes en que orden, solo sabes que es el mismo.
#print dic.items() #para jalar cada key y value como pareja, para todas las parejas del diccionario un "TUPLE"

#dic={"joe":1 , "churly":2, "mich":3}
#for i,j in dic.items():
#    print i,j
#puedes tener 2 iteration variables para los diccionarios convirtiendo el diccionario en una lista de parejas usando .items()


#name=raw_input("Enter the name of the file you want to read: ")
#file=open(name, "r")
#text=file.read()
#list=text.split()

#dic={}
#for i in list:
#    dic[i]=dic.get(i,0)+1

#bigcount = None
#bigword = None
#for k,v in dic.items():
#    if bigword is None or bigcount > v:
#        bigword=k
#        bigcount=v
#print bigword,bigcount

name=raw_input("enter file:")
handle=open(name,"r")
text=handle.read()   #estoy metiendo todo a una string
words=text.split()   #spliteo esa string para volverlo una lista

counts=dict()   #hago el diccionario
for word in words:  #hago un for para pasar por toda esa lista
    counts[word]=counts.get(word,0)+1  #busca el key value de la iteration variable, si encuentra el key value te regresa su valor. Si no lo encuentra le asigna el valor de 0.

bigcount=None 
bigword=None
for word,count in counts.items():  #for de 2 variables el key y el value, se llaman word y count para explicar mejor pero podrian ser a y b.
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print bigword,bigcount










    