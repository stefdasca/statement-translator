Supărați că lansarea părții a treia a filmului lor preferat s-a amânat până în iunie 2018, Henry și Hetty s-au gândit la propriul scenariu pentru finalul trilogiei:

Într-o lume în care vikingii pot zbura cu dragonii există `N` insule. Hiccup, șeful tribului de vikingi aflat pe insula `1`, știe `M` rute directe de zbor bidirecționale între insule. Pentru fiecare `j` intre `1` si `M`, ruta `j` unește insulele $A_j$ și $B_j$ și are lungime $D_j$. 

Pe fiecare insulă `i` `(1 \leq i \leq N)`, există dragoni din specia `i` care pot zbura fără a se opri pentru odihnă o distanță maximă $Dmax_i$. Cu alte cuvinte, dragonii de pe insula `i` vor putea parcurge orice rută `j`(1 \leq j \leq M), pentru care $D_j \leq Dmax_i$, indiferent de ce alte drumuri au făcut anterior.

Hiccup dorește să ajungă de pe insula `1` pe insula `N` pentru a-l salva pe Toothless, dragonul lui. Pentru a ajunge acolo, el va lua inițial un dragon din specia `1` (de pe insula `1`). Apoi, dacă la un moment dat Hiccup se află pe o insula `i` `(1 \leq i \leq N)`, având cu el un dragon din specia `t`, el poate:
1. Să zboare de pe insula `i` pe o altă insulă` x` cu dragonul pe care îl are, folosind o rută directă `j` între insulele `i` si `x`, bineînțeles doar dacă $D_j \leq Dmax_t$ .
2. Să schimbe dragonul din specia `t` pe care îl are cu un dragon din specia `i` aflat pe insula respectivă.

# Task
a. To determine the maximum distance $Dmax_i$ characteristic of a dragon that Hiccup can reach without changing the dragon he initially took from island `1`.
b. To determine the minimum distance that Hiccup must travel to get from island `1` to island `N`.

# Input data
The input file `dragoni.in` contains on the first line a natural number `p`. For all input tests, the number `p` can only have the value `1` or the value `2`. The second line contains two natural numbers `N` and `M` representing the number of islands, respectively the number of direct routes between islands. The third line contains `N` natural numbers, the `i`-th of these representing the maximum distance $Dmax_i$ that a dragon from island `i` can fly. The next `M` lines describe the `M` direct routes. On each of these lines, there are three natural numbers `A, B` and `D` meaning there is a bidirectional route of length `D` between islands `A` and `B`.

# Output data
In the output file `dragoni.out` a single natural number will be displayed.

If the value of `p` is `1`, only requirement `a` will be solved. In this case, the displayed number will represent the maximum distance $Dmax_i$ of a dragon `i` that Hiccup can reach without changing the dragon he initially took from island `1`.

If the value of `p` is `2`, only requirement `b` will be solved, in this case the displayed number will represent the minimum distance that Hiccup must travel to get from island `1` to island `N`.

# Constraints and clarifications
* `1 \leq N \leq 800`
* `1 \leq M \leq 6000`
* $1 \leq Dmax_i \leq 50 \ 000$, for any `1 \leq i \leq N`.
* $1 \leq A_j, B_j \leq N$, for any `1 \leq j \leq M`.
* $1 \leq D_j \leq 50 \ 000$, for any `1 \leq j \leq M`.
* It is guaranteed that Hiccup can reach island `N`.
* It is guaranteed that the answer to any requirement is a natural number less than $10^9$.
* For the correct resolution of the first requirement `20%` of the test score is awarded.
* For the correct resolution of the second requirement `80%` of the test score is awarded.

# Examples

`dragoni.in`
```
1
5 6
6 3 13 20 26
1 2 5
1 3 7
1 5 10
2 3 6
3 4 5
3 5 14
```

`dragoni.out`
```
20
```

`dragoni.in`
```
2
5 6
6 3 13 20 26
1 2 5
1 3 7
1 5 10
2 3 6
3 4 5
3 5 14
```

`dragoni.out`
```
28
```

Explanations
---

For the first test:
`P = 1` so only requirement `a)` will be solved.
There are `N = 5` islands and `M = 6` routes between them. Hiccup starts from island `1` with a dragon that can fly a maximum distance of `6`. With this dragon, he can only reach islands `1, 2, 3`, and `4`, because to reach island `5` he would have to travel a route longer than `6`. The maximum distance a dragon on islands `1, 2, 3`, or `4` can fly is therefore `20` (the dragon on island `4`). It is observed that the dragon that can fly a distance of `26` is on island `5` and is inaccessible.

For the second test:
`P = 2` so only requirement `b)` will be solved. There are `N = 5` islands and `M = 6` routes between them. To travel a minimum distance of `28` between islands `1` and `N`, Hiccup takes the following steps:
He flies from island `1` to island `2` a distance of `5` with the dragon from species `1`.
He flies from island `2` to island `3` a distance of `6` with the dragon from species `1`.
He changes the dragon from species `1` with the dragon found on island `3`, which can fly a maximum distance of `13`.
He flies from island `3` to island `1` a distance of `7` with the dragon from species `3`.
He flies from island `1` to island `5` a distance of `10` with the dragon from species `3`.
In total, he travels a distance of `5 + 6 + 7 + 10 = 28`.