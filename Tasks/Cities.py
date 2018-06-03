n=input ("Enter city name with capital letter: ")
a=("Almaty", "Astana", "Kyzylorda")
b=("Taraz", "Oskemen", "Kokshetau")
c=("Oral", "Atyrau", "Aktobe")
if n in a:
         print (n+ " is South of Kazakhstan")
elif n in b:
         print (n+ " is North of Kazakhstan")
elif n in c:
         print (n+ " is West of Kazakhstan")
else:
         print ("it is not city from Kazakhstan")
