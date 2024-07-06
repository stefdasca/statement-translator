Dornic să apară în probleme după mai mulți ani de așteptare, Micul Gates decide să joace următorul joc cu numere. Se consideră o mulțime de numere care la început este vidă.
Asupra acesteia se pot aplica următoarele tipuri de operații:

* `1 x` - Se adaugă numărul $x$ în mulțime;
* `2 y` - Se scot toate numerele divizibile cu (numărul prim) $y$ din mulțime;
* `3`  - Se dorește aflarea cardinalului mulțimii.

# Task
Scrieți un program care determină rezultatele la operațiile de tipul $3$.

# Input data
Pe prima linie a fișierului `prime.in` se află un număr $N$. Pe următoarele $N$ linii se află câte o operație după structura explicată anterior.

# Output data
Fișierul `prime.out` conține câte o linie cu valoarea determinată pentru fiecare task de tipul $3$, în ordinea în care acestea apar în fișierul de intrare.

# Constraints and clarifications
* Numărul de operații $3 \leq N \leq 3 * 10^5$, și există cel puțin o operație de tipul $3$;
* $2 \leq x \leq 2 * 10^6$; 
* $2 \leq y \leq 2 * 10^6$;
* Pentru $30$ puncte, $N \leq 10^3$;
* Toate numerele adăugate în mulțime prin operația de tipul $1$ sunt diferite între ele.



# Example

`prime.in`
```
6
1 10
1 3
1 5
3
2 5
3
```

`prime.out`
```
3
1
```

## Explanation

Inițial mulțimea este vidă. Primele $3$ operații de tipul $1$ adaugă pe rând $10$, $3$, și $5$. 
Următoare linie reprezintă o cerință de tipul $3$, la care răspunsul este $3$, reprezentând cardinalul mulțimii $\{10, 3, 5\}$.
Operația de pe linia următoare face să se scoată din mulțime numerele divizibile cu $5$, adică $\{10, 5\}$, deci la următoare operație de tip $3$, mulțimea un element.