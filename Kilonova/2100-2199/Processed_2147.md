
We consider an array $A$ with $N$ natural numbers and the position $pos$ as the first position in the array $A$. Upon this array, $M$ operations will be performed in order, of the form:
* ``1``: $pos$ becomes $pos - 1$. If $pos = 1$ before the operation, then the operation is ignored.
* ``2``: $pos$ becomes $pos + 1$. If $pos = N$ before the operation, then the operation is ignored.
* ``3 x``: The natural number $x$ is inserted at position $pos$ in the array $A$, and $N$ becomes $N + 1$. 
* ``4``: The number at position $pos$ is deleted from the array $A$, and $N$ becomes $N - 1$. If $pos = N$ before the operation, then $pos$ becomes $pos - 1$.
* ``5``: The number at position $pos$ is displayed.

# Task

Determine the values displayed in operation ``5``.

# Input data

The first line contains $N$ and $M$ separated by a space. The next line contains $N$ natural numbers, separated by a space, representing the elements of the array $A$. The next $M$ lines contain the operations, as described above. 

# Output data

The first line will contain the values displayed in operation ``5``, separated by a space.

# Constraints and clarifications

* $1 \leq N \leq 10^5$
* $1 \leq M \leq 4 \cdot 10^5$
* $0 \leq A_i \leq 10^9$, for each $1 \leq i \leq N$
* $0 \leq x \leq 10^9$
* It is guaranteed that the array $A$ will never be empty.
* The array $A$ is indexed from 1.

|#|Points|Constraints|
|-|-|-----------|
|0|0|Example|
|1|30|$1 \leq N \leq 500$, $1 \leq M \leq 1\ 000$|
|2|70|No additional constraints|

# Example

`stdin`
```
3 8
2 4 3
2
3 0
1
4
5
2
2
5
```

`stdout`
```
0 3
```

## Explanation
In this example, $N = 3$, $M = 8$, $A = [2, 4, 3]$ and $pos = 1$.
* After the first operation, $pos = 2$.
* After the second operation, $A = [2, 0, 4, 3]$ and $N = 4$.
* After the third operation, $0$ will be displayed.
* After the fourth operation, $pos = 1$.
* After the fifth operation, $A = [0, 4, 3]$ and $N = 3$.
* After the sixth operation, $pos = 2$.
* After the seventh operation, $pos = 3$
* After the eighth operation, $3$ will be displayed.
