c = input("Geben Sie Ihren Namen ein: ")
print("Herzlich Wilkommen " + c ) 
a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))


if b == 0:
    
    print("Zahl 1 = 0!")
    print("geben Sie eine neue Zahl für b ein (=ungleich 0)")
    a = int(input("Zahl 1: "))
    b = int(input("Zahl 2: "))
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
    
else:
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
 








