#7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt

#fname=raw_input("Enter a file name:")
#fhand=open(fname)
#for line in fhand:
  #  line=line.upper()
   # line=line.rstrip()
    #print line


#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below.

fname=raw_input("Enter a file name:")
fhand=open(fname)
count=0
sum=0
for line in fhand:
    line=line.rstrip()
    if 'X-DSPAM-Confidence:' in line:
        count=count+1
        largo=line.find(':')
        #print largo (aqui lo que hice ver es cuanto vale "largo" para saber en que caracter empieza lo que estoy buscando)
        search=line[(largo+1):]
        #aqui le digo que me traiga el dato empezando desde "largo" : "" hasta que acabe
        x=float(search)
        sum=sum+x

#print sum
#print count
print sum/count