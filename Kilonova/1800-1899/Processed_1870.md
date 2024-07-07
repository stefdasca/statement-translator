
The secret services of Crivățului Country have a very well established network. The network is made up of $N$ centers, numbered from $1$ to $N$. Between the centers, there are roads that can be traveled in both directions, with known lengths. A road connects two centers. Using the existing roads, there is a connection (direct or through other centers) between any two centers. The distance between two centers is the total **minimum** length of the roads traveled to get from one center to the other.
Chief Teo has decided to divide all centers into two departments: espionage and counter-espionage. A division is considered optimal if the **maximum distance** between any two centers in the same department is minimal.
If there are multiple solutions with the same maximum, the solution for which the difference (in absolute value) between the number of centers in the espionage department and the number of centers in the counter-espionage department is minimal is chosen. If even in this case there are multiple solutions, the first in lexicographical order is preferred.

# Task

Given the description of the network, write a program that finds an optimal division of the centers into two departments.

# Input data

The input file `spion.in` contains on the first line the natural numbers $N$ and $M$ representing the number of centers and the number of roads between them, respectively. On each of the following $M$ lines, three natural numbers are written; more precisely, on line $i+1$ are written the numbers $a_i \\ b_i \\ c_i$ with the meaning "there is a road between center $a_i$ and center $b_i$ of length $c_i$". The numbers written on the same line in the input file are separated by a space.

# Output data

The output file `spion.out` will contain two lines. The first line will contain a natural number representing the maximum distance between any two centers in the same department. On the second line will be written $N$ characters. Character $i$ will be the letter $C$ if center $i$ is in the counter-espionage department or the letter $S$ if center $i$ is in the espionage department in the optimal division determined.

# Constraints and clarifications

* $2 < N < 101$
* $0 < a_i, b_i \leq N$
* $0 < M, c_i < 16\ 001$
* We say that the division $(x_1, x_2, \dots, x_N)$ precedes lexicographically the division $(y_1, y_2, \dots, y_N)$ if there is a $k$ such that $x_i = y_i$, for any $i < k$ and $x_k < y_k$; the letter `C` < the letter `S`.
* Partial scores will be awarded as follows:
  - for correctly determining the maximum distance: $20\%$ of the respective test score
  - if the solution is correct (in terms of maximum distance and minimal absolute difference), but is not the first in lexicographical order: $60\%$
  - for obtaining the first correct solution in lexicographical order: $100\%.

# Example 1

`spion.in`
```
5 4
1 2 1
2 3 1
3 4 1
2 5 7
```

`spion.out`
```
3
CCCCS
```

## Explanation

The maximum distance between any two centers in the same department is $3$.
The absolute difference between the number of centers in the espionage and counter-espionage departments is $3$.
The solution is the first in lexicographical order.
Another solution would be `SSSC`, but this is larger lexicographically.

# Example 2

`spioni.in`
```
5 5
1 3 1
3 2 1
2 5 7
3 4 7
2 4 1
```

`spioni.out`
```
3
CCCCS
```

## Explanation

The maximum distance between any two centers in the same department is $3$.
The absolute difference between the number of centers in the espionage and counter-espionage departments is $3$.
```

## Explanation

The maximum distance between any two centers in the same department is $3$.
The absolute difference between the number of centers in the espionage and counter-espionage departments is $3$.
