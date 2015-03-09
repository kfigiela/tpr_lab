<!-- class: center, middle, inverse -->

# Techniki Programowania Równoległego

Prezentacja: [kfigiela.github.io/tpr_lab/?intro.md](http://kfigiela.github.io/tpr_lab/?intro.md)

Wersja do czytania: [github.com/kfigiela/tpr_lab/blob/gh-pages/intro.md](https://github.com/kfigiela/tpr_lab/blob/gh-pages/intro.md)

---
<!-- class: middle -->

## ![Avatar](http://olorin.info/av/av120.jpg) mgr inż. Kamil Figiela

* 1 i 3 zajęcia 
* Preferowany kontakt mailowy: [kfigiela@agh.edu.pl](mailto:kfigiela@agh.edu.pl)
* Można mnie spoktać na forum
* Pokój 3.42

---
<!-- class: center, middle -->

# Konta na serwerze gandalf.icsr.agh.edu.pl

## Czy jest ktoś bez konta?

---
<!-- class: middle -->

# Moodle

* Kurs: Techniki programowania równoległego
* [http://upel.agh.edu.pl/wiet/course/view.php?id=3](http://upel.agh.edu.pl/wiet/course/view.php?id=3)
* Klucz do kursu: `(pon|wt|sr|czw|pt)-(8|9|11|12)-TPR2015`

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

**Zasady te są opublikowane na [Moodle](http://upel.agh.edu.pl/wiet/pluginfile.php/13641/mod_resource/content/1/zasady-2015.pdf) i to jest wiążący dokument.**

---
# Tematyka zajęć

1. **MPI:** Podstawowe badania dotyczące opóźnienia i przepustowości – komunikacja typu punkt–punkt (spr. 1)
1. **MPI:** Komunikacja grupowa (spr. 2, odbiór spr. 1) 
1. **MPI:** Równoległość idealna + Badanie efektywności algorytmu cz.1 (spr. 3, odbiór spr. 2)
1. **MPI:** Typy pochodne, Mnożenie macierzy + Badanie efektywności algorytmu cz.2 (spr. 4)
1. **OpenMP** (odbiór spr. 3 i 4)
1. **OpenMP** (spr. 5) 
1. **MapReduce**
1. **MapReduce** (odbiór spr. 5)
1. Uzupełnienia zaległych sprawozdań  (tylko u RS): 11 do 15 maja dla cz. I labów
1. **GPU** (spr. 1)
1. **GPU** (odbiór spr. 1)
1. **GPU** (spr. 2)
1. **GPU** (odbiór spr. 2)
1. Uzupełnienia (u właściwego prowadzącego): 15-19 czerwca dla cz. II labów

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

<!-- ---

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
4. HowTo: [https://docs.cyfronet.pl/display/PLGDoc/Dokumentacja+PL-Grid](https://docs.cyfronet.pl/display/PLGDoc/Dokumentacja+PL-Grid) -->