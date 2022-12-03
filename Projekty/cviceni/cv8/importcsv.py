import csv

#1. Pro každé parkoviště vypište jméno a kapacitu
with open ("parkoviste.csv", encoding = "utf-8", newline="") as f:
    reader = csv.reader (f, delimiter = ";")
    next(reader)
    for row in reader:
        print(row[0],",",row[-1])

#2. Spočtěte celkovou kapacitu parkovišť
with open ("parkoviste.csv", encoding = "utf-8", newline="") as f:
    reader = csv.reader (f, delimiter = ";")
    next(reader)
    celk = 0
    for row in reader:
        celk += int(row[-1])
    print("Kapacita všech parkovišť je", celk)
    
#3. Spočtěte celkovou kapacitu P+R parkovišť
with open ("parkoviste.csv", encoding = "utf-8", newline="") as f:
    reader = csv.reader (f, delimiter = ";")
    next(reader)
    celk = 0
    for row in reader:
        if row[3] == "TRUE":
            celk += int(row[-1])
        elif row[3] == "FALSE":
            celk += 0
    print("Kapacita P+R parkovišť je", celk)

#4. Uložte P+R parkoviště do souboru pr.csv tak, že budou obsahovat sloupce "name" a "totalNumOfPlaces"
with open ("parkoviste.csv", encoding = "utf-8", newline="") as f, open ("pr.csv", "w", encoding = "utf-8", newline="") as fout:
    reader = csv.reader(f, delimiter=";")
    next(reader)

    writer = csv.writer(fout)
    for row in reader:
        if row[3] == "TRUE":
            writer.writerow([row[0], row[-1]])
        elif row[3] == "FALSE":
            pass