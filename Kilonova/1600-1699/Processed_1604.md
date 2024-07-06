> "Giving a High Five to the Bear"

Andrei solved the problem [trip](https://kilonova.ro/problems/619) and afterwards thought about going on a trip to the forest. When he returned, at the exit of the forest, there was a bear. The bear asked him $T$ questions of the form: "*I give you a natural number $N$. Tell me what $C_N^0 \cdot (N + 0) + C_N^1 \cdot (N + 1) + C_N^2 \cdot (N + 2) + \dots + C_N^N \cdot (N + N)$ is.*" By $C_N^K$ we denote [combinations of $N$ taken $K$ at a time](https://en.wikipedia.org/wiki/Combination).  
Andrei doesn't know how to solve the problem, so he asks you to solve it.

# Task

For each number $N$ among the $T$ given by the bear, you need to tell what $C_N^0 \cdot (N + 0) + C_N^1 \cdot (N + 1) + C_N^2 \cdot (N + 2) + \dots + C_N^N \cdot (N + N)$ is, more formally $\\sum_{i=0}^{N} C_N^i \cdot (N + i)$. Since these numbers can be very large, you will need to display them modulo $998 \\ 244 \\ 353$.

# Input data

The first line will contain the number $T$. Then, for $i$ from $1$ to $T$, the line $i + 1$ will contain a number $N$, representing the number given by the bear for the $i$-th question.

# Output data

The $i$-th line will contain a single number representing the answer to the bear's $i$-th question, modulo $998 \\ 244 \\ 353$.

# Constraints and clarifications

* $1 \\leq T \\leq 10$
* $1 \\leq N \\leq 10 ^ {18}$

| # | Points | Constraints |
| - | ------- | ------------ |
| 0 | 0 | Example |
| 1 | 5 | $N \\leq 100$ |
| 2 | 12 | $N \\leq 2 \\cdot 10 ^ 3$ |
| 3 | 16 | $N \\leq 2 \\cdot 10 ^ 6$ |
| 4 | 22 | $N \\leq 10 ^ 7$ |
| 5 | 45 | No additional constraints |


# Example

`stdin`
```
4
2 
6
2344
5459875
```

`stdout`
```
12
576
47421958
201586235
```

## Explanation

For the first test, $C_2^0 \cdot (2 + 0) + C_2^1 \cdot (2 + 1) + C_2^2 \cdot (2 + 2) =$ $1 \cdot 2 + 2 \cdot 3 + 1 \cdot 4 = 2 + 6 + 4 = 12$, and $12 \text{ mod } 998 \\ 244 \\ 353 = 12$, so the answer is $12$.

For the second test, $C_6^0 \cdot (6 + 0) + C_6^1 \cdot (6 + 1) + C_6^2 \cdot (6 + 2)$ $ + C_6^3 \cdot (6 + 3) + C_6^4 \cdot (6 + 4) + C_6^5 \cdot (6 + 5)$ $ + C_6^6 \cdot (6 + 6) = 1 \cdot 6 + 6 \cdot 7$ $+ 15 \cdot 8 + 20 \cdot 9 + 15 \cdot 10 + 6 \cdot 11$ $+ 1 \cdot 12 = 6 + 42 + 120 + 180 + 150 + 66 + 12 = 576$, and $576 \text{ mod } 998 \\ 244 \\ 353 = 576$, so the answer is $576$.