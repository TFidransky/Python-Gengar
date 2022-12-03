from turtle import forward, exitonclick, right, left, speed
# a = float(input("Zadejte hodnotu strany šestiúhelníku: "))
# for cyklus <proměnná> in <sekvence>: ;; v odsazeném bloku o řádek níže se pak opakuje podle toho kolikrát dáme sekvenci
# for i in range(6):
#    forward(a)
#    left(60)
# exitonclick()

#a = float(input("Zadejte délku sloupce a: "))
#b = float(input("Zadejte délku řádku b: "))
a = 4
b = 3

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
        
exitonclick()    

