In the year of grace $6983$ ($1475$), the Turkish army led by Suleiman Pasha was defeated by the allied Christian Moldavian-Hungarian-Polish armies led by Ștefan the Great. The battle took place near Vaslui in the place called Podu Înalt.

The terrain in which the battles took place can be represented as a two-dimensional array with $N$ rows and $M$ columns, numbered starting from $1$. The position of an element in the matrix is identified by its corresponding row and column. $P$ soldiers took part in the battle, in distinct positions, whose locations on the terrain are known.

~[vaslui.png]

In the two-dimensional array representing the terrain, tactical diagonals can be drawn at an angle of $45 ^{\circ}$, separating the soldiers. A tactical diagonal must begin and end at a position located on the edge of the terrain (row $1$ or row $N$, respectively column $1$ or column $M$). A tactical diagonal cannot pass through a position where a soldier is located.

Ștefan, a great strategist, wonders if it is possible to separate the soldiers into equally sized groups by drawing such tactical diagonals.

# Task

* Determine a tactical diagonal such that the battlefield is divided into two zones containing the same number of soldiers. If there is no solution, write only the value $-1$.
* Determine two perpendicular tactical diagonals that divide the battlefield into four zones, each containing the same number of soldiers. If there is no solution, write only the value $-1$.

# Input data

The input file `vaslui1475.in` contains in the first line the natural numbers $N$, $M$, and $P$, separated by a space, representing the number of rows, the number of columns, and the number of soldiers respectively. 

The next $P$ lines contain the positions of the soldiers, one soldier per line. The line describing the position of a soldier contains two natural numbers $lin$ and $col$, separated by a space, representing the row and column of the terrain area where the respective soldier is located.

# Output data

The output file `vaslui1475.out` will contain two lines.

The first line contains $4$ natural numbers $lin_1$, $col_1$, $lin_2$, and $col_2$, separated by a space, representing the position of the first element and the position of the last element of the diagonal determined for task $1$. If there is no solution, only the value $-1$ will be written.

The second line contains $8$ natural numbers $lin_{11}$, $col_{11}$, $lin_{12}$, $col_{12}$, $lin_{21}$, $col_{21}$, $lin_{22}$, and $col_{22}$, separated by a space, representing the position of the first element and the position of the last element of the first diagonal, respectively the position of the first element and the position of the last element of the second diagonal determined for task $2$. If there is no solution, only the value $-1$ will be written.

# Constraints and clarifications

* $2 \leq N, M \leq 50 \ 000$
* $0 \leq P \leq min(M \cdot N, 50 \ 000)$
* The rows and columns of the matrix are numbered starting from $1$.
* The first element on a tactical diagonal is the leftmost one, the last one is the rightmost.
* If there are multiple correct solutions, any of them will be displayed.
* Partial points will be awarded for the correct resolution of only task $1$. In this case, $40\%$ of the test score will be awarded.
* For tests worth $70$ points, $2 \leq N, M \leq 200$.

# Example 1

`vaslui1475.in`
```
6 8 4
1 1
2 5
5 4
6 8
```

`vaslui1475.out`
```
6 2 1 7
6 2 1 7 1 2 6 7
```

## Explanation

~[ex1.png]

# Example 2

`vaslui1475.in`
```
7 10 4
1 9
2 10
5 9
3 9
```

`vaslui1475.out`
```
1 8 3 10
-1
```

## Explanation

~[ex2.png]