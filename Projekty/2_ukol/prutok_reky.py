import csv
from math import floor

def openCSV() -> []:
    #try block
    file = open("vstup.csv", "r")
    reader = csv.reader(file)
    rows = []
    for row in reader:
        rows.append(row)
    return rows

def parseToWeeks(rows: []): #rozdělí to po 7 dnech (=týdny), weeks je [] 
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

def calculateWeekAverage(week): #projede všechny dny v týdnu, poté vydělí počtem dnů (zatím fixně 7)
    amounts = [] #průtoky
    for day in week:
        amounts.append(float(day[3].strip()))

    return sum(amounts) / len(amounts)

def writeWeekToCsv(first_day, average):
    file = open('vystup_7dni.csv', 'a') 
    writer = csv.writer(file)
    first_day[3] = '{0:.4f}'.format((floor(average*10000)/10000)).__str__() 
    writer.writerow(first_day)
    file.close()



def min_max (rows):
    max = rows[0][-1]
    max_day = rows[0][-2]
    min = rows[0][-1]
    min_day = rows[0][-2]
    for day in rows:
        if day[-1] > max:
            max = day[-1]
            max_day = day[-2]
    for day in rows:
        if day[-1] < min:
            min = day[-1]
            min_day = day[-2]
    print(f" Nejnižší hodnota byla zaznamenána dne {min_day}, hodnota byla {min}.")
    print(f" Nejvyšší hodnota byla zaznamenána dne {max_day}, hodnota byla {max}.")
    

def main():
    rows_of_csv = openCSV()
    weeks = parseToWeeks(rows_of_csv)
    min_max(rows_of_csv)
    for week in weeks:
        writeWeekToCsv(week[0], calculateWeekAverage(week))


main()
