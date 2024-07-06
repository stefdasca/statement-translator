Paftenie lives in a square city, divided into $n \times n$ square regions, arranged in $n$ rows, numbered from $1$ to $n$, and $n$ columns, numbered from $1$ to $n$. In each such region there is a café, and next to each café, there is a sign pointing north ($\uparrow$), south ($\downarrow$), west ($\leftarrow$) or east ($\rightarrow$). By "café $(i, j)$", we will refer to the café at row $i$ and column $j$.

On the first day, in each café, exactly one of the $n^2$ citizens of the city takes their breakfast. Starting from the second day, each citizen will take their breakfast in the neighboring café to the one where they had breakfast the previous day, according to the direction indicated by the sign associated with it. This process is repeated for $k$ days.

Starting from a day at café $(i, j)$, the neighboring café reached the next day is $(i - 1, j)$ if the direction of the sign is _north_ or $(i + 1, j)$ if the direction of the sign is _south_ or $(i, j - 1)$ if the direction of the sign is _west_ or $(i, j + 1)$ if the direction of the sign is _east_.

Paftenie defines the _happiness degree of a citizen_ as the number of citizens with whom they had breakfast together at least once during the $k$ days. Furthermore, Paftenie defines the _happiness degree of the city_ as the sum of the happiness degrees of its citizens.

# Task

As Paftenie is too distracted by his English breakfast with sausages and baked beans, he turns to you to determine:

1. The maximum number of citizens having breakfast together on the second day.
2. The happiness degree of his city.

# Input data

The input file `sim.in` contains in the first line a natural number $C$, and in the second line the natural numbers $n$ and $k$, separated by a space. The following $n$ lines in the file contain $n$ natural numbers from the set $\{1, 2, 3, 4\}$ ($1$ for north, $2$ for south, $3$ for west, $4$ for east), separated by a space. The $j$-th number on line $i + 2$ in the file represents the direction of the sign associated with café $(i, j)$.

# Output data

The output file `sim.out` will contain a single natural number $X$:

1. If $C = 1$, then $X$ will be the maximum number of citizens having breakfast together on the second day.
2. If $C = 2$, then $X$ will be the happiness degree of Paftenie's city.

# Constraints and clarifications

* $C \in \{1, 2\}$
* $2 \leq n \leq 1 \ 000$
* $k \in \{1 \ 000, 1 \ 000 \ 000 \ 000\}$
* It is guaranteed that there is no sign that, once followed, leads to leaving the city.

|#|Score|Constraints|
|-|-|--------|
|1|20|$C = 1, n \leq 30, k = 1 \ 000$|
|2|30|$C = 2, n \leq 30, k = 1 \ 000$|
|3|20|$C = 2, n \leq 30, k = 1 \ 000 \ 000 \ 000$|
|4|30|$C = 2, 30 < n \leq 1 \ 000, k = 1 \ 000 \ 000 \ 000$|

# Example 1

`sim.in`
```
1
3 1000
4 3 2
4 2 2
4 3 3
```

`sim.out`
```
3
```

## Explanation

The city is graphically represented in the bidimensional array (matrix) $A$, and its citizens are numbered as in the matrix $A_1$. In each cell of the matrix $A_i$, with $1 \leq i \leq 2$, are the citizens who, on day $i$, take their breakfast in the respective café.

The maximum number of citizens having breakfast together on the second day is $3$, located in café $(3, 2)$.

# Example 2


`sim.in`
```
2
5 1000
4 3 2 4 2
4 2 2 3 2
1 4 4 2 1
1 4 1 2 1
1 3 3 3 1
```

`sim.out`
```
30
```

## Explanation

The city is graphically represented in the bidimensional array (matrix) $B$, and its citizens are numbered as in the matrix $B_1$. In each cell of the matrix $B_i$, with $1 \leq i \leq 4$, are the citizens who, on day $i$, take their breakfast in the respective café.

The table $T$ contains the meetings that take place by the end of the $1000$ days. The second column contains the list of citizens with whom the citizen from the first column meets. The answer is $3+2+2+3+2+3+2+2+2+3+2+2+2 = 30$.

~[tempgrids.png]