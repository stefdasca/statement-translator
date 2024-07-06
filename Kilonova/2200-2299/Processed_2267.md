Here's the translated text:

---

Qwerty invented a new variant of the famous TETRIS game. In his version, the game features an array of N bowls numbered from $1$ to $N$, which are initially empty. Qwerty wants to perform $M$ operations on this array of bowls. An operation consists of choosing a continuous interval of bowls $[A, B]$ and adding a candy of color $C$ to each bowl in this interval. Additionally, if at any moment in time a bowl contains two candies of the same color $C$, they disappear, and if $C$ is greater than $1$, a candy of color $C-1$ replaces them.

The operations Qwerty will perform are defined by a recursive relation. He starts with the numbers $A_1 \\ B_1 \\ C_1$ and for any $i$ greater than $1$, he uses the relations:

* $A_i = Min(N, (A_{i-1} \\cdot i) \\ \\% \\ 1 \\ 008 \\ 989)$
* $B_i = Min(N, (B_{i-1} \\cdot i) \\ \\% \\ 1 \\ 008 \\ 989)$
* $C_i = (C_{i-1} \\cdot X + Y)\\ \\%\\ 47 + 1$

Qwerty will place a candy of color $C_i$ in all the bowls between $Min(A_i,B_i)$ and $Max(A_i,B_i)$.

# Task

Since Qwerty is finicky by nature, he wants to know the number of candies that will remain in the bowls before performing the operations, so he asks you to find this number for him.

# Input data

The first line of the input file `tetris.in` contains seven natural numbers $N \\ M \\ A \\ B \\ C \\ X \\ Y$ having the meanings from the statement.

# Output data

The output file `tetris.out` must contain a single number representing the number of candies remaining in the bowls.

# Constraints and clarifications

* $5 \\leq N,M \\leq 400 \\ 000$
* $1 \\leq A, B \\leq N$
* $1 \\leq C \\leq 47$
* $1 \\leq X, Y \\leq 100 \\ 000$
* **The way the input data is generated does not affect the problem's solution in any way!**

# Example

`tetris.in`
```
5 5 2 4 30 2 10
```

`tetris.out`
```
8
```

---