# 1) 
# Napište program, který převede formát DMS na stupně
#Program se uživatele zeptá na D, M, S a vypíše desetinné stupně

from math import degrees


d = float(input("Zadejte stupně: "))
m = float(input("Zadejte minuty: "))
s = float(input("Zadejte vteřiny: "))

dd = d + m/60 + s/3600
print("Vysledek je ", dd, "stupňů")

