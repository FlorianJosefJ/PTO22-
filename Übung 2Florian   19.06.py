a=["eins","zwei","drei","vier"]
b=["one","two","three","four"]

wort=input("Gib ein wort an: ")
j=4
for i in range(0,3):
    if a[i]==wort:
        j=i
print(b[j])

               