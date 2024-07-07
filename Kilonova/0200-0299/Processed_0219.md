
Fie `G` un graf orientat cu `N` noduri și `M` arce. Spunem că *nodul `Y` este accesibil din nodul `X`* dacă se poate ajunge de la `X` la `Y` mergând pe arce în sensul corespunzător al acestora. Spunem că nodul `X` este *“popular�* dacă pentru fiecare nod `Y` al grafului G se îndeplinește cel puțin una din condițiile:
1. `X` este accesibil din `Y`;
2. `Y` este accesibil din `X`.

# Task
Dându-se cele două numere `N` si `M` cât și arcele grafului, să se afle care sunt nodurile populare din graf.

# Input data
Prima linie a fișierului `drumuri.in` conține numerele `N` și `M`, cu semnificația din enunț. Următoarele `M` linii conțin câte două numere `X` și `Y`, semnificând faptul că există arc orientat de la `X` la `Y`.

# Output data
Prima linie a fișierului `drumuri.out` conține numărul `NR`, reprezentând numărul de noduri populare ale grafului. Următoarea linie va conține cele `NR` noduri populare afișate în ordine crescătoare.

# Constraints și clarifications
* `1 \leq N \leq 150 000`
* `1 \leq M \leq 300 000`
* Pentru `50%` din punctaj `N \leq 700, M \leq 1100`
* Pentru `65%` din teste, `G` este aciclic

# Example:

`drumuri.in`

```
5 4
1 2
3 2
2 4
4 5
```

`drumuri.out`

```
3
2 4 5
```

Explanation
---

Nodurile `2, 4` și `5` sunt singurele noduri populare. Nodul `1`, spre exemplu, nu este popular deoarece nu este accesibil din `3`, iar nici nodul `3` nu este accesibil din `1`.
