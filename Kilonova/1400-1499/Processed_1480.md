
Given a sequence $a_1$, $a_2$, $...$, $a_n$ of natural numbers, where $n$ is odd. We have a single allowed operation: we can add the same non-zero natural value to two different positions in the sequence.

# Task

1. Verify if the sequence can have all elements equal after applying a single operation.
2. Using the allowed operation multiple times, obtain the sequence with all elements equal, but the equal value obtained should not exceed twice the maximum value from the initial sequence.

# Input data

The file `perechi.in` contains, on the first line, a natural number $C$, the second line contains the number $n$, and on the third line, separated by a space, the values $a_1$, $a_2$, $...$, $a_n$.

# Output data

The file `perechi.out` will contain:

1. If $C = 1$, then only the first task will be solved, so the first line will contain the value $0$ if it is not possible to make all elements of the sequence equal, or three natural numbers $i \\ j \\ v$ meaning: add the value $v$ to positions $i$ and $j$ in the sequence to make all elements of the array equal.
2. If $C = 2$, then only the second task will be solved. Each line of the output file will contain exactly three values $i \\ j \\ v$ meaning: add the value $v$ to $a_i$ and $a_j$ (where $i$ and $j$ are distinct and range from $1$ to $n$).

# Constraints and clarifications

* $5 \leq n \lt 2 \ 000$, $n$ is odd
* $0 \leq a_i \leq 100 \ 000 \ 000$, for any $1 \leq i \leq n$
* The elements of the initial sequence are not necessarily distinct, but they are not all equal either
* If there are multiple solutions, you can output any of them.
* If the number of applied operations is less than or equal to $n$, and the final value is at most twice the initial maximum, and the result of applying the operations produces a sequence with the same value, you will receive $100\\%$ of the points.
* If the number of operations is between $n+1$ and $2 \cdot n$, and the final value is at most twice the initial maximum, and the result of applying the operations produces a sequence with the same value, you will receive $70\\%$ of the points.
* If the number of operations is more than $2n$ or if the final value exceeds twice the initial maximum, then you will receive $0$ points. Also, if as a result of the applied operations the sequence does not become uniform, or if you apply an operation where positions $i$ and $j$ are not in the range $1 ... n$, then you will also receive $0$ points.
* For tests worth $20$ points we will have $C = 1$. For the rest of the tests we will have $C = 2$, of which for $30$ points the sequence will consist of distinct numbers ranging from $1$ to $n$.

# Example 1

`perechi.in`
```
1
5
8 2 8 8 2
```

`perechi.out`
```
2 5 6
```

## Explanation

$C = 1$, so only the first task will be solved! By adding the value $6$ to positions $2$ and $5$ we obtain the constant sequence $8$, $8$, $8$, $8$, $8$.

# Example 2

`perechi.in`
```
2
5
8 5 6 3 10
```

`perechi.out`
```
1 2 2
3 4 4
2 4 3
```

## Explanation

$C = 2$, so only the second task will be solved! The maximum value in the sequence is $10$, so the final value must be at most $20$. A maximum of $5$ operations must be carried out for $100$ points.
Performing the operation $1$, $2$, $2$ we obtain the sequence $10$, $7$, $6$, $3$, $10$
Performing the operation $3$, $4$, $4$ we obtain the sequence $10$, $7$, $10$, $7$, $10$
Performing the operation $2$, $4$, $3$ we obtain the sequence $10$, $10$, $10$, $10$, $10$

# Example 3

`perechi.in`
```
1
5
8 2 7 8 2
```

`perechi.out`
```
0
```

## Explanation

$C = 1$, so only the first task will be solved! It is not possible to perform a single operation so that all elements of the sequence become equal.

# Example 4

`perechi.in`
```
2
3
1 2 3
```

`perechi.out`
```
1 3 1
1 2 2
```

## Explanation

$C = 2$, so only the second task will be solved! The maximum value in the sequence is $3$, so the final value must be at most $6$. A maximum of $3$ operations must be carried out for $100$ points.
Performing the operation $1$, $3$, $1$, we obtain the sequence $2$, $2$, $4$
Performing the operation $1$, $2$, $2$, we obtain the sequence $4$, $4$, $4$
