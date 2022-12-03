import csv
from datetime import datetime

def openCSV():
    with open ("vstup.csv", encoding = "utf-8", newline="") as f:
        rows = csv.reader(f, delimiter = ",")
        for row in rows:
            rok = row [-4]
            mesic = row [-3]
            den = row [-2]
            prutok = row[-1]    

        
#def kontrola():
#    try:
        
#def vypocet7(reader):
#    with open("vystup_7dni.csv","w", encoding = "utf-8", newline="") as f7:

  

#def vypocet365(reader):
#    with open("vystup_rok.csv", "w", encoding = "utf-8", newline="") as f365:

openCSV()

