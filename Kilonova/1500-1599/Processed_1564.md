```markdown
Roboțelul WALL-E este captiv într-un labirint dreptunghiular de dimensiuni $N * M$. Analizând harta, WALL-E constată că are de-a face cu un labirint extrem de sofisticat. El reușește să identifice următoarele tipuri de celule: `W` – celula unde, la început, se află WALL-E, `E` - celula $EXIT$ care poate fi accesată de WALL-E și care îl poate teleporta pe acesta instantaneu în afara labirintului, într-un loc sigur, `.` - celule libere, care pot fi accesate de WALL-E, `#` - celule de tip zid, care **NU** pot fi accesate de WALL-E, `+` - celule de tip ușă, care pot fi accesate de WALL-E, dar continuarea deplasării la o celulă vecină se poate face doar după o așteptare de exact $T$ secunde, `P` - celule de tip portal, care îl teleportează pe WALL-E instantaneu, la întâmplare, într-una dintre celelalte celule de tip portal. Dacă WALL-E accesează o celulă $(x_1, y_1)$ de tip portal, atunci el va fi instantaneu teleportat la o altă celulă $(x_2, y_2)$ de tip portal, iar mai departe el se va deplasa numai într-o celulă vecină cu $(x_2, y_2)$ (nu poate sta pe loc). WALL-E se poate deplasa într-o secundă în oricare dintre cele patru celule vecine: sus, dreapta, jos sau stânga, pe care le poate accesa. De asemenea, roboțelul **NU** se poate deplasa în afara labirintului decât prin intermediul celulei $EXIT$.

# Task

The chaotic behavior of the portals worries WALL-E, so he proposes to find out the minimum number of seconds in which, **with certainty**, he will be able to leave the maze. If it cannot be determined with certainty, or if WALL-E cannot leave the maze, the answer will be $-1$.

# Input data

In the text file `walle.in`, the first line contains the numbers $N$, $M$ and $T$, separated by a space. Each of the following $N$ lines contains a string of $M$ characters.

# Output data

In the text file `walle.out`, print on the first line a natural number representing the found answer or $-1$.

# Constraints and clarifications

* $1 \leq N, M \leq 500$;
* $0 \leq T \leq 1 \ 000$;
* There is a single cell marked with `W`;
* There is a single cell marked with `E`;
* The number of portal cells is greater than or equal to $2$;
* It is guaranteed that each portal cell has at least one accessible neighboring cell;
* For tests worth $19$ points, the maze will contain exactly $2$ portals and $T = 0$;
* For another $16$ points, the maze will contain exactly $2$ portals;
* For another $19$ points $1 \leq N, M \leq 50$, the maze will contain at most $6$ portals and $T = 0$;
* For another $27$ points $1 \leq N, M \leq 50$, the maze will contain at most $6$ portals;
* For another $10$ points $T = 0$.

# Example 1

`walle.in`
```
5 12 3
.....#P..E..
..P..###....
.....+...P..
..W...##....
............
```

`walle.out`
```
5
```

## Explanation

WALL-E will move in $2$ seconds to the portal at position $(2,3)$, which will teleport him in the worst case to position $(1,7)$, from where in $3$ seconds he will reach the EXIT. Total $5$ seconds.

# Example 2

`walle.in`
```
5 12 3
......P#.E..
..P..###....
.....+...P..
..W...##....
............
```

`walle.out`
```
12
```

## Explanation

WALL-E will move towards the EXIT, avoiding the portals and the door, on the shortest path.

# Example 3

`walle.in`
```
1 6 3
EPPPWP
```

`walle.out`
```
-1
```

## Explanation

Suppose WALL-E first moves to the portal $(1,4)$. It is uncertain that WALL-E can reach the portal $(1,2)$ because from the portal $(1,4)$, due to the chaotic behavior of the portals, he can reach any of the other three portals, not just the portal $(1,2)$, and then the next teleportation can return WALL-E, for the same reason, to the portal $(1,4)$. Similarly, the same thing will happen if WALL-E first moves to the portal $(1,6)$.
```