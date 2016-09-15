#6.5 Write code using find() and string slicing (see section 6.10) to extract the number
#at the end of the line below. Convert the extracted value to a floating point number and print it out.
#text = "X-DSPAM-Confidence:    0.8475";
#ftext=text.find(":")
#x=text[ftext+1:]
#print ftext
#print x
#print type (x)
#x=float(x)
#print x
#print type(x)

#fhand=open("texto.txt")
#count=0
#for i in fhand:
 #   count=count+1
  #  print i
   # print count
#print count

#handle=open("mbox-short.txt")
#for i in handle:
#    i=i.rstrip()
#    if i.startswith("From:"):
#       print i
   
#tambien puedes poner un if not
#if not i.startswith("From:"):
#       continue
#print i
    
#esto hace lo mismo pero al revez, dice si la linea no empieza c

#file=raw_input("Enter a File Name to Open:")
#try:
#    handle=open(file)
#except:
#    print "The file name does not exist"
#    exit()
#    
#for i in handle:
#    print i


#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
#fname=raw_input("Enter a File Name:")
#handle=open(fname)
#for i in handle:
#    i=i.rstrip()
#    print i.upper()
















