## Task

Determine the minimum number of minutes required for each person to reach their designated seat.

## Input data

The first line of the `cinema.in` file contains the number of friends $N$. The next line contains $N$ numbers representing the initial position of each friend. More precisely, the $i$-th value represents the seat where person $i$ initially sat.

## Output data

The first line of the `cinema.out` file will contain the minimum number $M$ of minutes required for each person to reach their designated seat. The next $M$ lines will have the following structure: the number $R$ of swaps executed in that minute, followed by $R$ pairs of numbers $i \ j$, separated by a space, indicating that in that minute person $i$ swaps seats with person $j$.

## Constraints and clarifications

$2 \leq N \leq 1000$

Evaluation is done on $10$ tests.

The score received for each correctly ordered test is $\left[\frac{M Ok}{M user} \cdot 10\right]$.

## Example

`cinema.in`
```
3
3 1 2
```

`cinema.out`
```
2
1 2 1
2 1 2 2 3
```