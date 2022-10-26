from math import sqrt
from turtle import forward, right, left, exitonclick, speed, penup, pendown, circle

speed(9)

#velikost hracího pole
a = int(input("Zadejte šířku hracího pole (=množství sloupců): "))
b = int(input("Zadejte výšku hracího pole (=množství řádků): "))


#vykreslení hracího pole - čtverec
for y in range(b):
    for x in range (a):
        for i in range (4):
            forward (50)
            left(90)
        forward(50)
    right(180)
    forward(a*50)
    right(90)
    forward(50)
    right(90)
#vrácení na [0,0] pozici        
right(90)
forward(50*b)
left(90)

while True: 
    c = int(input("Hráč 1, zadejte x-ovou souřadnici: "))
    d = int(input("Hráč 1, nyní zadejte y-ovou souřadnici: "))
    forward((50*c)-50)
    left(90)
    forward((50*d)-50)
    right(90)
    #křížek z [0,0]
    left(45)
    forward((sqrt(5000)))
    right(135)
    forward(50)
    right(135)
    forward((sqrt(5000)))
    #vrácení na [0,0]
    left(135)
    forward(50*d)
    right(90)
    forward((50*c)-50)
    right(180)
    c = int(input("Hráč 2, nyní zadejte X-ovou souřadnici: "))
    d = int(input("Hráč 2, nyní zadejte y-ovou souřadnici: "))
    #kolečko z [0,0]
    forward((50*c)-50)
    left(90)
    forward((50*d)-50)
    right(90)
    forward(25)
    circle(25)
    left(180)
    forward(25+(50*c)-50)
    left(90)
    forward((50*d)-50)
    left(90)

exitonclick()