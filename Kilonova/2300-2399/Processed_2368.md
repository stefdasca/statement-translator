File Contents:
Fie $X$ o matrice cu $M$ coloane (numerotate de la $1$ la $M$) și $N$ linii (numerotate de la $1$ la $N$) cu componente din mulțimea $\{ 0, 1 \}$. Pe fiecare linie a matricei se află o singură secvență (eventual vidă) formată din elemente egale cu $1$, secvență identificată prin poziția de început (indicele coloanei pe care se află primul $1$ din secvență) și lungimea ei. Restul elementelor de pe linie sunt egale cu $0$.

# Task
Să se determine numărul de dreptunghiuri cu dimensiunile $A$ și $B$, formate numai din $1$ care se află în matricea $X$. Dreptunghiurile numărate au fie $A$ linii și $B$ coloane, fie $A$ coloane și $B$ linii.

# Input data
Fișierul de intrare `drept.in` conține pe prima linie cele $4$ numere naturale separate prin câte un spațiu cu semnificația din enunț, în ordinea $M \ N \ A \ B$. Pe fiecare dintre următoarele $N$ linii conțin câte două numere naturale separate prin spațiu, descriind matricea $X$. Mai exact linia $i$ a fișierului conține poziția de început și lungimea secvenței de elemente egale cu $1$ de pe linia $i-1$ a matricei $X$.

# Output data
Fișierul de ieșire `drept.out` va conține o singură linie pe care veți scrie numărul de dreptunghiuri care respectă condițiile din enunț.

# Constraints and clarifications
* $1 \leq N, A, B \leq 2 \ 000 \ 099$
* $1 \leq M \leq 5 \ 000 \ 099$
* $0 \leq$ Lungimea unei secvențe formată din elemente egale cu $1 \leq M$

# Example

`drept.in`
```
5 6 2 3
1 5
1 3
1 2
1 1
3 3
2 4
```

`drept.out`
```
3
```

## Explanation

~[name.png]

||1|2|3|4|5|
|-----|----|---|---|----|---|
|1|1|1|1|1|1|
|2|1|1|1|0|0|
|3|1|1|0|0|0|
|4|1|0|0|0|0|
|5|0|0|1|1|1|
|6|0|1|1|1|1|

Cele $3$ dreptunghiuri au colțurile stânga-sus/dreapta-jos:
(1, 1) / (3, 2)
(1, 1) / (2, 3)
(5, 3) / (6, 5)