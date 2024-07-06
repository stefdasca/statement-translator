Directorul unei școli dorește să premieze la sfârșitul anului școlar pe cei mai buni elevi la învățătură. Pentru acest lucru el are de rezolvat două probleme:

1. Să determine câți elevi vor fi premiați dintre cei $n$ elevi ai școlii. După discuții aprinse cu ceilalți profesori se hotărăște în Consiliul Profesoral ca numărul premianților să fie $n - k$, unde $k$ este cel mai mare număr pătrat perfect mai mic strict decât $n$. De exemplu, pentru $n = 150$, $k$ este $144$ (pentru că $144$ = $12^2$), deci vor fi premiați $150 - 144 = 6$ elevi.
2. Pentru a fi cât mai multă liniște la premiere, în Consiliul Profesoral se ia decizia ca elevii care nu vor fi premiați să fie așezați pe terenul de sport pe rânduri de câte $p$ elevi (unde $p^2 = k$). În acest scop, directorul a numerotat elevii nepremiați de la $1$ la $k$ și a hotărât ca elevii să fie așezați în ordinea descrescătoare a numerelor asociate.

# Task

Scrieți un program care citește $n$, numărul de elevi din școală și calculează numărul de elevi premiați precum și modul de așezare a elevilor nepremiați.

# Input data

Fișierul de intrare `lascoala.in` va conține numărul $n$.

# Output data

Fișierul de ieșire `lascoala.out` va conține pe prima linie numărul de elevi premiați, iar pe următoarele linii așezarea elevilor nepremiați.

# Constraints and clarifications

* $2 \leq n \leq 700$;

# Example

`lascoala.in`
```
35
```

`lascoala.out`
```
10
25 24 23 22 21
20 19 18 17 16
15 14 13 12 11
10 9 8 7 6
5 4 3 2 1
```

## Explanation

Cel mai mare pătrat perfect mai mic ca $n$ este $25 = 5^2$.

