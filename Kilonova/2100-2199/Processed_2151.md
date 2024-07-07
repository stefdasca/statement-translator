
# Task

$M$ mafiosos have taken control of the city of Grozburg. This city is represented as the $Ox$ axis of the coordinate system, with each positive integer coordinate having a building. It is known that among all the buildings in the city, $N$ are banks where the mafiosos can deposit their illegal earnings. Each mafioso can use his influence to control an interval of exactly $K$ consecutive buildings in the city. To avoid raising suspicions from DIICOT, the mafiosos want a minimal number of buildings in the city to be under their influence. A building is considered to be under the influence of the mafiosos if it is under the influence of at least one of them.

The mafiosos need to choose their intervals of buildings (not necessarily disjoint) such that each can choose a bank within his interval where he will deposit his earnings. Two mafiosos cannot choose the same bank for depositing their earnings, even if the bank is in both of their intervals. For the $M$ mafiosos to coexist peacefully, each must have his own bank.

You need to choose the influence intervals of each mafioso so that the above restrictions are respected and the number of buildings under their influence is minimized.

# Input data

The first line of the file `mafioti.in` contains $N$, $M$, and $K$, the number of banks in the city, the number of mafiosos, and the length of the influence interval, respectively. The next line contains $N$ positive and distinct integers, the $i$-th of these numbers representing the coordinate of the $i$-th bank.

# Output data

The first (and only) line of the file `mafioti.out` should contain the minimum number of buildings under the influence of the mafiosos such that the above rules are respected.

# Constraints and clarifications

* $1 \leq N \leq 5\ 000$
* $1 \leq M \leq 1\ 000$
* $1 \leq K \leq 1\ 000\ 000\ 000$
* The coordinates of the buildings are in the interval $[1, 1\ 000\ 000\ 000]$
* For $40\%$ of the tests $N \leq 500$

# Example

`mafioti.in`
```
6 4 4
1 3 4 5 7 8
```

`mafioti.out`
```
5
```

## Explanation

The first mafioso chooses the buildings $1, 2, 3, 4$ (controls bank $1$). The second chooses the buildings $1, 2, 3, 4$ (controls bank $3$). The third chooses the buildings $2, 3, 4, 5$ (controls bank $4$). The fourth chooses the buildings $2, 3, 4, 5$ (controls bank $5$). In total, the mafiosos control a minimum of $5$ buildings.
