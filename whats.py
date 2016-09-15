listajoe=list()
listalili=list()
countjoe=0
countlili=0
count=0
#file=raw_input("Enter a file name: ")

text=open("chatli.txt")
for x in text:
    x=x.rstrip().split()
    count=count+1    
    if x[4]=="J.:":
        if "mujer" in x[5:]:
            listajoe.append(x)
            countjoe=countjoe+1
        else:
            continue        
    else:
        if "hey" in x[5:]:
            listalili.append(x)
            countlili=countlili+1

     #   for element in x:
      #      if element in listajoe: continue
       #     else:
        #        listajoe.append(element)
        #print words
#        print words[5:]
    #else: continue
        #print words[6:]
#print listajoe
#print listalili
#print "a ver"
print "joe dijo",countjoe, "veces"
print "Lili dijo",countlili, "veces"
print count
#print listajoe

