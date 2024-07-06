In the neighboring village, there is a rectangular agricultural field divided into $N \cdot M$ identical elementary squares, arranged side by side with $M$ on each row and $N$ on each column. The rows are numbered from $1$ to $N$, and the columns from $1$ to $M$. An elementary square located on the field at row $R$ and column $C$ is identified by the coordinates $(R, C)$.

Rectangular areas of the field (each formed by one or more adjacent elementary squares) are claimed by $T$ farmers from the village, as heirs, based on documents received from their ancestors. Because there are also false documents, it was found that multiple farmers may claim the same elementary squares.

In the $T$ documents of the farmers, the rectangular areas are each specified by two pairs of numbers $(X, Y)$ and $(Z, U)$, representing the coordinates of the first elementary square in the top-left corner of the area (row $X$ and column $Y$), respectively the coordinates of the last elementary square located in the bottom-right corner of the area (row $Z$ and column $U$).

# Task

Write a program to read the natural numbers $N, M, T, R, C$ and then the $T$ pairs of coordinates $(X, Y)$ and $(Z, U)$ specified in the documents (corresponding to the claimed rectangular areas) and determine:

1. the number of farmers claiming the elementary square identified by the coordinates $(R, C)$
2. the maximum number of farmers claiming the same elementary square
3. the maximum number of elementary squares forming a square **not claimed** by any farmer

# Input data

The input file `teren.in` contains on the first line a natural number $P$ which can only have the value $1$, value $2$ or value $3$. The second line of the file contains five natural numbers $N, M, T, R, C$, separated by space, with the meaning from the statement. On each of the next $T$ lines of the file there are four nonzero natural numbers $X_K, Y_K, Z_K, U_K$, separated by space, representing the pairs of coordinates $(X_K,Y_K)$ and $(Z_K,U_K)$ corresponding to the areas claimed by the $T$ farmers ($1 \leq K \leq T$).

# Output data

The output file `teren.out` will contain on the first line a natural number representing the number of farmers who claim the elementary square identified by the coordinates $(R, C)$ if the task was $1$, a natural number representing the maximum number of farmers claiming the same elementary square if the task was $2$, or a natural number representing the maximum number of elementary squares forming a square area **not claimed** by any farmer if the task was $3$.

# Constraints and clarifications

* $3 \leq N, M \leq 180$
* $3 \leq T \leq 100$
* $1 \leq R \leq N$
* $1 \leq C \leq M$
* $1 \leq X_K \leq Z_K \leq N$ and $1 \leq Y_K \leq U_K \leq M$ for $1 \leq K \leq T$
* For correctly solving task $1$ you get $20\\%$ of the total score, for correctly solving task $2$ you get $20\\%$, and for correctly solving task $3$ you get $60\\%.

# Example 1

`teren.in`
```
1
3 5 3 2 2
2 3 2 3
1 2 3 3
2 1 2 3
```

`teren.out`
```
2
```

## Explanation

The elementary square with coordinates $R = 2$ and $C = 2$ is claimed by $2$ farmers.
~[teren.png|align=center]

# Example 2

`teren.in`
```
2
3 5 3 2 2
2 3 2 3
1 2 3 3
2 1 2 3
```

`teren.out`
```
3
```

## Explanation

The elementary square with coordinates $(2, 3)$ is claimed by $3$ farmers (the maximum number of claims).

# Example 3

`teren.in`
```
3
3 5 3 2 2
2 3 2 3
1 2 3 3
2 1 2 3
```

`teren.out`
```
4
```

## Explanation

There are two square areas not claimed by any farmer, each formed by the maximum number of four elementary squares. These have the coordinates: $(1, 4)$ and $(2, 5)$ and $(2, 4)$ and $(3, 5)$, respectively.