import random
pytania_i_odpowiedzi = [
    {
        "pytanie": "Ile wynosi liczba e do potęgi pi i pomnożona przez pierwiastek z dwóch?",
        "odpowiedzi": ["1 12.34", "2 7.78", "3 6.28"],
        "poprawna_odpowiedz": "3"
    },
    {
        "pytanie": "Która z cząsteczek ma największą masę wodoru, helu i azotu?",
        "odpowiedzi": ["1 H2", "2 He", "3 N2"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Jak nazywa się najwyższy szczyt w systemie górskim Himalaje?",
        "odpowiedzi": ["1 Mount Everest", "2 K2", "3 Mont Blanc"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Który filozof napisal 'Krytykę czystego rozumu'?",
        "odpowiedzi": ["1 Georg Wilhelm Friedrich Hegel", "2 Immanuel Kant", "3 Friedrich Nietzsche"],
        "poprawna_odpowiedz": "2"
    },
    {
        "pytanie": "Ile wynosi 2 do potęgi 10?",
        "odpowiedzi": ["1 1024", "2 100", "3 20"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Który rok uważany jest za początek okresu renesansu w historii sztuki?",
        "odpowiedzi": ["1 14 wiek", "2 15 wiek", "3 16 wiek"],
        "poprawna_odpowiedz": "2"
    },
    {
        "pytanie": "Który z elementów chemicznych jest najlżejszy?",
        "odpowiedzi": ["1 Wodór", "2 Hel", "3 Lit"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Który kompozytor jest autorem 'Czarodziejskiego fletu'?",
        "odpowiedzi": ["1 Ludwig van Beethoven", "2 Wolfgang Amadeus Mozart", "3 Johann Sebastian Bach"],
        "poprawna_odpowiedz": "2"
    },
    {
        "pytanie": "Jaki termin określa ilość ciepła potrzebną do podniesienia temperatury jednego grama wody o jeden stopień Celsjusza?",
        "odpowiedzi": ["1 Kaloria", "2 Kilojoule", "3 Dekalitry"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Który z instrumentów muzycznych jest związany z Ericem Claptonem i Jimim Hendrixem?",
        "odpowiedzi": ["1 Gitara basowa", "2 Trąbka", "3 Gitara elektryczna"],
        "poprawna_odpowiedz": "3"
    },
    {
        "pytanie": "Co to jest równanie Schrodingera?",
        "odpowiedzi": ["1 Równanie różniczkowe", "2 Równanie falowe", "3 Równanie kwantowe"],
        "poprawna_odpowiedz": "3"
    },
    {
        "pytanie": "Jaka jest wartość liczby pi (π) do stu miejsc po przecinku?",
        "odpowiedzi": ["1 3.1415926535", "2 3.1415926539", "3 3.1415926541"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Kto jest autorem trylogii 'Władca Pierścieni'?",
        "odpowiedzi": ["1 George R.R. Martin", "2 J.R.R. Tolkien", "3 C.S. Lewis"],
        "poprawna_odpowiedz": "2"
    },
    {
        "pytanie": "Który fizyk odkrył pierwszy antyproton?",
        "odpowiedzi": ["1 Niels Bohr", "2 Paul Dirac", "3 Emilio Segrè"],
        "poprawna_odpowiedz": "3"
    },
    {
        "pytanie": "Który kraj jest uważany za kolebkę sztuki renesansu?",
        "odpowiedzi": ["1 Włochy", "2 Francja", "3 Hiszpania"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Który naukowiec stworzył teorię względności?",
        "odpowiedzi": ["1 Isaac Newton", "2 Albert Einstein", "3 Stephen Hawking"],
        "poprawna_odpowiedz": "2"
    },
    {
        "pytanie": "Ile wynosi przyspieszenie ziemskie na powierzchni planety?",
        "odpowiedzi": ["1 5 m/s^2", "2 9.8 m/s^2", "3 12.5 m/s^2"],
        "poprawna_odpowiedz": "2"
    },
    {
        "pytanie": "Kto napisał sztukę 'Hamlet'?",
        "odpowiedzi": ["1 William Shakespeare", "2 Christopher Marlowe", "3 Samuel Beckett"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Jaka jest najwyższa góra w systemie górskim Andów?",
        "odpowiedzi": ["1 Aconcagua", "2 K2", "3 Mont Blanc"],
        "poprawna_odpowiedz": "1"
    },
    {
        "pytanie": "Który malarz jest autorem 'Mony Lisy'?",
        "odpowiedzi": ["1 Leonardo da Vinci", "2 Vincent van Gogh", "3 Pablo Picasso"],
        "poprawna_odpowiedz": "1"
    },
    {
"pytanie": "Jaka jest stolica Brazylii?",
"odpowiedzi": ["1. São Paulo", "2. Rio de Janeiro", "3. Brasília", "4. Salvador"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Które państwo jest najmniejsze pod względem powierzchni?",
"odpowiedzi": ["1. Rosja", "2. Kanada", "3. Monako", "4. Australia"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Kto jest autorem 'Romea i Julii'?",
"odpowiedzi": ["1. Charles Dickens", "2. Jane Austen", "3. William Shakespeare", "4. Fyodor Dostoevsky"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Ile wynosi pierwiastek kwadratowy z liczby 144?",
"odpowiedzi": ["1. 12", "2. 14", "3. 16", "4. 18"],
"poprawna_odpowiedz": 1
},
{
"pytanie": "Który pierwiastek chemiczny ma symbol 'H'?",
"odpowiedzi": ["1. Węgiel", "2. Miedź", "3. Wodór", "4. Złoto"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Co oznacza skrót 'HTML'?",
"odpowiedzi": ["1. Hyper Text Markup Language", "2. High Tech Multi-Level", "3. Home Tool Management Lingo", "4. Hyper Transfer Markup Loop"],
"poprawna_odpowiedz": 1
},
{
"pytanie": "Który kontynent jest największy pod względem powierzchni?",
"odpowiedzi": ["1. Ameryka Północna", "2. Azja", "3. Afryka", "4. Australia"],
"poprawna_odpowiedz": 2
},
{
"pytanie": "W którym roku miała miejsce Bitwa pod Grunwaldem?",
"odpowiedzi": ["1. 1410", "2. 1487", "3. 1598", "4. 1325"],
"poprawna_odpowiedz": 1
},
{
"pytanie": "Co oznacza skrót 'DNA'?",
"odpowiedzi": ["1. Dynamic New Age", "2. Deoxyribonucleic Acid", "3. Digital Network Association", "4. Dual Neural Application"],
"poprawna_odpowiedz": 2
},
{
"pytanie": "Które państwo posiada najdłuższą linię brzegową na świecie?",
"odpowiedzi": ["1. Australia", "2. Kanada", "3. Brazylia", "4. Rosja"],
"poprawna_odpowiedz": 4
},
{
"pytanie": "Kto jest autorem powieści 'Zdobywcy świata'?",
"odpowiedzi": ["1. Leo Tolstoy", "2. Gabriel García Márquez", "3. Salman Rushdie", "4. Czesław Miłosz"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Ile wynosi liczba Pi (π) w przybliżeniu?",
"odpowiedzi": ["1. 2.718", "2. 3.142", "3. 1.618", "4. 1.732"],
"poprawna_odpowiedz": 2
},
{
"pytanie": "Kto jest autorem malarstwa 'Mona Lisa'?",
"odpowiedzi": ["1. Pablo Picasso", "2. Vincent van Gogh", "3. Leonardo da Vinci", "4. Claude Monet"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Jaki gaz stanowi około 78% składu atmosfery ziemi?",
"odpowiedzi": ["1. Hel", "2. Tlen", "3. Azot", "4. Argon"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Która z planet układu słonecznego jest najbliższa słońcu?",
"odpowiedzi": ["1. Mars", "2. Wenus", "3. Jowisz", "4. Uran"],
"poprawna_odpowiedz": 2
},
{
"pytanie": "W którym roku odbyła się pierwsza wyprawa człowieka na Księżyc?",
"odpowiedzi": ["1. 1969", "2. 1975", "3. 1982", "4. 1990"],
"poprawna_odpowiedz": 1
},
{
"pytanie": "Który kraj jest największym producentem kawy na świecie?",
"odpowiedzi": ["1. Kolumbia", "2. Brazylia", "3. Etiopia", "4. Indie"],
"poprawna_odpowiedz": 2
},
{
"pytanie": "Co oznacza skrót 'UNESCO'?",
"odpowiedzi": ["1. United Nations Educational, Scientific, and Cultural Organization", "2. Universal Science and Culture Entity Organization", "3. Union of Science and Culture Education Operations", "4. United Nations and Culture Educational Society Organization"],
"poprawna_odpowiedz": 1
},
{
"pytanie": "Który pierwiastek chemiczny ma symbol 'Na'?",
"odpowiedzi": ["1. Neon", "2. Nikiel", "3. Sód", "4. Nikel"],
"poprawna_odpowiedz": 3
},
{
"pytanie": "Które państwo posiada najwięcej ludności na świecie?",
"odpowiedzi": ["1. Stany Zjednoczone", "2. Chiny", "3. Indie", "4. Brazylia"],
"poprawna_odpowiedz": 2
},
    {
        "pytanie": "Który z tych matematyków jest znany z twierdzenia znaczonego jego nazwiskiem, które jest jednym z fundamentów rachunku?",
        "odpowiedzi": ["1. René Descartes", "2. Pierre-Simon Laplace", "3. Johann Bernoulli", "4. Pierre de Fermat"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Ile wynosi pierwiastek z liczby 16?",
        "odpowiedzi": ["1. 2", "2. 4", "3. 8", "4. 16"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Kto napisał utwór 'Zbrodnia i kara'?",
        "odpowiedzi": ["1. Leo Tolstoy", "2. Fyodor Dostoevsky", "3. Gustave Flaubert", "4. James Joyce"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Ile wynosi przekątna kwadratu o boku długości 5 cm?",
        "odpowiedzi": ["1. 10 cm", "2. 5 cm", "3. 7.07 cm", "4. 2.5 cm"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który pierwiastek chemiczny ma symbol 'H'?",
        "odpowiedzi": ["1. Hel", "2. Hydron", "3. Wodór", "4. Neon"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Które z państw Afryki graniczy z Marokiem?",
        "odpowiedzi": ["1. Algieria", "2. Libia", "3. Mauretania", "4. Egipt"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który z tych wynalazców jest znany z wynalezienia żarówki?",
        "odpowiedzi": ["1. Thomas Edison", "2. Alexander Graham Bell", "3. Nikola Tesla", "4. Albert Einstein"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Które z państw nie jest członkiem Unii Europejskiej?",
        "odpowiedzi": ["1. Francja", "2. Norwegia", "3. Niemcy", "4. Włochy"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Ile wynosi 2 do potęgi 10?",
        "odpowiedzi": ["1. 10", "2. 20", "3. 100", "4. 1024"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Który z elementów układu słonecznego jest największy?",
        "odpowiedzi": ["1. Księżyc", "2. Wenus", "3. Ziemia", "4. Słońce"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Który kraj jest największym producentem kawy na świecie?",
        "odpowiedzi": ["1. Brazylia", "2. Wietnam", "3. Kolumbia", "4. Indie"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który z tych języków jest uważany za język miłości?",
        "odpowiedzi": ["1. Niemiecki", "2. Francuski", "3. Chiński", "4. Angielski"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Która planeta jest znana jako 'Planeta Czerwona'?",
        "odpowiedzi": ["1. Wenus", "2. Mars", "3. Jowisz", "4. Saturn"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Która z tych oper to dzieło Giuseppe Verdiego?",
        "odpowiedzi": ["1. Carmen", "2. La Traviata", "3. Rigoletto", "4. Tosca"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który pierwiastek chemiczny ma symbol 'Au'?",
        "odpowiedzi": ["1. Srebro", "2. Złoto", "3. Platyna", "4. Cyna"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "W którym roku wybuchła II wojna światowa?",
        "odpowiedzi": ["1. 1939", "2. 1941", "3. 1945", "4. 1947"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Która z planet jest najbliższa Ziemi?",
        "odpowiedzi": ["1. Wenus", "2. Mars", "3. Jowisz", "4. Saturn"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Jak nazywa się największy kontynent na Ziemi?",
        "odpowiedzi": ["1. Europa", "2. Ameryka Południowa", "3. Azja", "4. Australia"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który kolor pojawia się na fladze Włoch?",
        "odpowiedzi": ["1. Zielony", "2. Czerwony", "3. Biały", "4. Niebieski"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Która planeta jest znana jako 'Planeta Ziemia'?",
        "odpowiedzi": ["1. Mars", "2. Jowisz", "3. Wenus", "4. Ziemia"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Ile wynosi pierwiastek kwadratowy z liczby 144?",
        "odpowiedzi": ["1. 9", "2. 12", "3. 15", "4. 16"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Która z tych konstelacji jest znana jako 'Wielki Wóz'?",
        "odpowiedzi": ["1. Orzeł", "2. Ryby", "3. Wielki Wóz", "4. Skorpion"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który metal jest znany jako 'Cieśla ze Srebrem'?",
        "odpowiedzi": ["1. Cynk", "2. Miedź", "3. Srebro", "4. Ołów"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Która z rzek jest najdłuższą rzeką na świecie?",
        "odpowiedzi": ["1. Nil", "2. Amazonka", "3. Missisipi", "4. Jangcy"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Które z tych państw nie jest członkiem Unii Europejskiej?",
        "odpowiedzi": ["1. Francja", "2. Niemcy", "3. Włochy", "4. Norwegia"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Który z tych filmów jest dziełem Stanleya Kubricka?",
        "odpowiedzi": ["1. Forrest Gump", "2. Casablanca", "3. Skazani na Shawshank", "4. 2001: Odyseja kosmiczna"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Która z tych państwowych flag jest czerwono-biała?",
        "odpowiedzi": ["1. Polska", "2. Niemcy", "3. Włochy", "4. Wielka Brytania"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Która z tych oper to dzieło Giacomo Pucciniego?",
        "odpowiedzi": ["1. Traviata", "2. Rigoletto", "3. Madama Butterfly", "4. Don Giovanni"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Ile wynosi liczba Avogadra?",
        "odpowiedzi": ["1. 6.02 x 10^23", "2. 3.14", "3. 42", "4. 9.81"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Ile wynosi pierwiastek z liczby 225?",
        "odpowiedzi": ["1. 15", "2. 17", "3. 20", "4. 18"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który pierwiastek chemiczny ma symbol 'Na'?",
        "odpowiedzi": ["1. Wodór", "2. Węgiel", "3. Sód", "4. Ksygen"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Która z planet układu słonecznego jest najbliższa Słońcu?",
        "odpowiedzi": ["1. Wenus", "2. Mars", "3. Jowisz", "4. Uran"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Kto jest autorem powieści 'Złodziejka książek'?",
        "odpowiedzi": ["1. Stephen King", "2. J.K. Rowling", "3. Markus Zusak", "4. George Orwell"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Ile wynosi przyspieszenie ziemskie?",
        "odpowiedzi": ["1. 5.67 m/s^2", "2. 9.81 m/s^2", "3. 12.34 m/s^2", "4. 7.89 m/s^2"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Kto jest autorem obrazu 'Mona Lisa'?",
        "odpowiedzi": ["1. Vincent van Gogh", "2. Leonardo da Vinci", "3. Pablo Picasso", "4. Rembrandt"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Ile stron ma Biblia?",
        "odpowiedzi": ["1. 1000", "2. 1500", "3. 2000", "4. 3000"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który kraj jest największym producentem herbaty na świecie?",
        "odpowiedzi": ["1. Chiny", "2. Indie", "3. Sri Lanka", "4. Japonia"],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Która z planet jest znana jako 'Planeta Czerwona'?",
        "odpowiedzi": ["1. Mars", "2. Wenus", "3. Jowisz", "4. Uran"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Która z tych państwowych flag ma kolor zielony?",
        "odpowiedzi": ["1. Włochy", "2. Kanada", "3. Brazylia", "4. Australia"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Które z państw sąsiaduje z Polską na zachodzie?",
        "odpowiedzi": ["1. Niemcy", "2. Czechy", "3. Ukraina", "4. Słowacja"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Jaki pierwiastek chemiczny ma najwyższą liczbę atomową?",
        "odpowiedzi": ["1. Wodór", "2. Hel", "3. Urządzenie", "4. Uran"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "W którym roku wybuchła I wojna światowa?",
        "odpowiedzi": ["1. 1914", "2. 1917", "3. 1919", "4. 1921"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Która z tych planet jest najmniejsza?",
        "odpowiedzi": ["1. Merkury", "2. Wenus", "3. Mars", "4. Ziemia"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który z wynalazków jest przypisywany Thomasowi Edisonowi?",
        "odpowiedzi": ["1. Telewizja", "2. Telefon", "3. Żarówka", "4. Samochód"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Kto jest autorem powieści 'Zabić drozda'?",
        "odpowiedzi": ["1. George Orwell", "2. John Steinbeck", "3. Harper Lee", "4. F. Scott Fitzgerald"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Która z rzek jest najdłuższa na świecie?",
        "odpowiedzi": ["1. Nil", "2. Amazonka", "3. Missisipi", "4. Jenisej"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Które z tych zwierząt jest gadem?",
        "odpowiedzi": ["1. Rekin", "2. Delfin", "3. Krokodyl", "4. Wieloryb"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Które z tych państw jest najmniejsze pod względem powierzchni?",
        "odpowiedzi": ["1. Rosja", "2. Kanada", "3. Monako", "4. Australia"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który z tych filmów wyreżyserował Quentin Tarantino?",
        "odpowiedzi": ["1. Avatar", "2. Pulp Fiction", "3. Incepcja", "4. E.T."],
        "poprawna_odpowiedz": 2
    },
    {
        "pytanie": "Który pierwiastek chemiczny ma symbol 'H'?",
        "odpowiedzi": ["1. Węgiel", "2. Hel", "3. Wodór", "4. Azot"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który z tych kompozytorów jest znany z tworzenia symfonii i sonat na fortepian solo?",
        "odpowiedzi": ["1. Johann Sebastian Bach", "2. Wolfgang Amadeus Mozart", "3. Ludwig van Beethoven", "4. Franz Schubert"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Która z planet jest najbliżej Słońca?",
        "odpowiedzi": ["1. Wenus", "2. Mars", "3. Jowisz", "4. Saturn"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który kraj jest największym producentem kawy na świecie?",
        "odpowiedzi": ["1. Brazylia", "2. Kolumbia", "3. Wietnam", "4. Indie"],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który z tych naukowców jest znany z teorii względności?",
        "odpowiedzi": ["1. Isaac Newton", "2. Galileo Galilei", "3. Albert Einstein", "4. Johannes Kepler"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Który z tych filmów zdobył Oscara za najlepszy film w 1994 roku?",
        "odpowiedzi": ["1. Forrest Gump", "2. Pulp Fiction", "3. Incepcja", "4. E.T."],
        "poprawna_odpowiedz": 1
    },
    {
        "pytanie": "Który z tych oceanów jest największy?",
        "odpowiedzi": ["1. Ocean Indyjski", "2. Ocean Arktyczny", "3. Ocean Spokojny", "4. Ocean Atlantycki"],
        "poprawna_odpowiedz": 3
    },
    {
        "pytanie": "Która z tych roślin jest rośliną jednoroczną?",
        "odpowiedzi": ["1. Tulipan", "2. Róża", "3. Paproć", "4. Marchewka"],
        "poprawna_odpowiedz": 4
    },
    {
        "pytanie": "Który z tych wynalazków jest przypisywany Alexanderowi Grahamowi Bellowi?",
        "odpowiedzi": ["1. Telewizja", "2. Telefon", "3. Żarówka", "4. Samochód"],
        "poprawna_odpowiedz": 2
    }
    # Dodaj tutaj pozostałe trudne pytania z odpowiedziami
]


random.shuffle(pytania_i_odpowiedzi)

# Funkcja do przeprowadzania quizu
def przeprowadz_quiz(pytania_i_odpowiedzi):
    punkty = 0

    for pytanie_i_odpowiedzi in pytania_i_odpowiedzi:
        print(pytanie_i_odpowiedzi["pytanie"])
        for odpowiedz in pytanie_i_odpowiedzi["odpowiedzi"]:
            print(odpowiedz)
        odpowiedz = input("Wybierz numer poprawnej odpowiedzi: ")
        if odpowiedz == pytanie_i_odpowiedzi["poprawna_odpowiedz"]:
            print("Poprawna odpowiedź!")
            punkty += 1
        else:
            print(f"Błędna odpowiedź. Poprawna odpowiedź to: {pytanie_i_odpowiedzi['odpowiedzi'][int(pytanie_i_odpowiedzi['poprawna_odpowiedz']) - 1][3:]}")

    print(f"Twój wynik to {punkty}/{len(pytania_i_odpowiedzi)}.")

# Wywołanie funkcji przeprowadz_quiz
przeprowadz_quiz(pytania_i_odpowiedzi)
