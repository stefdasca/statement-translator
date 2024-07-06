Roboțelul Nino a primit cadou un dispozitiv care inscripționează bile. Dispozitivul poate fi încărcat cu $n$ bile, ce vor fi inscripționate în ordine, cu numerele $1, 2, \dots, n$.

Nino trebuie să împartă bilele inscripționate în două șiruri, $X$ și $Y$, astfel:

* La primul pas Nino va pune în primul șir bila cu numărul $1$ ($X_1 = 1$), iar în al doilea șir bila cu numărul $2$ ($Y_1 = 2$).
* La al doilea pas Nino va pune în primul șir bila cu numărul $3$ ($X_2 = 3$), iar în al doilea șir bila cu numărul $4$ ($Y_2 = 4$).
* La fiecare pas $i \geq 3$ Nino va pune în șirul $X$ bila $X_i = X_{i-1} + Y_{i-1}$, iar în șirul $Y$, în ordine crescătoare, bilele numerotate cu $X_{i-1}+1, X_{i-1}+2, \dots, X_i-1$, cu excepția bilei $4$ care a fost pusă deja.

Dacă la un pas $k$, $X_k > n$, bilele rămase vor fi inscripționate cu valorile $X_{k-1}+1, X_{k-1}+2, \dots, n$ și vor fi puse în șirul $Y$.

Pentru că bilele se rostogolesc, Nino împachetează în tuburi verticale de culoare galbenă, bilele din primul șir, iar în tuburi verticale de culoare roșie, bilele din al doilea șir. În fiecare tub încap cel mult $m$ bile, dispuse pe o singură coloană. Tuburile sunt așezate vertical, întâi cele galbene, în ordinea umplerii, apoi cele roșii în ordinea umplerii lor. Bilele de la baza fiecărui tub formează nivelul $1$, cele situate imediat deasupra lor formează nivelul $2$ etc., nivelul maxim putând fi $m$.

~[tbile.jpg]

# Task

Se dau numerele naturale $n$ și $m$ și se cer să se determine:
1) Numărul de tuburi de culoare roșie necesare pentru a împacheta bilele din șirul $Y$ și numărul total de bile conținute de acestea.
2) Pentru un nivel $v$ dat, suma numerelor inscripționate pe bilele de pe nivelul $v$.

# Input data

Fișierul de intrare `tbile.in` conține pe prima linie un număr natural $c$ reprezentând cerința care trebuie să fie rezolvată ($1$ sau $2$), pe a doua linie un număr natural $n$, reprezentând numărul de bile ce se inscripționează, iar pe cea de a treia linie un număr natural $m$, reprezentând numărul de bile care încap într-un tub. Dacă cerința este $c = 2$, fișierul de intrare conține, în plus, pe a patra linie, un număr natural $v$ reprezentând numărul unui nivel.

# Output data

Dacă cerința este $c=1$, atunci, pe prima linie a fișierului `tbile.out`, vor fi scrise două numere naturale, separate printr-un spațiu, reprezentând, în această ordine, numărul de tuburi de culoare roșie necesare pentru a împacheta bilele din șirul $Y$, respectiv, numărul total de bile conținute de acestea.
Dacă cerința este $c=2`, atunci, pe prima linie a fișierului `tbile.out` va fi scris un număr natural reprezentând suma numerelor inscripționate pe bilele de pe nivelul $v$.

# Constraints and clarifications

* $5 \leq n \leq 2 \ 000 \ 000 \ 000$;
* $1 \leq v \leq m \leq 311 \ 445 \ 015$;
* Se acordă $30$ de puncte pentru rezolvarea corectă a cerinței $1$ și $60$ de puncte pentru rezolvarea corectă a cerinței $2$. Se acordă $10$ puncte din oficiu.

# Example 1

`tbile.in`
```
1
36
5
```

`tbile.out`
```
6 29
```

## Explanation

Primul șir va conține $7$ bile $(1, 3, 7, 12, 18, 26, 35)$, iar cel de al doilea $36-7=29$ de bile (ca în figura de mai sus). Sunt necesare $6$ tuburi de capacitate $5$.

# Example 2

`tbile.in`
```
2
36
5
3
```

`tbile.out`
```
126
```

## Explanation

Pe nivelul $3$ se găsesc bilele inscripționate cu numerele $7, 5, 11, 17, 23, 29$ și $34$. Suma acestor valori este $126$.