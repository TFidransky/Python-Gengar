# 2)
# Napiště program pro opačnou konverzi

dd = float(input("Zajdete stupně v desetinném formátu: "))

d = int(dd)
z = (dd - d) * 60
m = int(z)
y = (z - m) * 60
s = int(y)

print("Výsledek je", d, "stupňů,", m, "minut", "a", s, "sekund")