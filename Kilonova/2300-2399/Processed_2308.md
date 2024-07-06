Fie $A$ și $B$ două mulțimi de șiruri formate doar din litere mici ale alfabetului englez (de la `a` la `z`). Fie $Na$ numărul șirurilor din mulțimea $A$, iar $Nb$ numărul șirurilor din mulțimea $B$.
Se spune că $s_1 \ s_2 \dots s_k$ este o subsecvență a unui șir $a_1 \ a_2 \dots a_n$ dacă există un număr natural $i (1 \leq i \leq n - k)$ astfel încât $s_1 = a_i$, $s_2= a_{i+1}, \dots, s_k = a_{i+k-1}$.

# Task

Scrieți un program care să determine numărul șirurilor care sunt subsecvențe ale tuturor șirurilor din $A$, dar nu sunt subsecvențe ale niciunui șir din $B$.

# Input data

Fișierul de intrare `sub.in` conține pe prima linie un număr natural $Na$ reprezentând numărul de șiruri din mulțimea $A$. Următoarele $Na$ linii conțin cele $Na$ șiruri ale mulțimii $A$, fiecare șir pe câte o linie. Linia $Na+2$ a fișierului conține un număr natural $Nb$ reprezentând numărul de șiruri din mulțimea $B$. Următoarele $Nb$ linii conțin cele $Nb$ șiruri ale mulțimii $B$, fiecare șir pe câte o linie.

# Output data

Fișierul de ieșire `sub.out` va conține o singură linie pe care se va scrie o valoare naturală reprezentând numărul șirurilor care sunt subsecvențe ale tuturor șirurilor din $A$, dar nu sunt subsecvențe ale niciunui șir din $B$.

# Constraints and clarifications

* $1 \leq Na \leq 100$
* $1 \leq Nb \leq 100$
* Lungimile șirurilor din mulțimile $A$ și $B$ sunt numere cuprinse între $1$ și $300$. 

# Example

`sub.in`
```
3
abcaf
bcaf
dbdafabcaf
3
bacbc
fbca
ca
```

`sub.out`
```
3
```

## Explanation

Șirurile: `a`, `b`, `c`, `f`, `bc`, `ca`, `af`, `bca`, `bcaf`, `caf` sunt subsecvențe ale tuturor șirurilor din `A`. Dintre acestea șirurile: `a`, `b`, `c`, `f`, `ca`, `af`, `bca` sunt subsecvențe ale cel puțin unui șir din $B$.
Rămân $3$ șiruri care sunt subsecvențe ale tuturor șirurilor din $A$, dar nu sunt subsecvențe ale niciunui șir din $B$: `af`, `caf`, `bcaf`.

