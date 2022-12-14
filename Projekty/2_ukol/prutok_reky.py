import csv
import string
from math import floor
import copy
import os

# třída pro výjimku prázdného souboru. Chtěl jsem se vyhnout užití knihovny pandas, když není ve VS Code defaultně a musí se stáhnout
class EmptyFileException(Exception):
    def __init__(self, message):
        self.message = message

# otevírá soubor, poté to odchytává errory, v případě, že tam je, tak to uživateli vyhodí příslušnou hlášku do konzole
def open_csv() -> [str]:
    rows = []

    try:
        with open("vstup.csv", 'r') as f:
            reader = csv.reader(f, delimiter=",")

            if os.stat("vstup.csv").st_size == 0:
                raise EmptyFileException("Vstupní soubor je prázdný.")

            for row in reader:
                if len(row) < 4:
                    raise IndexError("Ve vstupním souboru je méně sloupců než se očekávalo.")
                try:
                    last_column = float(row[-1])
                except ValueError:
                    raise ValueError("Poslední sloupec není platné desetinné číslo.")
                rows.append(row)

    except EmptyFileException as EmptyFile:
        print(EmptyFile)
        exit(1)
    except FileNotFoundError:
        print("Vstupní soubor nebyl nalezen.")
        exit(1)
    except (ValueError, IndexError) as e:
        print(e)
        exit(1)

    return rows

# funkce rozdělí dataset na týdny (7 dní = týden), pokud počet dnů není dělitelný 7, tak to poslední hodnoty 
# (co se nevešly do posledního plného týdne (= dělitelného 7)) vezme jako nekompletní týden a dá ho jako týden o x dnech
def split_to_weeks(rows: []) -> [[str]]:
    final_idx = 0
    weeks = []

    # cele tydny
    for number_of_week in range(0, floor(len(rows) / 7)):
        week = []
        for row_number in range(0, 7):
            week.append(rows[final_idx])
            final_idx += 1
        weeks.append(week)

    # poslední (nekompletní, nemá 7 dní) týden
    if final_idx != len(rows):
        week = []
        for row_number in range(0, len(rows) - final_idx):
            week.append(rows[final_idx])
            final_idx += 1
        if len(week) > 0:
            weeks.append(week)
    return weeks

# rozděluje dataset na jednotlivé roky (=years). Nejdřív to vytáhne první rok, který v datasetu je, poté to porovnává s dalšími řádky.
# Dokud jsme ve stejném roce, tak to bude přiřazovat ke stejnému roku
# Jakmile se rok změní, tak se naše proměnná posune o 1 rok a začne znovu nabírat data pro tento rok.
def split_to_years(rows: []) -> [[str]]:  # rozdělí to na jednotlivé roky (=years)
    year_idx = 0
    years = [[]]
    current_year = get_year_from_date(rows[0][2])

    for row in rows:
        if get_year_from_date(row[2]) == current_year:
            years[year_idx].append(row)
        else:
            current_year = get_year_from_date(row[2])
            year_idx = year_idx + 1
            years.append([])
            years[year_idx].append(row)

    return years

# splitne formát roku (v základu v datech formát dd.mm.rrrr, na další výpočet je potřeba převést na dd, mm, rrrr)
def get_year_from_date(date: string):
    dateSplit = date.split(".")
    return int(dateSplit[2])

# projede všechny dny v jednom týdnu, poté to vydělí počtem dnů v tomtéž týdnu
def calculate_period_average(period):
    amounts = []  # průtoky hodnoty
    for day in period:
        amounts.append(float(day[3].strip()))

    return sum(amounts) / len(amounts)  # vrací průměr za daný týden

# zápis nových řádků (průměry za týdny / roky) do CSV souborů ("vystup_7dni.csv" a "vystup_rok.csv")
def write_period_to_csv(first_day, average, filename):
    with open(filename, 'a', encoding="utf-8", newline='') as fwrite:
        writer = csv.writer(fwrite)
        dayToWrite = copy.deepcopy(first_day)  # deepcopy slouží k tomu, aby to neměnilo původní proměnnou first_day
        dayToWrite[3] = '{0:.4f}'.format(average)
        writer.writerow(dayToWrite)

# zjišťuje minimální a maximální průtok, pak to vypíše do konzole - hodnota průtoku a datum, kdy k minimu / maximu došlo
# dělá to na principu, že vezme hodnotu prvního dne (=řádku) v datasetu a potom srovnává druhý řádek. Pokud je hodnota 
# v druhém řádku větší / menší, tak nahradí hodnotu z prvního řádku a pak se další řádek srovnává s tímto. Takhle až do konce datasetu.
def min_max_prutok(rows):
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
    rows_of_csv = open_csv()
    weeks = split_to_weeks(rows_of_csv)
    years = split_to_years(rows_of_csv)
    min_max_prutok(rows_of_csv)
    for week in weeks:
        write_period_to_csv(week[0], calculate_period_average(week), 'vystup_7dni.csv')
    for year in years:
        write_period_to_csv(year[0], calculate_period_average(year), 'vystup_rok.csv')

main()
