import csv
from datetime import datetime


def openCSV():
    with open ("vstup.csv", encoding = "utf-8", newline="") as f:
        reader = csv.reader(f, delimiter = ",")


#def kontrola():
#    try:

#def vypocet():
#    celk = 0

#def pocitej7():
#    with open("vystup_7dni.csv","w", encoding = "utf-8", newline="") as f7:

#def pocitej365():
#    with open("vystup_rok.csv", "w", encoding = "utf-8", newline="") as f365:

openCSV()
