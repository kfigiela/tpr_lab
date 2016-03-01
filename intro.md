<!-- class: center, middle, inverse -->

# Techniki Programowania Równoległego

Prezentacja: [kfigiela.github.io/tpr_lab/?intro.md](http://kfigiela.github.io/tpr_lab/?intro.md)

Wersja do czytania: [github.com/kfigiela/tpr_lab/blob/gh-pages/intro.md](https://github.com/kfigiela/tpr_lab/blob/gh-pages/intro.md)

---
<!-- class: middle -->

## ![Avatar](https://avatars3.githubusercontent.com/u/174118?v=3&s=120) mgr inż. Kamil Figiela

* Preferowany kontakt mailowy: [kfigiela@agh.edu.pl](mailto:kfigiela@agh.edu.pl)

---
<!-- class: center, middle -->

# Konta na serwerze gandalf.icsr.agh.edu.pl

## Czy jest ktoś bez konta?

---
<!-- class: middle -->

# Moodle

* Kurs: Techniki programowania równoległego
* [http://upel.agh.edu.pl/wiet/course/view.php?id=277](http://upel.agh.edu.pl/wiet/course/view.php?id=277)
* Klucz do kursu: `TPR2016-(wt|cz)(11|12|17|19)`


---
# Organizacja zajęć

* Wykład (egzamin):
  * egzamin zerowy ustny (~6–10 czerwca);
  * dopuszczenie do egz. zerowego przy zal. 4.5 i 5.0 z labów i uzyskanie tej oceny przed terminem zerowym,
  * termin I = test, terminy: II i III (poprawki) ustne
* Laboratorium (~2/3 PR; ~1/3 PR na GPU).
* Ocena końcowa: średnia z egz. i zal. z lab, ze wskazaniem na laby. + ewentualne promocje (0.5 do 1 oceny w górę)

* **Promocja**: referat na wykładzie wg tematu zaproponowanego przez RS lub, jeśli ciekawy, przez studenta (np. z prowadzonych  badań lub interesującego tematu; związek z TPR konieczny) (dostępne do wyczerpania zasobów); termin wygłoszenia referatu 25 kwietnia
* Istnieje możliwość wykorzystania promocji do podniesienia oceny z labów, co może dać wejście na zerówkę
* Istnieje możliwość, że oddający sprawozdania w "awaryjnych" terminach nie będą mogli podejść do zerówki.


---

# Zasady oceniania części 1

* Punktacja pierwszych 9 spotkań (waga ~2/3 do oceny z labów):
  * 8 ćwiczeń laboratoryjnych, na każdych do zdobycia:
    * 3 punkty za zadania z zajęć,
    * 2 punkty za aktywność;
  * 4 sprawozdania z zadań domowych, każde warte 10 punktów.
* Wszystkie sprawozdania są obowiązkowe.
* Łącznie można zdobyć 80 punktów.
* Za 100% tej części przyjmujemy 72 punktów, ze względu na uznaniowość aktywności.

---

# Zasady oceniania części 2 (GPU)

* Punktacja ostatnich 3 spotkań (waga ~1/3 do oceny z labów):
  * 3 ćwiczeń laboratoryjnych, na każdych do zdobycia:
    * 3 punkty za zadania z zajęć,
    * 2 punkty za aktywność;
  * 2 sprawozdania z zadań domowych, każde warte 10 punktów.
* Wszystkie sprawozdania są obowiązkowe.
* Łącznie można zdobyć 35 punktów.
* Za 100% tej części przyjmujemy 31 punktów, ze względu na uznaniowość aktywności.

**Oceny wyliczane są zgodnie z regulaminem studiów, za 100% przyjmujemy 72+31=103 punktów.**

**Zasady te są opublikowane na [Moodle](http://upel.agh.edu.pl/wiet/course/view.php?id=277) i to jest wiążący dokument.**

---
# Tematyka zajęć

1. **MPI (mgr inż. Kamil Figiela):** Podstawowe badania dotyczące opóźnienia i przepustowości – komunikacja typu punkt–punkt (spr. 1)
1. **MPI (dr inż. Włodzimierz Funika):** Komunikacja grupowa (odbiór spr. 1)
1. **MPI (dr inż. Dariusz Król):** Równoległość idealna, Scalarm (spr. 2)
1. **MPI (mgr inż. Łukasz Opioła):** Typy pochodne, Mnożenie macierzy (spr. 3)
1. **OpenMP (dr inż. Renata Słota)** (odbiór spr. 2 i 3)
1. **OpenMP (dr inż. Renata Słota)** (spr. 4)
1. **MapReduce (dr inż. Dariusz Król)**
1. **MapReduce (dr inż. Dariusz Król)** (odbiór spr. 4)
1. Uzupełnienia zaległych sprawozdań  (tylko u RS): 5 i 10 maja dla cz. I labów
1. **GPU (I. Gawlik)** (spr. 1)
1. **GPU (dr inż. Paweł Topa)** (odbiór spr. 1, spr 2.)
1. **GPU (I. Gawlik)** (odbiór spr. 2)
1. Uzupełnienia (u właściwego prowadzącego): 6 czerwca dla cz. II labów

---
# Zasady oceniania zadania

* Sprawozdania są indywidualne!
* Sprawozdanie części I labów stanowią:
  * wykresy,
  * kod programu,
  * wyniki pomiarów,
  * wiedza/komentarz/odpowiedź na pytania.
* Nic nie drukujemy, nie trzeba tworzyć dokumentu sprawozdania, ale warto zrobić notatki z wnioskami.
* **☠️☠️☠️ Wykresy bez podpisanych osi i bez dodatkowych informacji nie będą przyjmowane ☠️☠️☠️**
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
