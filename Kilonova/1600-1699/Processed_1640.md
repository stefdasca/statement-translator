Fie $A = (a_1, a_2, \ldots, a_N)$ o permutare a mulțimii $\{1, 2, \ldots, N\}$.
Permutarea $A$ o numim *$K$-swap* dacă prin aplicarea algoritmului de sortare *bubble-sort* sunt necesare exact $K$ swapuri (interschimbări) pentru ca aceasta să devină permutarea identică.
Reamintim algoritmul *bubble-sort*:

```cpp
do {
    ok = 1;
    for (int i = 1; i < N; i++)
        if (a[i] > a[i + 1]) {
            swap(a[i], a[i + 1]);
            ok = 0;
        }
} while (ok == 0);
```

# Task

Pentru $N$ și $K$ dat să se determine numărul de permutări *$K$-swap* ale mulțimii $\{1, 2, \ldots, N\}$.
Exemplu: pentru $N = 3$ și $K = 2$, dintre permutările $\{1, 2, 3\}$, $\{1, 3, 2\}$, $\{2, 1, 3\}$, $\{2, 3, 1\}$, $\{3, 1, 2\}$, $\{3, 2, 1\}$, permutările $2$-swap sunt următoarele: $\{2, 3, 1\}$, $\{3, 1, 2\}$.

# Input data

Fișierul de intrare `kswap.in` conține pe prima linie două numere naturale nenule $N \ K$ separate prin câte un spațiu, cu semnificația descrisă anterior.

# Output data

Pe prima linie a fișierului de ieșire `kswap.out` se va scrie un singur număr natural $M$ ce reprezintă numărul de permutări $K$-swap, modulo $30103$ ale mulțimii $\{1, 2, \ldots, N\}$.

# Constraints and clarifications

* $1 \leq N \leq 150$
* $1 \leq K \leq N \times (N - 1) / 2$
* Prin permutarea identică înțelegem permutarea $\{1, 2, \ldots, N\}$

# Examples

`kswap.in`
```
4 5
```

`kswap.out`
```
3
```

## Explanation

Permutările mulțimii $\{1, 2, 3, 4\}$ sunt: $\{1, 2, 3, 4\}$, $\{1, 2, 4, 3\}$, $\{1, 3, 2, 4\}$, $\{1, 3, 4, 2\}$, $\{1, 4, 2, 3\}$, $\{1, 4, 3, 2\}$, $\{2, 1, 3, 4\}$, $\{2, 1, 4, 3\}$, $\{2, 3, 1, 4\}$, $\{2, 3, 4, 1\}$, $\{2, 4, 1, 3\}$, $\{2, 4, 3, 1\}$, $\{3, 1, 2, 4\}$, $\{3, 1, 4, 2\}$, $\{3, 2, 1, 4\}$, $\{3, 2, 4, 1\}$, $\{3, 4, 1, 2\}$, $\{3, 4, 2, 1\}$, $\{4, 1, 2, 3\}$, $\{4, 1, 3, 2\}$, $\{4, 2, 1, 3\}$, $\{4, 2, 3, 1\}$, $\{4, 3, 1, 2\}$, $\{4, 3, 2, 1\}$.
Doar $3$ dintre acestea sunt permutări $5$-swap: $\{3, 4, 2, 1\}$, $\{4, 2, 3, 1\}$, $\{4, 3, 1, 2\}$