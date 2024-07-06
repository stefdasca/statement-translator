Great mathematician, Little Gates enjoys playing by writing natural numbers starting with the value $1$, $n$ per line, until he fills $n$ lines. On the first line, he writes from left to right, numbers from $1$ to $n$, continues on the second line, from right to left with numbers from $n+1$ to $2 \cdot n$, then from left to right numbers from $2n+1$ to $3 \cdot n$ and so on, until he fills the $n$ lines.

# Task

1. Determine the sum of the even elements on the first line.
2. Determine the sum of the elements on the last line.
3. Determine the sum of the elements in the first column. (The sum of the elements that are first on their respective line).

# Input data

The input file `numere.in` contains the number $c$ of the task, which can only be $1$, $2$, or $3$, on the first line. The second line contains the non-zero natural number $n$.

# Output data

The output file `numere.out` will contain the determined value according to the task.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;

# Example 1

`numere.in`
```
1
6
```

`numere.out`
```
12
```

## Explanation

It is observed that $n=6$, the numbers written by Little Gates are arranged as follows:

|   |   |   |   |   |   |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 |
|12 |11 |10 | 9 | 8 | 7 |
|13 |14 |15 |16 |17 |18 |
|24 |23 |22 |21 |20 |19 |
|25 |26 |27 |28 |29 |30 |
|36 |35 |34 |33 |32 |31 |

The task is $1$.
Thus, the even numbers on the first line are: $2$, $4$, and $6$. Their sum is $12$.

# Example 2

`numere.in`
```
2
6
```

`numere.out`
```
201
```

## Explanation

The task is $2$, and $n=6$. The numbers are arranged as in the table above.
The sum of the elements on the last line $= 36+35+34+33+32+31 = 201$.

# Example 3

`numere.in`
```
3
6
```

`numere.out`
```
111
```

## Explanation

The task is $3$, and $n=6$. The numbers are arranged as in the table above.
The sum of the elements in the first column $= 1+12+13+24+25+36 = 111$.