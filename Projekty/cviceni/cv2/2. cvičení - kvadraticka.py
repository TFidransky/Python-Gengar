# Program, který najde kořeny kvadratické rovnice; koeficienty josu a, b, c
# Program vypíše:
# - rovnice má kořeny <x1>, <x2>
# - rovnice má dvojnásobný kořen <x>
# - rovnice nemá v R řešení
from math import sqrt

a = input("Zadej koeficient u x^2: ")
#print *(repr(a))
a = float(a)
b = float(input("Zadej koeficient u x: "))
c = float(input("Zadej konstantni clen: "))

D = b*b - 4*a*c

if D < 0:
    print("Rovnice nema reseni")

elif D == 0:
    x = -b/(2*a)
    print("Rovnice ma prave jedno reseni", x)
else:
    x1 = -b+sqrt(D)/(2*a)
    x2 = -b-sqrt(D)/(2*a)
    print("Rovnice ma dve reseni", x1, x2)


