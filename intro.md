<!-- class: center, middle, inverse -->

# Techniki Programowania Równoległego

Prezentacja: [kfigiela.github.io/mpi_lab/tutorial.html](http://kfigiela.github.io/mpi_lab/intro.html)

Wersja do czytania: [github.com/kfigiela/mpi_lab/blob/gh-pages/tutorial.md](https://github.com/kfigiela/mpi_lab/blob/gh-pages/intro.md)

---
<!-- class: middle -->

## ![Avatar](http://olorin.info/av/av120.jpg) mgr inż. Kamil Figiela

.right-column[

* 1 i 3 zajęcia 
* Preferowany kontakt mailowy: [kfigiela@agh.edu.pl](mailto:kfigiela@agh.edu.pl)
* Można mnie spoktać na forum
* Pokój 3.42

]

---
<!-- class: center, middle -->

# Konta na serwerze gandalf.icsr.agh.edu.pl

## Czy jest ktoś bez konta?

---
<!-- class: middle -->

# Moodle

* Kurs: Techniki programowania równoległego
* [http://upel.agh.edu.pl/wiet/course/view.php?id=3](http://upel.agh.edu.pl/wiet/course/view.php?id=3)
* Klucz do kursu: `TPR2014`

---
<!-- class: middle -->

# Organizacja zajęć

Wykład prowadzą:

* dr inż. Renata Słota (~10, ocena końcowa)
* dr inż. Witold Alda (5)

Zajęcia laboratoryjne prowadzą:

* Część 1 (blokowo)
  * dr inż. Renata Słota (1 zajęcia),
  * dr inż. Maciej Malawski (1 zajęcia),
  * dr inż. Włodzimierz Funika (1 zajęcia),
  * mgr inż. Kamil Figiela (2 zajęcia),
  * mgr inż. Michał Orzechowski (2 zajęcia).
* Część 2 (grupy) - ???

---
# Organizacja zajęć

* Wykład (egzamin):
  * egzamin zerowy ustny (~15–19 czerwca);
  * dopuszczenie do egz. zerowego przy zal. 4.5 i  5.0 z labów; grupa secjalna
  * termin I = test, terminy: II i III (poprawki) ustne
* Laboratorium (2/3 PR; 1/3 PR na GPU).
* Ocena końcowa: średnia z egz. i zal. z lab, ze wskazaniem na laby. + ewentualne promocje (0.5 do 1 oceny w górę)

* **Promocja**: referat na wykładzie wg tematu zaproponowanego przez RS lub, jeśli ciekawy, przez studenta (np. z prowadzonych  badań lub interesującego tematu; związek z TPR konieczny) (dostępne do wyczerpania zasobów); termin wygłoszenia referatu 5 maja
* Istnieje **grupa specjalna** laboratoryjna (ilość miejsc ograniczona do max 15); zajęcia w tej grupie są na zasadzie obowiązkowych,  indywidualnych konsultacji; nabór polega na zapisie do grupy wtorek 12.50 na własna opowiedzialność ;) ćwiczenie będzie polegać na realizacji programu równoległego z wykorzystaniem min. 2 technologii z 4: MPI, OpenMP, MapReduce, GPU; temat do uzgodnienia z RS; brak postępów na konsultacjach oznacza powrót na zajęcia grupowe na wynegocjowanych warunkach.


---

# Zasady oceniania części 1

* Punktacja pierwszych 9 spotkań (waga 2/3 do oceny z labów):
  * 8 ćwiczeń laboratoryjnych, na każdych do zdobycia:
    * 3 punkty za zadania z zajęć,
    * 2 punkty za aktywność;
  * 5 sprawozdań z zadań domowych, każde warte 10 punktów.
* Wszystkie sprawozdania są obowiązkowe.
* Łącznie można zdobyć 80 punktów.
* Za 100% tej części przyjmujemy 80 punktów, ze względu na uznaniowość aktywności.

---

# Zasady oceniania części 2 (GPU)

* Punktacja ostatnich 4 spotkań (waga 1/3 do oceny z labów):
  * 4 ćwiczeń laboratoryjnych, na każdych do zdobycia:
    * 3 punkty za zadania z zajęć,
    * 2 punkty za aktywność;
  * 2 sprawozdania z zadań domowych, każde warte 12 punktów.
* Wszystkie sprawozdania są obowiązkowe.
* Łącznie można zdobyć 44 punktów.
* Za 100% tej części przyjmujemy 40 punktów, ze względu na uznaniowość aktywności.

**Oceny wyliczane są zgodnie z regulaminem studiów, za 100% przyjmujemy 80+40=120 punktó**

---
# Tematyka zajęć

1. MPI: Podstawowe badania dotyczące opóźnienia i przepustowości - komunikacja typu punkt–punkt (spr. 1)
1. MPI: Komunikacja grupowa (spr. 2, odbiór spr. 1) 
1. MPI: Równoległość idealna + Badanie efektywności algorytmu cz.1 (spr. 3, odbiór spr. 2)
1. MPI: Typy pochodne, Mnożenie macierzy + Badanie efektywności algorytmu cz.2 (spr. 4)
1. OpenMP (odbiór spr. 3 i 4)
1. OpenMP (spr. 5) 
1. MapReduce
1. MapReduce (odbiór spr. 5)
1. Uzupełnienia zaległych sprawozdań  (tylko u RS): 11 do 15 maja dla cz. I labów
1. GPU (spr.1)
1. GPU (odbiór spr.1)
1. GPU (spr.2)
1. GPU (odbiór spr.2)
1. Uzupełnienia (u właściwego prowadzącego): 15-19 czerwca dla cz. II labów

---
# Plan na dziś

1. Uruchomienie Hello World!
    * Python
    * C
    * C++ i Boost
2. Prosta komunikacja w MPI
3. Pomiar czasu dla ping-pong
4. Aplikacje typu master-slave
5. Zadanie domowe

---
# Ćwiczenie 1
## Sposoby komunikacji

* Przetestuj rózne sposoby komunikacji P2P dostępne w MPI.
* Sposoby komunikacji [1]
  * Standard send `MPI_Send`
  * Synchronous send `MPI_Ssend`
  * Buffered send `MPI_Bsend`
  * Ready send `MPI_Rsend`
  * Non-blocking send `MPI_Isend` + `MPI_Wait`, `MPI_Test`
* Odbieranie danych `MPI_Recv`, `MPI_Irecv`
* **Jak działa komunikacja standardowa?**

.footnote[
[1] [http://www.dartmouth.edu/~rc/classes/intro_mpi/mpi_comm_modes.html](http://www.dartmouth.edu/~rc/classes/intro_mpi/mpi_comm_modes.html)
]


---
# Ćwiczenie 2
## Mierzenie opóźnień

* Zaimplementuj aplikację, gdzie 2 węzły wymieniają się komunikatami (ping–pong).
* Sprawdź zwykłą i buforowaną komunikację.
* Zmierz opóźnienie (przyda się funkcja `MPI_Wtime`).
* **W jaki sposób należy dokonać pomiaru?**

---
# Ćwiczenie 3
## „Token ring”

* Zaimplementuj aplikację, w której każdy node przesyła do kolejnego otrzymaną daną.
* Sprawdź zwykłą i synchroniczną komunikację.
* Jak poprzednio dokonaj pomiarów.

---
# Zadanie domowe

Celem zadania jest zmierzenie opóźnienia i przepustowości połączeń w klastrze. 

* Należy przetestować dwa różne typy komunikacji P2P w MPI.
* Należy dokonać pomiarów::
  * przepustowości [Mbit/s] od długości komunikatów [B]: wykres,
  * opóźnienia [ms] przesyłania krótkiego komunikatu: wartość. 
* Zespoły 4 osobowe:
  * 3 osoby implementują testy w C/C++/Python,
  * testy powinny być przeprowadzone tą samą metodą (liczba iteracji, zakres rozmiaru danych itp.),
  * czwarta osoba uruchamia kody pozostałych osób i przeprowadza testy na klastrze Zeus.
* **Uwaga!** W C++/Boost dostępna jest tylko komunikacja standardowa i tylko taką można w tam przetestować. 
  * Testy dla komunikacji standardowej.
  * Przetestować wbudowane w bibliotekę boost mechanizmy automatycznej serializacji standardowych struktur z STL (vector, map, string, etc.) - ocenić overhead serializacji dla typu `vector`. 
* **Sugestia:** Do rysowania wykresów można użyć [Gnuplot](http://www.gnuplot.info) lub [R](http://www.r-project.org).

???

Jeśli jest np. 13 osób – dopuszczamy zespoły 3 osobowe i pomijamy C++.

---
# Zadanie domowe – Zeus

1. Review kodu kolegów (czy metoda pomiarów jest taka sama).
1. Uruchomienie kodów na klastrze Zeus w różnych konfiguracjach 
   * 1 node fizyczny
   * 2 nody fizyczne – patrz `man mpiexec`
1. Przeprowadzenie pomiarów
1. Wygenerowanie wykresów
1. **Wnioski!**

---
# Zasady oceniania zadania

* Sprawozdania są indywidualne!
* Sprawozdanie części I labów stanowią:
  * wykresy,
  * kod programu,
  * wyniki pomiarów,
  * wiedza/komentarz/odpowiedź na pytania.
* Nic nie drukujemy, nie trzeba tworzyć dokumentu sprawozdania, ale warto zrobić notatki z wnioskami.
* Wykresy bez podpisanych osi i bez dodatkowych informacji nie będą przyjmowane
* Punktacja:
  * 2 punkty za poprawny kod i jego znajomość,
  * 2 punkty za poprawne wykresy i ich omówienie,
  * 2 punkty za poprawne wyniki,
  * 4 punkty za odpowiedź na pytania teoretyczne z danego zagadnienia.

---

# Konta na serwerach Cyfronetu/PLGrid/Zeus

1. http://plgrid.pl › Rejestracja
2. Należy podać:
    * Typ: Użytkownik
    * Opiekun: Renata Słota
    * Nr OPI opiekuna: 93749
    * Nasz typ OPI: podopieczny
    * Temat badań: AGH. Techniki Programowania Równoległego
3. Po aktywacji konta na [http://portal.plgrid.pl/](http://portal.plgrid.pl/) należy aktywować:
    * Dostęp do UI - Cyfronet
    * Dostęp do klastra ZEUS
3. `ssh login@ui.cyfronet.pl`
4. HowTo: [https://docs.cyfronet.pl/display/PLGDoc/Dokumentacja+PL-Grid](https://docs.cyfronet.pl/display/PLGDoc/Dokumentacja+PL-Grid)