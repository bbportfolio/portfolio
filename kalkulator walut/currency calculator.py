import requests

# Dictionary mapping currency codes to country names
currency_codes_and_names = {
       "AED": "United Arab Emirates",
    "AFN": "Afghanistan",
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Netherlands Antilles",
    "AOA": "Angola",
    "ARS": "Argentina",
    "AUD": "Australia",
    "AWG": "Aruba",
    "AZN": "Azerbaijan",
    "BAM": "Bosnia and Herzegovina",
    "BBD": "Barbados",
    "BDT": "Bangladesh",
    "BGN": "Bulgaria",
    "BHD": "Bahrain",
    "BIF": "Burundi",
    "BMD": "Bermuda",
    "BND": "Brunei",
    "BOB": "Bolivia",
    "BRL": "Brazil",
    "BSD": "Bahamas",
    "BTC": "Bitcoin",
    "BTN": "Bhutan",
    "BWP": "Botswana",
    "BYN": "Belarus",
    "BYR": "Belarus (obsolete)",
    "BZD": "Belize",
    "CAD": "Canada",
    "CDF": "Congo",
    "CHF": "Switzerland",
    "CLF": "Chile (unit of account)",
    "CLP": "Chile",
    "CNY": "China",
    "COP": "Colombia",
    "CRC": "Costa Rica",
    "CUC": "Cuba (exchange rate)",
    "CUP": "Cuba (unit of account)",
    "CVE": "Cape Verde",
    "CZK": "Czech Republic",
    "DJF": "Djibouti",
    "DKK": "Denmark",
    "DOP": "Dominican Republic",
    "DZD": "Algeria",
    "EGP": "Egypt",
    "ERN": "Eritrea",
    "ETB": "Ethiopia",
    "EUR": "Eurozone",
    "FJD": "Fiji",
    "FKP": "Falkland Islands (Malvinas)",
    "GBP": "United Kingdom",
    "GEL": "Georgia",
    "GGP": "Guernsey",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "Gambia",
    "GNF": "Guinea",
    "GTQ": "Guatemala",
    "GYD": "Guyana",
    "HKD": "Hong Kong",
    "HNL": "Honduras",
    "HRK": "Croatia",
    "HTG": "Haiti",
    "HUF": "Hungary",
    "IDR": "Indonesia",
    "ILS": "Israel",
    "IMP": "Isle of Man",
    "INR": "India",
    "IQD": "Iraq",
    "IRR": "Iran",
    "ISK": "Iceland",
    "JEP": "Jersey",
    "JMD": "Jamaica",
    "JOD": "Jordan",
    "JPY": "Japan",
    "KES": "Kenya",
    "KGS": "Kyrgyzstan",
    "KHR": "Cambodia",
    "KMF": "Comoros",
    "KPW": "North Korea",
    "KRW": "South Korea",
    "KWD": "Kuwait",
    "KYD": "Cayman Islands",
    "KZT": "Kazakhstan",
    "LAK": "Laos",
    "LBP": "Lebanon",
    "LKR": "Sri Lanka",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "LTL": "Lithuania",
    "LVL": "Latvia",
    "LYD": "Libya",
    "MAD": "Morocco",
    "MDL": "Moldova",
    "MGA": "Madagascar",
    "MKD": "North Macedonia",
    "MMK": "Myanmar (Burma)",
    "MNT": "Mongolia",
    "MOP": "Macau",
    "MRO": "Mauritania",
    "MUR": "Mauritius",
    "MVR": "Maldives",
    "MWK": "Malawi",
    "MXN": "Mexico",
    "MYR": "Malaysia",
    "MZN": "Mozambique",
    "NAD": "Namibia",
    "NGN": "Nigeria",
    "NIO": "Nicaragua",
    "NOK": "Norway",
    "NPR": "Nepal",
    "NZD": "New Zealand",
    "OMR": "Oman",
    "PAB": "Panama",
    "PEN": "Peru",
    "PGK": "Papua New Guinea",
    "PHP": "Philippines",
    "PKR": "Pakistan",
    "PLN": "Poland",
    "PYG": "Paraguay",
    "QAR": "Qatar",
    "RON": "Romania",
    "RSD": "Serbia",
    "RUB": "Russia",
    "RWF": "Rwanda",
    "SAR": "Saudi Arabia",
    "SBD": "Solomon Islands",
    "SCR": "Seychelles",
    "SDG": "Sudan",
    "SEK": "Sweden",
    "SGD": "Singapore",
    "SHP": "Saint Helena",
    "SLL": "Sierra Leone",
    "SOS": "Somalia",
    "SRD": "Suriname",
    "STD": "São Tomé and Príncipe",
    "SYP": "Syria",
    "SZL": "Eswatini",
    "THB": "Thailand",
    "TJS": "Tajikistan",
    "TMT": "Turkmenistan",
    "TND": "Tunisia",
    "TOP": "Tonga",
    "TRY": "Turkey",
    "TTD": "Trinidad and Tobago",
    "TWD": "Taiwan",
    "TZS": "Tanzania",
    "UAH": "Ukraine",
    "UGX": "Uganda",
    "USD": "United States",
    "UYU": "Uruguay",
    "UZS": "Uzbekistan",
    "VEF": "Venezuela",
    "VES": "Venezuela (unit of account)",
    "VND": "Vietnam",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XAF": "Central African CFA franc",
    "XAG": "Silver",
    "XAU": "Gold",
    "XCD": "East Caribbean Dollar",
    "XDR": "Special Drawing Rights",
    "XOF": "West African CFA franc",
    "XPF": "CFP Franc",
    "YER": "Yemen",
    "ZAR": "South Africa",
    "ZMK": "Zambian Kwacha (obsolete)",
    "ZMW": "Zambian Kwacha",
    "ZWL": "Zimbabwean Dollar (obsolete)"
}

def get_exchange_rates():
    url = "http://api.exchangeratesapi.io/v1/latest"
    access_key = "6bf2fae5319d24ff13e48f00a885ddfe" #paste here your API-KEY
    full_url = f"{url}?access_key={access_key}"

    try:
        response = requests.get(full_url)
        data = response.json()
        if "rates" in data:
            return data["rates"]
        else:
            print("Failed to fetch exchange rates.")
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def convert_currencies(rates, amount, from_currency, to_currency):
    if from_currency in rates and to_currency in rates:
        rate_from = rates[from_currency]
        rate_to = rates[to_currency]
        converted_amount = (amount / rate_from) * rate_to
        return converted_amount
    else:
        print("Currency rates not found. Please check if you provided correct currency codes.")
        return None

def main():
    while True:
        exchange_rates = get_exchange_rates()

        if exchange_rates:
            print("Available currencies:")
            for currency in exchange_rates:
                if currency in currency_codes_and_names:
                    country_name = currency_codes_and_names[currency]
                else:
                    country_name = "Unknown country"
                print(f"{currency} - {country_name}")

            from_currency = input("Enter the currency code you want to convert from: ").upper()
            to_currency = input("Enter the currency code you want to convert to: ").upper()
            amount = float(input("Enter the amount to convert: "))

            result = convert_currencies(exchange_rates, amount, from_currency, to_currency)

            if result:
                print(f"{amount} {from_currency} equals {result} {to_currency}")

            continuation = input("Do you want to continue (yes/no)? ").lower()
            if continuation != "yes":
                break

if __name__ == "__main__":
    main()
