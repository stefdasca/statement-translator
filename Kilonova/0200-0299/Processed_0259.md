
A sequence with $n$ integers and $q$ queries of the form $x, y$ is given.

To answer, in order, each query which means: "Remove from the sequence the elements at positions between $x$ and $y$. What is the minimum value among the remaining elements in the sequence?". **ATTENTION! The operation of deleting the numbers with positions between $x$ and $y$ implies replacing the elements with positions strictly greater than $y$, in order, on positions greater than $x$. The number of elements will be reduced by $y-x+1$ after each query.**

# Input data
The first line contains the natural number $n$.

Starting with the second line, there are $n$ integers arranged on one or more lines, separated by spaces, representing the elements of the sequence.

The next line contains the natural number $q$.

The following $q$ lines contain two natural numbers $x$ and $y$, as described above.

# Output data
Print the answers to the $q$ queries in order on $q$ lines.

# Constraints and clarifications
* $1 \leq n \leq 100\ 000$;
* $1 \leq q \lt n$;
* Each value in the sequence is an integer and belongs to the interval $[-10^9, 10^9]$;
* It is guaranteed that after each operation the sequence will never remain empty;
* It is guaranteed that, at each query, $x$ and $y$ refer to existing positions in the sequence at that moment;
* **ATTENTION! The operation of deleting the numbers with positions between $x$ and $y$ implies replacing the elements with positions strictly greater than $y$, in order, on positions greater than $x$. The number of elements will be reduced by $y-x+1$.**

## Subtask 1 (30 points)
* $2 \leq n \leq 1\ 000$

## Subtask 2 (70 points)
* $1\ 001 \leq n \leq 100\ 000$

# Example
`stdin`
```
5
1 5 -4 0 3
3
3 3
3 4
1 1
```
`stdout`
```
0
1
5
```

# Explanation
After deleting the element at the third position, the resulting sequence is $[1, 5, 0, 3]$, so the minimum is $0$.

After deleting the elements at positions $3$ and $4$ from the new sequence, the resulting sequence is $[1, 5]$, so the minimum is $1$.

After deleting the element at the first position, the resulting sequence is $[5]$, so the minimum is $5$.
