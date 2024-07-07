Fie șirul de numere naturale: $a$, $a+1$, $a+2$, $\dots$, $b$. Din toate numerele acestui șir se poate forma un alt număr prin „lipirea� tuturor cifrelor numerelor din șir, în ordinea din șir. Numim acest număr $x$. Exemplu: $a=97$ și $b=105$. Se va obține prin „lipire� numărul $x = 979899100101102103104105$.

# Task

Se citesc numerele naturale $a$, $b$, $c$ și $d$ și se cere:
* Să se afișeze cifra de pe poziția $c$ din numărul $x$;
* Să se afișeze cel mai mare număr obținut după eliminarea a exact $c$ cifre din numărul $x$.
* Să se afișeze numărul de apariții ale cifrei $d$ în numărul obținut după eliminări.

# Input data

Prima linie a fișierului de intrare `maxim.in` conține numerele $a$, $b$, $c$ și $d$, separate de un spațiu.

# Output data

Se vor afișa în fișierul de ieșire `maxim.out`:
* pe prima linie, cifra de pe poziția $c$ din numărul $x$;
* pe a doua linie, numărul maxim obținut după eliminarea celor $c$ cifre;
* pe a treia linie se va afișa numărul de apariții ale cifrei $d$ în numărul obținut după eliminări.

# Constraints and clarifications

* Numerele $a$, $b$ și $c$ sunt naturale și $1 \leq a \leq b \leq 1 \ 000$;
* $1 \leq c <$ (numărul de cifre ale numărului $x$).
* Numărul natural $d$ este o cifră, $0 \leq d \leq 9$.
* Cifrele eliminate pot fi oriunde în cadrul numărului $x$, nu neapărat pe poziții consecutive.
* Pentru rezolvarea cerinței $1$ se acordă $20 \%$ din punctaj, pentru cerința $2$, $40 \%$ din punctaj și pentru cerința $3$, $40 \%$ din punctaj.

# Example 1

`maxim.in`

```
13 19 8 1
```

`maxim.out`

```
6
671819
2
```

## Explanation

$a=13$, $b=19$, $c=8$ și $d=1$. Numărul $x$ obținut prin „lipire� este $13141516171819$. Cifra de pe poziția $c=8$ din $x$ este $6$. Acest $6$ se scrie pe prima linie de pe ecran. Pe linia a doua este numărul $671819$, după ce s-au eliminat $c=8$ cifre și anume: $1$, $3$, $1$, $4$, $1$, $5$, $1$ de pe primele poziții și apoi cifra $1$ de după cifra $6$; astfel, numărul rămas este $671819$. Pe ultima linie este numărul $2$ (numărul de apariții ale cifrei $d=1$ în numărul obținut după eliminări).