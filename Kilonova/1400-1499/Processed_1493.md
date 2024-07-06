The terminal of an airport is a very large hall shaped like a rectangle divided into unit squares. There are several people here, who must wear a badge with a barcode that can be read at any time by surveillance cameras and decoded by the security service’s computers. Each unit square can be occupied by only one person at a time. The hall is represented by a matrix with $R$ rows and $C$ columns, its elements being natural numbers of at most $6$ digits with the following values: `0` – for unoccupied space, and non-zero natural numbers representing the identifiers (IDs) of the persons. Among these people, there are infiltrators who have IDs identical to those of other people. If two or more people have the same ID, they are all considered suspects. The infiltrators want to get close to VIPs (important people) to record their conversations with a microphone that can capture sounds within a **square** with side $D$, centered on the infiltrator. This square is not necessarily entirely within the matrix of the hall (see the adjacent figure)!

~[3185a933b4f9493beaf55464370bb426.png|align=right]

By convention, VIP IDs are distinct prime numbers. Moreover, the ID of a VIP can be copied, thus increasing the number of suspects. A VIP is characterized by a level of importance: the larger the ID, the higher the level of importance (the person is "more important"). Suspect people have an associated "danger level." This is higher if the number of VIPs within the square with side $D$, centered on the suspect, is higher. If there are two suspects with the same danger level, the "more dangerous" person is the one who has the VIP with the highest ID in their square. In case of a tie, the "more dangerous" person is the one situated on a row with a smaller index, and if row indices tie, on a column with a smaller index. There are also suspects with a danger level of $0$ if there is no prime number within the square centered on them.

# Task

1. Determine the number of suspects in the waiting room.
2. Determine the ID and coordinates of the suspects, ($RS_i$ - the row of suspect $i$, $CS_i$ - the column of suspect $i$) in descending order of "danger level."

# Input data

The input file `intrus.in` will contain on the first line the value $p$, which can be either $1$ or $2$. The second line will contain the values $R, C$ and $D$, separated by a space. On the next $R$ lines, there will be $C$ natural numbers of at most $6$ digits, separated by a space, representing the elements of the matrix described in the statement.

# Output data

If $p=1$, only the first task is required to be solved. In this case, the output file `intrus.out` will contain a single value $T$ (which can be $0$), representing the number of suspects. If $p=2$, only the second task will be solved. In this case, the output file `intrus.out` will contain on each line $3$ non-zero natural numbers: $ID_i$ (the ID of suspect $i$), $R_i, C_i$ (the row and column where the suspect is located), separated by a space. If there is no suspect, the first line of the output file `intrus.out` will contain $-1$.

# Constraints and clarifications

* $0 < R, C \leq 1 \ 000$
* $3 \leq D \leq 9, D$ odd number.
* For $p=2$ it is guaranteed that the number of suspects does not exceed $10\%$ of the total number of people in the hall.

# Example 1

`intrus.in`
```
1
3 4 3
1 0 7 3
5 2 3 0
3 2 0 1
```

`intrus.out`
```
7
```

## Explanation

$p=1$, only task 1 is solved.

There are $2$ IDs with value $2$ and $3$ IDs with value $3$, so there are $5$ suspects.

# Example 2

`intrus.in`
```
2
3 4 3
1 0 7 8
5 2 3 0
3 2 0 9
```

`intrus.out`
```
2 2 2
2 3 2
3 2 3
3 3 1
```

## Explanation

$p=2$, only task 2 is solved.

The person with ID $2$, located at row $2$ and column $2$ has the highest danger level. Next is ID $2$ from $(3, 2)$, $3$ from $(2, 3)$ and $3$ from $(3, 1)$, who represent a suspect, although their $D$ side area is not entirely within the matrix of the hall!
