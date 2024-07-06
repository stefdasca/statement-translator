Ian managed to find some time to play a game with his friend Edi.

They have $N$ stones on a table. Stone $i$ weighs $a_i$ kilograms. The game is played as follows:
* Both of them choose a permutation $(p_1, p_2, \dots, p_N)$.
* For each $i=1 \dots N$, they proceed as follows: if the stones taken by Ian weigh less than the stones taken by Edi so far, Ian takes the stone with index $p_i$. Otherwise, Edi takes the stone with the index $p_i$.

# Task

Since they are both very busy, they ask you to find the number of permutations $p$ for which at the end of the game the weight of the stones each of them has is the same. Because this number can be very large, you have to print it modulo $998\ 244\ 353$.

# Input data

The first line contains a number $N$ representing the number of stones on the table. The next line contains $N$ numbers $a_1, a_2, \dots, a_N$. Stone $i$ weighs $a_i$ kilograms.

# Output data

The first line will contain a single integer representing the number of permutations with the required property.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $1 \leq a_i \leq 700$

# Example 1

`stdin`
```
3
1 1 2
```

`stdout`
```
4
```

## Explanation

The $4$ permutations are: $(1, 3, 2)$, $(2, 3, 1)$, $(3, 1, 2)$, $(3, 2, 1)$.

# Example 2

`stdin`
```
4
1 2 3 8
```

`stdout`
```
0
```
