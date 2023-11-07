import re
from collections import Counter
import nltk
nltk.download('punkt')
from nltk.corpus import cmudict
nltk.download('cmudict')
cmudict = cmudict.dict()

# Funkcja do liczenia słów i zdań
def licz_slowa_zdania(tekst):
    zdania = nltk.sent_tokenize(tekst)
    slowa = re.findall(r'\w+', tekst)
    liczba_slow = len(slowa)
    liczba_zdan = len(zdania)
    liczba_cyfr = len(re.findall(r'\d', tekst))  # Liczba cyfr w tekście
    return liczba_slow, liczba_zdan, liczba_cyfr

# Funkcja do częstości występowania słów
def czestosc_slow(tekst):
    slowa = re.findall(r'\w+', tekst)
    slowa = [slowo.lower() for slowo in slowa]
    czestotliwosc = Counter(slowa)
    najczestsze_slowa = czestotliwosc.most_common(10)
    return najczestsze_slowa

# Funkcja do obliczania długości zdania bez spacji i znaków interpunkcyjnych
def dlugosc_zdania(tekst):
    return len(re.findall(r'\w', tekst))  # Liczba liter i cyfr w zdaniu

# Funkcja do obliczania statystyk tekstu
def statystyki_tekstu(tekst):
    zdania = nltk.sent_tokenize(tekst)
    slowa = re.findall(r'\w+', tekst)
    srednia_dl_zdan = sum(dlugosc_zdania(zdanie) for zdanie in zdania) / len(zdania)  # Średnia długość zdania bez spacji i interpunkcji
    srednia_liczba_slow = len(slowa) / len(zdania)
    return srednia_dl_zdan, srednia_liczba_slow

# Funkcja do wykrywania najdłuższego i najkrótszego zdania
def najdluzsze_najkrotsze_zdanie(tekst):
    zdania = nltk.sent_tokenize(tekst)
    zdania.sort(key=len)
    najkrotsze = zdania[0]
    najdluzsze = zdania[-1]
    return najkrotsze, najdluzsze

# Funkcja do analizy stopnia trudności tekstu
def stopien_trudnosci(tekst):
    zdania = nltk.sent_tokenize(tekst)
    slowa = re.findall(r'\w+', tekst)
    liczba_zdan = len(zdania)
    liczba_slow = len(slowa)
    liczba_sylab = sum([sum([1 for ph in pr if ph[-1].isdigit()]) for word in slowa for pr in cmudict.get(word.upper(), [[]])[0]])

    stopien_fk = 206.835 - 1.015 * (liczba_slow / liczba_zdan) - 84.6 * (liczba_sylab / liczba_slow)
    return stopien_fk

# Funkcja do wizualizacji wyników
def wizualizacja_wynikow(tekst, liczba_slow, liczba_zdan, liczba_cyfr, najczestsze_slowa, srednia_dl_zdan, srednia_liczba_slow, najkrotsze, najdluzsze, stopien_fk):
    print("Analiza tekstu:")
    print("Liczba słów:", liczba_slow)
    print("Liczba zdań:", liczba_zdan)
    print("Liczba cyfr:", liczba_cyfr)
    print("Najczęstsze słowa:")
    for slowo, ilosc in najczestsze_slowa:
        print(f"{slowo}: {ilosc}")
    print("Średnia długość zdania:", srednia_dl_zdan)
    print("Średnia liczba słów na zdanie:", srednia_liczba_slow)
    print("Najkrótsze zdanie:", najkrotsze)
    print("Najdłuższe zdanie:", najdluzsze)
    print("Stopień trudności tekstu (Flesch-Kincaid):", stopien_fk)

# Przykład użycia
tekst = "To jest przykłaodyw tekst."
ilosc_liter = len([znak for znak in tekst if znak.isalpha()])
print("Ilość liter w tekście:", ilosc_liter)

liczba_slow, liczba_zdan, liczba_cyfr = licz_slowa_zdania(tekst)
najczestsze_slowa = czestosc_slow(tekst)
srednia_dl_zdan, srednia_liczba_slow = statystyki_tekstu(tekst)
najkrotsze, najdluzsze = najdluzsze_najkrotsze_zdanie(tekst)
stopien_fk = stopien_trudnosci(tekst)
wizualizacja_wynikow(tekst, liczba_slow, liczba_zdan, liczba_cyfr, najczestsze_slowa, srednia_dl_zdan, srednia_liczba_slow, najkrotsze, najdluzsze, stopien_fk)
