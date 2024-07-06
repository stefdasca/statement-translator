As in most fairy tales, Prince Charming sought a maiden and found her, but her father demanded that he pave the road of length $N$ that connects their castles. The tiles with which he will pave the road have the same width (equal to the width of the road) and natural number lengths. Being a somewhat troubled emperor, he desires that the paving be done using a minimum number of tiles, the length difference between two consecutive tiles not exceeding $1$, and the first and last tiles each being of length $1$. The emperor is not content to receive just a number (the minimum number of tiles needed) from Prince Charming: he also wants the smallest lexicographic paving possibility.

Lexicographic comparison of two sequences of numbers is an extension of the alphabetic comparison of two words. Thus, given two numerical sequences of the same length, $A_1, A_2, \dots, A_m$ and $B_1, B_2, \dots, B_m$, they are equal if and only if $A_i = B_i$ for any $i$ from $1$ to $m$. The sequence $A$ is lexicographically smaller than the sequence $B$ if there exists a value $k$ such that $A_k < B_k$ and $A_i = B_i$ for any $i$ from $1$ to $k - 1$. For example, the sequence $3, 5, 4, 1$ is lexicographically greater than the sequence $3, 5, 2, 9$ because the first position where the values differ is position $3$ ($4 > 2$), without considering the values after this.

# Task

Given the length of the road, determine the minimum number of tiles needed for paving and the smallest lexicographically paving possibility with the minimum number of tiles.

# Input data

The first line of the file `pavare.in` contains a natural number $V$. The second line contains a natural number $N$ representing the length of the road.

# Output data

If $V$ has the value $1$, the file `pavare.out` will contain, on the first line, only the minimum number of tiles needed for paving.

If $V$ has the value $2$, the file `pavare.out` will contain, on the first line, a sequence of numbers separated by spaces, representing the paving solution of the road, using a minimum number of tiles, which is the smallest lexicographically.

# Constraints and clarifications

* $V \in \{1, 2\}$
* $1 \leq N \leq 10^9$;
* For $30$% of the score $V = 1$.

# Example 1

`pavare.in`
```
1
7
```

`pavare.out`
```
5
```

## Explanation

For the road of length $7$, $5$ tiles are needed.

# Example 2

`pavare.in`
```
2
7
```

`pavare.out`
```
1 1 2 2 1
```

## Explanation

The solutions with the minimum number of tiles are: $1 1 2 2 1$, $1 2 1 2 1$, $1 2 2 1 1$.