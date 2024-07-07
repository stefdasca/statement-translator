It is considered a table with $N$ rows and $N$ columns (numbered from $1$ to $N$) which contains the value $1$ in each of the $N \cdot N$ cells. The values in the table can be modified by applying two coded operations as follows:

* $L \ nr$, which simultaneously changes the signs of all numbers in the row with number $nr$.
* $C \ nr$, which simultaneously changes the signs of all numbers in the column with number $nr$.

# Task
1. Given a sequence of $K$ operations ($L \ nr$ or $C \ nr$) on the rows/columns of the initial table (in which all cells contain the value $1$), determine the number of positive values in the table at the end of executing the $K$ operations.
2. Determine the minimum number of operations $L \ nr$ or $C \ nr$ which, applied to the initial table, modify it so that the resulting table contains exactly $Z$ negative values.

# Input data

The input file `tablou.in` contains on the first line the number $p = 1$ or $p = 2$, representing the task number to be solved.

* If $p = 1$, then the second line of the input file contains the numbers $N$ and $K$, separated by a space, and the following $K$ lines contain each a capital letter ($L$ or $C$) and a number $nr$, separated by a space, representing the coding of one of the two operations ($L \ nr$ or $C \ nr$).
* If $p = 2$, then the second line of the input file contains the numbers $N$ and $Z$, separated by a space.

# Output data

* If $p = 1$, then the output file `tablou.out` contains on the first line a natural number, representing the number of positive values in the resulting table at the end of executing the $K$ operations on the initial table (answer to task $1$).
* If $p = 2$, then the output file `tablou.out` contains on the first line a natural number representing the minimum number of operations $L \ nr$ or $C \ nr$, which, applied to the initial table, modify it so that the resulting table contains exactly $Z$ negative values (answer to task $2$). If it is not possible to obtain a table with $Z$ negative values by applying $L \ nr$ or $C \ nr$ operations to the initial table, then the file will contain on the first line the value $0$ (zero).

# Constraints and clarifications

* $N, K, Z$ and $nr$ are natural numbers
* $3 \leq N \leq 20\ 000$; $1 \leq K \leq 43\ 000$; $1 \leq Z \leq N \cdot N$; $1 \leq nr \leq N$;
* By changing the sign, the value $-1$ turns into $1$ and the value $1$ turns into $-1$
* $10$ points are awarded officially and $45$ points each for the correct resolution of each task.

# Example 1

`tablou.in`
```
1
4 4
L 1
L 3
C 1
L 1
```

`tablou.out`
```
10
```

## Explanation

$N = 4$. At the end of applying the sequence of $K = 4$ operations, the modified table has the content:

```
-1  1  1  1
-1  1  1  1
 1 -1 -1 -1
-1  1  1  1
```

Thus, the table contains $10$ positive values.

# Example 2

`tablou.in`
```
2
3 5
```

`tablou.out`
```
3
```

## Explanation

A minimum of $3$ operations is necessary, for example:

$L \ 3$
$L \ 1$
$C \ 1$

# Example 3

`tablou.in`
```
2
4 7
```

`tablou.out`
```
0
```

## Explanation

There is no sequence of operations for which $Z = 7$ negative values can be obtained.


