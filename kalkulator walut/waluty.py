import requests

# Słownik przypisujący kody walut do nazw krajów
kody_i_nazwy = {
    "AED": "Zjednoczone Emiraty Arabskie",
    "AFN": "Afganistan",
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Antyle Holenderskie",
    "AOA": "Angola",
    "ARS": "Argentyna",
    "AUD": "Australia",
    "AWG": "Aruba",
    "AZN": "Azerbejdżan",
    "BAM": "Bośnia i Hercegowina",
    "BBD": "Barbados",
    "BDT": "Bangladesz",
    "BGN": "Bułgaria",
    "BHD": "Bahrajn",
    "BIF": "Burundi",
    "BMD": "Bermudy",
    "BND": "Brunei",
    "BOB": "Boliwia",
    "BRL": "Brazylia",
    "BSD": "Bahamy",
    "BTC": "Bitcoin",
    "BTN": "Bhutan",
    "BWP": "Botswana",
    "BYN": "Białoruś",
    "BYR": "Białoruś (przestarzały)",
    "BZD": "Belize",
    "CAD": "Kanada",
    "CDF": "Kongo",
    "CHF": "Szwajcaria",
    "CLF": "Chili (jednostka rozrachunkowa)",
    "CLP": "Chile",
    "CNY": "Chiny",
    "COP": "Kolumbia",
    "CRC": "Kostaryka",
    "CUC": "Kuba (kurs wymiany)",
    "CUP": "Kuba (jednostka rozrachunkowa)",
    "CVE": "Republika Zielonego Przylądka",
    "CZK": "Czechy",
    "DJF": "Dżibuti",
    "DKK": "Dania",
    "DOP": "Dominikana",
    "DZD": "Algieria",
    "EGP": "Egipt",
    "ERN": "Erytrea",
    "ETB": "Etiopia",
    "EUR": "Unia Europejska",
    "FJD": "Fidżi",
    "FKP": "Falklandy (Malwiny)",
    "GBP": "Wielka Brytania",
    "GEL": "Gruzja",
    "GGP": "Guernsey",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "Gambia",
    "GNF": "Gwinea",
    "GTQ": "Gwatemala",
    "GYD": "Gujana",
    "HKD": "Hongkong",
    "HNL": "Honduras",
    "HRK": "Chorwacja",
    "HTG": "Haiti",
    "HUF": "Węgry",
    "IDR": "Indonezja",
    "ILS": "Izrael",
    "IMP": "Wyspa Man",
    "INR": "Indie",
    "IQD": "Irak",
    "IRR": "Iran",
    "ISK": "Islandia",
    "JEP": "Jersey",
    "JMD": "Jamajka",
    "JOD": "Jordania",
    "JPY": "Japonia",
    "KES": "Kenia",
    "KGS": "Kirgistan",
    "KHR": "Kambodża",
    "KMF": "Komory",
    "KPW": "Korea Północna",
    "KRW": "Korea Południowa",
    "KWD": "Kuwejt",
    "KYD": "Kajmany",
    "KZT": "Kazachstan",
    "LAK": "Laos",
    "LBP": "Liban",
    "LKR": "Sri Lanka",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "LTL": "Litwa",
    "LVL": "Łotwa",
    "LYD": "Libia",
    "MAD": "Maroko",
    "MDL": "Mołdawia",
    "MGA": "Madagaskar",
    "MKD": "Macedonia",
    "MMK": "Mjanma (Birma)",
    "MNT": "Mongolia",
    "MOP": "Makau",
    "MRO": "Mauretania",
    "MUR": "Mauritius",
    "MVR": "Malediwy",
    "MWK": "Malawi",
    "MXN": "Meksyk",
    "MYR": "Malezja",
    "MZN": "Mozambik",
    "NAD": "Namibia",
    "NGN": "Nigeria",
    "NIO": "Nikaragua",
    "NOK": "Norwegia",
    "NPR": "Nepal",
    "NZD": "Nowa Zelandia",
    "OMR": "Oman",
    "PAB": "Panama",
    "PEN": "Peru",
    "PGK": "Papua-Nowa Gwinea",
    "PHP": "Filipiny",
    "PKR": "Pakistan",
    "PLN": "Polska",
    "PYG": "Paragwaj",
    "QAR": "Katar",
    "RON": "Rumunia",
    "RSD": "Serbia",
    "RUB": "Rosja",
    "RWF": "Rwanda",
    "SAR": "Arabia Saudyjska",
    "SBD": "Wyspy Salomona",
    "SCR": "Seszele",
    "SDG": "Sudan",
    "SEK": "Szwecja",
    "SGD": "Singapur",
    "SHP": "Święta Helena",
    "SLL": "Sierra Leone",
    "SOS": "Somalia",
    "SRD": "Surinam",
    "STD": "Wyspy Świętego Tomasza i Książęca",
    "SYP": "Syria",
    "SZL": "Eswatini",
    "THB": "Tajlandia",
    "TJS": "Tadżykistan",
    "TMT": "Turkmenistan",
    "TND": "Tunezja",
    "TOP": "Tonga",
    "TRY": "Turcja",
    "TTD": "Trynidad i Tobago",
    "TWD": "Tajwan",
    "TZS": "Tanzania",
    "UAH": "Ukraina",
    "UGX": "Uganda",
    "USD": "Stany Zjednoczone",
    "UYU": "Urugwaj",
    "UZS": "Uzbekistan",
    "VEF": "Wenezuela",
    "VES": "Wenezuela (jednostka rozrachunkowa)",
    "VND": "Wietnam",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XAF": "Afryka Środkowa",
    "XAG": "Srebro",
    "XAU": "Złoto",
    "XCD": "Wschodni Karaiby",
    "XDR": "Specjalne Prawa Ciągnienia",
    "XOF": "Afryka Zachodnia",
    "XPF": "Polinezja Francuska",
    "YER": "Jemen",
    "ZAR": "Republika Południowej Afryki",
    "ZMK": "Kwacha zambijska (przestarzały)",
    "ZMW": "Kwacha zambijska",
    "ZWL": "Dolar Zimbabwe (przestarzały)",
}


