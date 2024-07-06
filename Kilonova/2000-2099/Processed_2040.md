# Task

Cătălin wrote on the board all the natural numbers from $l$ to $r$ (inclusive). Unfortunately, some of these numbers got erased.

Knowing that only $n$ numbers $a_1, a_2, \ldots, a_n$ remain on the board, Cătălin wants to find out:

- If $c=1$, what is the sum of the numbers that were erased from the board?
- If $c=2$, what is the smallest number that was erased from the board?
- If $c=3$, what is the largest number that was erased from the board?

# Input data

The input file `nrsterse.in` will contain:

The first line contains a number $c$ - the number of the task.

The second line contains three numbers $n$, $l$ and $r$.

The third line contains the $n$ numbers $a_1, a_2, \ldots, a_n$ that remain on the board.

# Output data

- If $c=1$, the output file `nrsterse.out` will contain the sum of the numbers that were erased from the board.
- If $c=2$, the output file `nrsterse.out` will contain the smallest number that was erased from the board.
- If $c=3$, the output file `nrsterse.out` will contain the largest number that was erased from the board.

# Constraints and clarifications

- $1 \le c \le 3$;
- $1 \le n \le 10^5$;
- $1 \le l < r \le 10^9$;
- $n < r - l + 1$;
- $l \le a_1 < a_2 < \ldots < a_n \le r$;
- For $20$ points, $c=1$ and $l=1$;
- For $20$ points, $c=1$;
- For $30$ points, $c=2$;
- For $30$ points, $c=3$.

# Example 1

`nrsterse.in`
```
1
6 2 10
2 3 4 6 9 10
```

`nrsterse.out`
```
20
```

## Explanation

Cătălin wrote on the board the numbers $2, 3, 4, 5, 6, 7, 8, 9$ and $10$, of which $5$, $7$ and $8$ got erased. Their sum is equal to $5 + 7 + 8 = 20$.

# Example 2

`nrsterse.in`
```
2
6 2 10
2 3 4 6 9 10
```

`nrsterse.out`
```
5
```

## Explanation

Among all the erased numbers, $5$ is the smallest.

# Example 3

`nrsterse.in`
```
3
6 2 10
2 3 4 6 9 10
```

`nrsterse.out`
```
8
```

## Explanation

Among all the erased numbers, $8$ is the largest.