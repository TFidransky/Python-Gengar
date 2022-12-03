import csv
from math import floor


def openCSV() -> []:
    file = open("vstup.csv", "r")
    reader = csv.reader(file)
    rows = []
    for row in reader:
        rows.append(row)

    return rows

def parseToWeeks(rows: []):
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

def calculateWeekAverage(week):
    amounts = []
    for day in week:
        amounts.append(float(day[3].strip()))

    return sum(amounts) / len(amounts)

def writeWeekToCsv(first_day, average):
    file = open('output.csv', 'a')
    writer = csv.writer(file)
    first_day[3] = '{0:.4f}'.format((floor(average*10000)/10000)).__str__()
    writer.writerow(first_day)

def main():
    rows_of_csv = openCSV()
    weeks = parseToWeeks(rows_of_csv)
    for week in weeks:
        writeWeekToCsv(week[0], calculateWeekAverage(week))

main()


