#fruit="banana"
#index=0
#while index<len(fruit):
  #  letter=fruit[index]
 #   print index,letter
#    index=index+1

#fruit2="banana"
#for letter in fruit2:
 #   print letter
#for each letter in banana


#print len('banana')*7

#6.5 Write code using find() and string slicing (see section 6.10) to extract the number
#at the end of the line below. Convert the extracted value to a floating point number and
#print it out.

text = "X-DSPAM-Confidence:    0.8475";
x=text.find(":")
print text[x+1:]
num=float(text[x+1:])
print num
print type(num)
#declaro el texto como variable
#busco dentro del texto los :
#imprimo desde donde empiezan los : hasta el final solo para ver que va bien el codigo
#despues declaro otra variable para poder hacer ese texto un numero float
#lo multiplico por 2 para que se vea que si es numero, tambien se puede hacer con type

