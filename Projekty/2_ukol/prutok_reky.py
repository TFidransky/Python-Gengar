import csv
import string
from math import floor
import copy


def openCSV() -> []:
    file = None
    reader = None
    try:
        file = open("vstup.csv", "r")
        reader = csv.reader(file)
    except:
        print("Chyba pri nacitani vstupu")

    rows = []  # prázdný list
    for row in reader:
        rows.append(row)

    file.close()

    return rows


def parseToWeeks(rows: []):  # rozdělí to po 7 dnech (=týdny), weeks je []
    i = 0
    weeks = []

    #nacti cele tydny
    for number_of_week in range(0, floor(len(rows) / 7)):
        weeks.append([])
        for day in range(0, 7):
            weeks[number_of_week].append(rows[i])
            i = i + 1

    #nacti posledni tyden
    if i != len(weeks):
        weeks.append([])
        for day in range(0, len(rows) - i):
            weeks[len(weeks) - 1].append(rows[i])

    return weeks

def parseToYears(rows: []):
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

def getYearFromDate(date: string):
    dateSplit = date.split(".")
    return int(dateSplit[2])

def calculatePeriodAverage(period):  # projede všechny dny v týdnu, poté vydělí počtem dnů v daném týdnu
    amounts = []  # průtoky
    for day in period:
        amounts.append(float(day[3].strip()))

    return sum(amounts) / len(amounts)

def writePeriodToCsv(first_day, average, filename):
    file = open(filename, 'a')
    writer = csv.writer(file)
    dayToWrite = copy.deepcopy(first_day)
    dayToWrite[3] = '{0:.4f}'.format(average)
    writer.writerow(dayToWrite)

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
