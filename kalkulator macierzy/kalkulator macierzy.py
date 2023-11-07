import numpy as np

def wczytaj_macierz():
    try:
        wiersze = int(input("Podaj liczbę wierszy macierzy: "))
        kolumny = int(input("Podaj liczbę kolumn macierzy: "))
        print("Wprowadź elementy macierzy (oddzielone spacją lub enterem):")
        macierz = []
        for _ in range(wiersze):
            wiersz = list(map(float, input().split()))
            if len(wiersz) != kolumny:
                print("Błąd: Liczba elementów w wierszu nie zgadza się z liczbą kolumn.")
                return None
            macierz.append(wiersz)
        return np.array(macierz)
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłowe dane.")
        return None

def oblicz_wyznacznik(macierz):
    if macierz.shape[0] == macierz.shape[1]:
        return np.linalg.det(macierz)
    else:
        print("Błąd: Wyznacznik można obliczyć tylko dla macierzy kwadratowej.")
        return None

def dodawanie_macierzy(macierz_a, macierz_b):
    if macierz_a.shape == macierz_b.shape:
        return macierz_a + macierz_b
    else:
        print("Błąd: Macierze muszą mieć takie same rozmiary.")
        return None

def odejmowanie_macierzy(macierz_a, macierz_b):
    if macierz_a.shape == macierz_b.shape:
        return macierz_a - macierz_b
    else:
        print("Błąd: Macierze muszą mieć takie same rozmiary.")
        return None

def mnozenie_macierzy(macierz_a, macierz_b):
    if macierz_a.shape[1] == macierz_b.shape[0]:
        return np.dot(macierz_a, macierz_b)
    else:
        print("Błąd: Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")
        return None

def wyswietl_macierz(macierz):
    if macierz is not None:
        print(macierz)

if __name__ == "__main__":
    while True:
        print("Kalkulator macierzy")

        macierz_a = wczytaj_macierz()

        if macierz_a is not None:
            while True:
                print("Wybierz operację:")
                print("1. Dodawanie macierzy")
                print("2. Odejmowanie macierzy")
                print("3. Mnożenie macierzy")
                print("4. Obliczanie wyznacznika macierzy")
                print("5. Wyjście")

                wybor = input("Twój wybór: ")

                if wybor == "1":
                    macierz_b = wczytaj_macierz()
                    if macierz_b is not None:
                        suma = dodawanie_macierzy(macierz_a, macierz_b)
                        if suma is not None:
                            print("Suma macierzy:")
                            wyswietl_macierz(suma)
                elif wybor == "2":
                    macierz_b = wczytaj_macierz()
                    if macierz_b is not None:
                        roznica = odejmowanie_macierzy(macierz_a, macierz_b)
                        if roznica is not None:
                            print("Różnica macierzy:")
                            wyswietl_macierz(roznica)
                elif wybor == "3":
                    macierz_b = wczytaj_macierz()
                    if macierz_b is not None:
                        iloczyn = mnozenie_macierzy(macierz_a, macierz_b)
                        if iloczyn is not None:
                            print("Iloczyn macierzy:")
                            wyswietl_macierz(iloczyn)
                elif wybor == "4":
                    wyznacznik = oblicz_wyznacznik(macierz_a)
                    if wyznacznik is not None:
                        print("Wyznacznik macierzy:")
                        print(wyznacznik)
                elif wybor == "5":
                    break
                else:
                    print("Błąd: Nieprawidłowy wybór operacji.")

            kontynuacja = input("Czy chcesz kontynuować (tak/nie)? ").lower()
            if kontynuacja != "tak":
                break
