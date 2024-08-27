## Task

Magnet

We have $N$ point-like objects located at integer coordinates on the $Ox$ axis. We can act on these objects with a magnet in the following way: The magnet will be activated at a position with integer coordinates (which may or may not coincide with the position of some of the $N$ objects) $S$, with a certain intensity, a natural number, $X$. Objects to the left of the magnet will generally move $X$ units to the right, with the exception of those that would pass the position of the magnet through such a move. These will instead stop exactly at the magnet's position. Similarly, objects to the right of the magnet will move $X$ units to the left, but none of them will pass the position of the magnet. If the position of the magnet already coincides with the position of some objects, they will remain in place.

You are given an array $A$ of length $N$, representing the positions on the $Ox$ axis where there are objects. This array can contain duplicates. You are also given an array $B$ of length $N$, representing the positions on the $Ox$ axis where we would like to have the objects after successively applying the magnet. Is it possible to move the objects to those positions? If so, you are asked for a sequence of at most $10 * N$ operations that accomplish this.

## Input data

The input file `magnet.in` will contain on its first line the number $T$, representing the number of tests. The following lines will contain the description of each test, so for each test, the first line will contain $N$ the number of objects. On the next line, there will be $N$ values $A_1, A_2, \dots, A_N$ representing the initial positions of the objects, and on the third line there will be another $N$ values $B_1, B_2, \dots, B_N$ representing the positions where we want the objects to be after applying the operations.

## Output data

The output file `magnet.out` must contain $T$ responses, representing the answers for each test. Thus, if there is no sequence of operations to move the $N$ objects from positions $A_1, A_2, \dots, A_N$ to positions $B_1, B_2, \dots, B_N$, the file should contain $-1$. If a sequence exists, the number of operations $K$ followed by $K$ lines should be printed. Each of these $K$ lines should contain 2 numbers $S$ and $X$, signifying that the magnet is activated at position $S$ with intensity $X$.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 10\ 000$ 

$0 \leq A_i, B_i \leq 1\ 000\ 000\ 000$

If there are multiple solutions, any of them is accepted. The minimum number of operations is not required, only that it should be less than or equal to $10 * N$.

For any displayed operation, $0 \leq S, X \leq 1\ 000\ 000\ 000$

For tests worth 20% of the points $N \leq 15$ and $A_i, B_i \leq 150$

For tests worth 40% of the points $N \leq 550$ and $A_i, B_i \leq 4500$

## Example

`magnet.in`
```
2
2
5 7
9 6
4
4 2 4 10
5 7 5 5
```

`magnet.out`
```
-1
2
4 3
7 1
```

## Explanation

For the first test, any operation we do cannot separate the 2 objects anymore; they will always be at most 2 units apart from each other.

For the second test, after the first operation, the objects will be at positions 4, 4, 4, and 7. Another valid answer would have been:
```
2
10 1
5 3
```