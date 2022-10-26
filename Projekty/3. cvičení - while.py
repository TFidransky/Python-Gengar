# while <výraz>:
#   blok; dokud je výraz platný, tak se blok opakuje

#while True:
#    print("Ahoj")

#vstup = input("Zadej x")
#while vstup != "x":
#    vstup = input("Zadej x")

# HRA, program si náhodně zvolí číslo a vyzve uživatele, aby to číslo uhádnul.
# Pokud uživatel číslo uhodne, tak mu program pogratuluje, jinak mu řekne jestli je tip vyšší nebo nižší než vybrané číslo
from random import randint  #randint bude vyhazovat náhodné číslo v rozmezí co mu určíme

a = randint(1,100)
b = int(input("Hledáte náhodně zvolené číslo mezi 1 a 100. Zvolte číslo, které si myslíte, že to je: "))
while a != b:
    if b < a:
        print("Vámi zvolené číslo je menší než hádané číslo")
        b = int(input("Zadejte jiné, větší číslo mezi 1 a 100: "))
    
    elif b > a:
        print("Vámi zvolené číslo je větší než hádané číslo")
        b = int(input("Zadejte jiné, menší číslo mezi 1 a 100: "))

print("Gratulujeme, vybrali jste vhodné číslo!")