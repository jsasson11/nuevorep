#strings no se pueden alterar
#   fruit="Banana"
#   fruit[0]=b
#listas si se pueden alterar
#fruits=["Banana", "BAN", "Carrot"]
#print fruits
#x=raw_input("Dame otra fruta para quitar BAN:")
#fruits[1]=x
#print fruits
#____________________

#el len() de una lista regresa los elementos que estan dentro de la lista
#el len() de una string regresa los caracteres o espacios que hay dentro del string
#si vas a modificar una lista, la funcion range() te puede ayudar
#range crea una lista con los espacios que tu le pidas con el parametro
#range(4) te hace una lista de [0,1,2,3] hasta el 4 sin incluirlo

#friends=["Joseph", "Glenn", "Sally"]
#print len(friends)
#>>>>3
#print range(len(friends))
#>>>>[0,1,2]
#______________

#friends=["Joseph", "Glenn", "Sally"]
#for i in friends:
#    print "Hello", i
    
#for i in range(len(friends)):
#    friend=friends[i]
#    print "Hello", friend

#los dos imprimen lo mismo, uno lo hace directo y el otro hace una lista con los subindices de friends
#despues le dice que la iteracion en la que se encuentre la iguale a friend
#y ya despues imprime friend

#_______________________

#puedes concatenar listas con +
#amigos=["Juan", "Jose", "Gerardo"]
#y=amigos + friends
#print y
#tambien puedes recortar las listas como si fueran strings
#x=y[1:3]
#print x
#tambien puedes decirle "sort yourself"
#print amigos
#amigos.sort()
#la lista ya se altero y ya se quedo con ese nuevo orden
#________________________

#listanum=[1,2,3,4,5,6,4332,4534,232323,3422,-1]
#print listanum
#print len(listanum)
#print max(listanum)
#print min(listanum)
#print sum(listanum)
#print sum(listanum) / len(listanum)

#______________hay dos formas de construir una lista y hacer operaciones con ella, es mas facil hacerlo con listas
#total=0
#count=0
#while True:
#    num=raw_input("Enter a Number: ")
#    if num =="done": break
#    num=float(num)
#    total=num+total
#    count=count+1
#average=total/count
#print "Average", average

#acuerdate que la lista guarda los numeros en el ram, entonces si hay una gran cantidad va a ocupar espacio mientras que el otro solo va a ir haciendo calculos
#es mas poderosa la lista porque puedo hacer mas operaciones como max min sort etc con la lista y programarlo es mas sencillo
#numlist=list()
#while True:
#    input=raw_input("Enter a number:")
#    if input=="done": break
#    input=float(input)
#    numlist.append(input)
#average=sum(numlist)/len(numlist)
#print average

#split
#agarra una string como abc="mi mail es joseph@kosmos.la y el tuyo" y la convierte en una lista de 7 elementos
#abc= "mi mail es joseph@kosmos.la y el tuyo"
#lista=abc.split()
#print lista
# ["mi","mail","es","joseph@kosmos.la", "y", "el", "tuyo"]
#imaginate que quieres sacar unicamente le dominio
#lo que harias es hacer otro split
#mail=lista[3]
#dominio=mail.split("@")
#print dominio[1]
#kosmos.la


#Open the file romeo.txt and read it line by line. For each line, split the line into a list
#of words using the split() method. The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append
#it to the list. When the program completes, sort and print the resulting words in alphabetical order.

#text=open("romeo.txt")
#list2=list()

#for line in text:
#    line=line.rstrip()
#    list=line.split()
   
#    for word in list:
#        if word in list2:
#            continue
#        else:
#            list2.append(word)
#list2.sort()
#print list2

#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

fhand=open("mbox-short.txt")
count=0
for i in fhand:
    i=i.rstrip()
    if i .startswith("From "):
        fromm=i.split()
        print fromm[1]
        count=count+1
    else:
        continue
print count

