def pobierz_kursy_walut():
    url = "http://api.exchangeratesapi.io/v1/latest"
    access_key = "6bf2fae5319d24ff13e48f00a885ddfe" #wklej tu swój klucz API
    full_url = f"{url}?access_key={access_key}"
    
    try:
        response = requests.get(full_url)
        data = response.json()
        if "rates" in data:
            return data["rates"]
        else:
            print("Nie udało się pobrać kursów walut.")
            return None
    except Exception as e:
        print("Wystąpił błąd:", e)
        return None

def przelicz_waluty(kursy, kwota, waluta_z, waluta_na):
    if waluta_z in kursy and waluta_na in kursy:
        kurs_z = kursy[waluta_z]
        kurs_na = kursy[waluta_na]
        przeliczona_kwota = (kwota / kurs_z) * kurs_na
        return przeliczona_kwota
    else:
        print("Nie znaleziono kursów walut. Sprawdź, czy podałeś poprawne kody walut.")
        return None

def main():
    while True:
        kursy_walut = pobierz_kursy_walut()
        
        if kursy_walut:
            print("Dostępne waluty:")
            for waluta in kursy_walut:
                if waluta in kody_i_nazwy:
                    nazwa_kraju = kody_i_nazwy[waluta]
                else:
                    nazwa_kraju = "Nieznany kraj"
                print(f"{waluta} - {nazwa_kraju}")
            
            waluta_z = input("Podaj kod waluty, którą chcesz wymienić: ").upper()
            waluta_na = input("Podaj kod waluty, na którą chcesz wymienić: ").upper()
            kwota = float(input("Podaj kwotę do wymiany: "))
            
            wynik = przelicz_waluty(kursy_walut, kwota, waluta_z, waluta_na)
            
            if wynik:
                print(f"{kwota} {waluta_z} to {wynik} {waluta_na}")
            
            kontynuacja = input("Czy chcesz kontynuować (tak/nie)? ").lower()
            if kontynuacja != "tak":
                break

if __name__ == "__main__":
    main()
