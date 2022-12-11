# funkce, ač tady je možná mírně nadbytečná, vzhledem k délce kódu, nicméně takhle lze celá funkce přesunout do jiného programu
# nejdříve se vytvoří prázdný slovník, poté se spustí for cyklus, dlouhý podle délky inputu. Pokud už znak je někdy započítán, tak se přičte +1, pokud ne, tak se mu přidělí 1.
# To se provádí znovu do té doby, než se ukončí for cyklus (= dojede na konec inputu).
# char_freq je poté seřazeno podle četnosti znaků, pokud se "u" vyskytlo 4x a "b" 3x, tak "u" bude první, ač abecedně by bylo druhé
# poslední for cyklus tiskne znaky, opět dokud nevypíše všechny znaky co se objevily v inputu.
def print_char_freq(string):
  char_freq = {}

  for char in string:
    if char != " ":
      if char not in char_freq:
        char_freq[char] = 1
      else:
        char_freq[char] += 1

  char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

  for char, freq in char_freq:
    print(f"{char}: {freq}")

string = input("Zadeje větu, u které chcete zjistit frekvenci: ")
print_char_freq(string)
