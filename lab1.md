<!-- class: center, middle, inverse -->

# Techniki Programowania Równoległego
## Lab 1

Prezentacja: [kfigiela.github.io/tpr_lab/lab1.html](http://kfigiela.github.io/tpr_lab/?lab1.md)

Wersja do czytania: [github.com/kfigiela/tpr_lab/blob/gh-pages/lab1.md](https://github.com/kfigiela/tpr_lab/blob/gh-pages/lab1.md)


---
# Plan na dziś

1. Uruchomienie Hello World!
    * Python
    * C
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
* Zespoły 3 osobowe:
  * 2 osoby implementują testy w C/Python,
  * testy powinny być przeprowadzone tą samą metodą (algorytm, liczba iteracji, zakres rozmiaru danych itp.),
  * trzecia osoba uruchamia kody pozostałych osób i przeprowadza testy na klastrze Zeus.
* **Sugestia:** Do rysowania wykresów można użyć [Gnuplot](http://www.gnuplot.info) lub [R](http://www.r-project.org)/[ggplot2](http://ggplot2.org).
* Podział na zespoły: [http://goo.gl/forms/K78G2elg4P](http://goo.gl/forms/K78G2elg4P)
<!-- * **Uwaga!** W C++/Boost dostępna jest tylko komunikacja standardowa i tylko taką można w tam przetestować.
  * Testy dla komunikacji standardowej.
  * Przetestować wbudowane w bibliotekę boost mechanizmy automatycznej serializacji standardowych struktur z STL (vector, map, string, etc.) - ocenić overhead serializacji dla typu `vector`.  -->


---
# Zadanie domowe – Zeus

1. Review kodu kolegów (czy metoda pomiarów jest taka sama).
1. Uruchomienie kodów na klastrze Zeus w różnych konfiguracjach 
   * 1 node fizyczny
   * 2 nody fizyczne – patrz `man mpiexec`
1. Przeprowadzenie pomiarów
1. Wygenerowanie wykresów
1. **Wnioski!**