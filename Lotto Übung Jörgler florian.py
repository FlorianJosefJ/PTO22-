#----Jörgler Florian-----

import random #Liabary für Zufalls Zahl einfügen

b = 0 #variable hier vergeben
zahl =[]


int_t = int(input("Bitte geben Sie folgend ein, wie viele Tipps sie abgeben möchten: ")) 



if int_t <=5: 
    while b <int_t:
        x = random.randint(1,45)#random zahl zwischen 1 und 45
        if x in zahl: #wenn x in in zahl schon vorhanden vorgang wiederholen
            b = b  
        else:
            zahl.append(x)
            b+=1

    print("Ihre zufälligen Zahlen sind: ", zahl)

else:
    print("Maximal 5 Tipps!")