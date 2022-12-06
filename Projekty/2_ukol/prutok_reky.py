import csv
import string
from math import floor
import copy

# otevírá soubor, poté to odchytává error, v případě, že tam je, tak to uživateli vyhodí hlášku do konzole
def openCSV() -> []: 
    file = None
    reader = None
    try:
        file = open("vstup.csv", "r")
        reader = csv.reader(file)
    except:
        print("Chyba pri načítání vstupu")

    rows = []  # prázdný list
    for row in reader:
        rows.append(row)

    file.close()

    return rows

# funkce rozdělí řádky na týdny (7 dní = týden), pokud poslední týden < 7 dní, tak to vezme taky jako týden, nehledě na délce
def parseToWeeks(rows: []):
    row_number = 0
    weeks = []

    #nacti cele tydny
    for number_of_week in range(0, floor(len(rows) / 7)):
        weeks.append([])
        for row_number in range(0, 7):
            weeks[number_of_week].append(rows[row_number])
            row_number = row_number + 1

    #nacti posledni tyden
    if row_number != len(rows):
        weeks.append([])
        for row_number in range(0, len(rows) - row_number):
            weeks[len(weeks) - 1].append(rows[row_number])

    return weeks # vrácení hodnot pro další výpočty

# rozděluje dataset na jednotlivé roky (=years). Nejdřív to vytáhne první rok, který v datasetu je, poté to porovnává s dalšími řádky.
# Dokud jsme ve stejném roce, tak to bude přiřazovat ke stejnému roku
# Jakmile se rok změní, tak se naše proměnná posune o 1 rok a začne znovu nabírat data pro tento rok.
def parseToYears(rows: []): # rozdělí to na jednotlivé roky (=years)
    year_idx = 0
    years = [[]]
    current_year = getYearFromDate(rows[0][2])

    for row in rows:
        if getYearFromDate(row[2]) == current_year:
            years[year_idx].append(row)
        else:
            current_year = getYearFromDate(row[2])
            year_idx = year_idx + 1
            years.append([])
            years[year_idx].append(row)

    return years

# splitne formát roku (v základu v datech formát dd.mm.rrrr, na další výpočet je potřeba převést na dd, mm, rrrr)
def getYearFromDate(date: string):
    dateSplit = date.split(".")
    return int(dateSplit[2])

# projede všechny dny v jednom týdnu, poté to vydělí počtem dnů v tomtéž týdnu
def calculatePeriodAverage(period):
    amounts = []  # průtoky hodnoty
    for day in period:
        amounts.append(float(day[3].strip()))

    return sum(amounts) / len(amounts) # vrací průměr za daný týden

# zápis nových řádků (průměry za týdny / roky) do CSV souborů ("vystup_7dni.csv" a "vystup_rok.csv")
def writePeriodToCsv(first_day, average, filename):
    file = open(filename, 'a')
    writer = csv.writer(file)
    dayToWrite = copy.deepcopy(first_day) # deepcopy slouží k tomu, aby to neměnilo původní proměnnou first_day
    dayToWrite[3] = '{0:.4f}'.format(average)
    writer.writerow(dayToWrite)

# zjišťuje minimální a maximální průtok, pak to vypíše do konzole - hodnota průtoku a datum, kdy k minimu / maximu došlo 
# dělá to na principu, že vezme hodnotu prvního dne (=řádku) v datasetu a potom srovnává druhý řádek. Pokud je hodnota 
# v druhém řádku větší / menší, tak nahradí hodnotu z prvního řádku a pak se další řádek srovnává s tímto. Takhle až do konce datasetu.
def min_max_prutok (rows):
    max_prutok = rows[0][-1]
    max_prutok_den = rows[0][-2]
    min_prutok = rows[0][-1]
    min_prutok_den = rows[0][-2]
    for day in rows:
        if day[-1] > max_prutok:
            max_prutok = day[-1]
            max_prutok_den = day[-2]
    for day in rows:
        if day[-1] < min_prutok:
            min_prutok = day[-1]
            min_prutok_den = day[-2]
    print(f" Nejnižší hodnota byla zaznamenána dne {min_prutok_den}, hodnota byla {min_prutok}.")
    print(f" Nejvyšší hodnota byla zaznamenána dne {max_prutok_den}, hodnota byla {max_prutok}.")
    
# projetí celého programu
def main():
    rows_of_csv = openCSV()
    weeks = parseToWeeks(rows_of_csv)
    years = parseToYears(rows_of_csv)
    min_max_prutok(rows_of_csv)
    for week in weeks:
        writePeriodToCsv(week[0], calculatePeriodAverage(week), 'vystup_7dni.csv')

    for year in years:
        writePeriodToCsv(year[0], calculatePeriodAverage(year), 'vystup_rok.csv')

main()
