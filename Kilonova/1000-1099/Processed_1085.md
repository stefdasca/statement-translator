Here is the translated statement.

---

On the planet Aret, there is a rectangular-shaped continent divided into $R \cdot C$ identical squares, arranged with $C$ per row and $R$ per column. Each square represents a country. Rows are numbered from $1$ to $R$ from top to bottom, and columns from $1$ to $C$ from left to right. A country located in row $X$ and column $Y$ is identified by the coordinates $(X, Y)$.

~[nori1.png|align=right]

Above the continent, there are $N$ clouds of different types, as in figure $1$, which are also made up of identical squares, and the surface of a square entirely covers the surface of a country. Clouds can enter the continent from the west and move horizontally to the east, or they can enter from the north and move vertically to the south.

Each hour, the clouds move one position in their direction of movement, and when the cloud completely leaves the continent's surface, it re-enters the continent above the same country covered at the first entry (the initial position) and continues moving. Clouds enter for the first time above the continent after a waiting time of $W$ and can overlap during their movement. A cloud is called "entire," if during its movement, there is at least one hour when the cloud is situated above the continent without exceeding its edges.

In the example of figure $2$, there are three clouds, represented by the numbers $1$, $2$, and $3$. Cloud $1$ - of type $1$ - enters the continent through the country $(2, 1)$ after $3$ hours of waiting, cloud $2$ - of type $3$ - enters through the country $(4, 1)$ after $0$ hours of waiting, and cloud $3$ - of type $5$ - enters through the country $(1, 3)$ after $1$ hour of waiting. In this example, the position of each cloud in the first $9$ hours is depicted. In countries not covered by clouds, the sky is clear, and in countries where at least two clouds overlap, there is a storm.

~[nori2.png]

# Task

Given the natural numbers $R$, $C$, $N$, the coordinates of the country where each cloud enters the continent, its type, as well as the waiting time of each cloud at its first entry onto the continent, determine:
1. The number $A$ of entire clouds and the minimum time $B$ after which all entire clouds are situated above the continent without exceeding its edges;
2. Given a time $T$, determine the number $S$ of countries that have a clear sky after $T$ hours and the number $F$ of countries where there is a storm after $T$ hours.

# Input data

The input file `nori.in` contains:
* The first line contains a natural number $P$ which can only have values $1$ or $2$;
* The second line contains four natural numbers $R$, $C$, $N$, and $T$, in this order, separated by a space, with the meaning stated in the task;
* In the next $N$ lines there are four natural numbers $X_i$, $Y_i$, $Z_i$, and $W_i$, where $i \in \{1, 2, 3, \dots, N\}$ in this order, separated by a space. The numbers $X_i$ and $Y_i$ represent the row and column, of the country through which cloud $i$ enters the continent, $Z_i$ represents the type of cloud $i$, and $W_i$ represents the waiting time of the cloud $i$ at the first entrance above the continent.

# Output data

* If the value of $P$ is $1$, only requirement $1$) will be solved. In this case, the output file `nori.out` will contain two natural numbers $A$ and $B$, in this order, separated by a space. The number $A$ represents the number of entire clouds, and $B$ is the determined minimum time;
* If the value of $P$ is $2$, only requirement $2$) will be addressed. In this case, the output file `nori.out` will contain two natural numbers $S$ and $F$, in this order, separated by a space. The number $S$ represents the number of countries that have a clear sky after $T$ hours, and $F$ represents the number of countries where there is a storm after $T$ hours.

# Constraints and clarifications

* $2 \leq R, C \leq 200$;
* $1 \leq N \leq 50$;
* $1 \leq T \leq 2\ 000\ 000$;
* $1 \leq Z_i \leq 25$; $Z_i$ is an odd number; $Z_i$ can be greater than $R$ or $C$;
* $0 \leq W_i \leq 200$;
* For requirement $1$), it is guaranteed that $1 \leq B < 300\ 000$;
* Multiple clouds can enter the continent through the same country;
* No cloud enters the continent through the country with coordinates $(1, 1)$;
* If $X_i$ = $1$ then $2 \leq Y_i \leq C$
* If $Y_i$ = $1$ then $2 \leq X_i \leq R$
* For a correct resolution of requirement $1$, $30\%$ of the points are given, and for requirement $2$, $70\%$ of the points are given.

# Example 1

`nori.in`
```
1
5 3 3 9
2 1 1 3
4 1 3 0
1 3 5 1
```

`nori.out`
```
2 9
```

## Explanation

_See the example in figure $2$_. There are $2$ entire clouds, namely cloud $1$ and cloud $2$. The two clouds are entirely above the continent, first time after $9$ hours.

# Example 2

`nori.in`
```
2
5 3 3 9
2 1 1 3
4 1 3 0
1 3 5 1
```

`nori.out`
```
8 2
```

## Explanation

_See the example in figure $2$_. After $T=9$ hours, the countries with a clear sky are at the coordinates:
$(1, 1)$, $(1, 2)$, $(1, 3)$, $(2, 1)$, $(2, 3)$, $(3, 1)$, $(3, 3)$, $(5, 1)$ and the countries where there is a storm are at the coordinates: $(4, 3)$ and $(5, 2)$.

---

I have reviewed the translation and fixed any potential grammar and syntax errors according to the rules of the English language.