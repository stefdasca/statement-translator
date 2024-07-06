```markdown
# Task

An array is a sequence of natural numbers. Initially, there are $N$ arrays, numbered from $1$ to $N$, each containing a single natural number. Then, other $M$ arrays are defined (numbered from $N+1$ to $N+M$). The array $i$ ($N+1 \leq i \leq N+M$) is obtained by concatenating the arrays with numbers $a(i)$ and $b(i)$. By concatenation we mean adding the elements of $b(i)$, in order, after the last element of $a(i)$. After concatenation, the arrays $a(i)$ and $b(i)$ are not modified (practically, only a new array is created without modifying the existing arrays).

Considering the $N+M$ arrays defined earlier, you must answer $Q$ queries of type $(i,p)$, meaning: What is the number at position $p$ in the array with number $i$? The numbers in an array are numbered from $1$ to the number of elements in the array.

# Input data

The first line of the input file `carray.in` contains three natural numbers: $N$, $M$, and $Q$. The next $N$ lines contain each a natural number. The number on the $i$-th of these lines represents the number contained in array $i$.

The next $M$ lines contain each two natural numbers. The $i$-th of these $M$ lines contains the values $a(N+i)$ and $b(N+i)$ (based on which array $N+i$ is constructed).

The next $Q$ lines contain each two natural numbers $i$ and $p$, representing a query $(i,p)$.

# Output data

In the output file `carray.out`, print, in order, for each query $(i,p)$ from the input file, the number that is at position $p$ in the array $i$.

# Constraints and clarifications

* $1 \leq N \leq 20\ 000$
* $0 \leq M \leq 500\ 000$
* $1 \leq Q \leq 20\ 000$
* $1 \leq a(i) < i$ and $1 \leq b(i) < i$ (for $N+1 \leq i \leq N + M$)
* In tests, the number of elements of each array will be at most $10^{16}$.
* The argument $i$ of a query $(i, p)$ is between $1$ and $N+M$.
* The argument $p$ of a query $(i, p)$ is between $1$ and the number of elements in array $i$.
* The natural number contained by each of the arrays $1, \ldots, N$ is between $0$ and $100\ 000\ 000$.

# Example

`carray.in`
```
3 4 5
3
6
9
1 2
4 2
5 5
6 3
1 1
4 2
5 2
6 4
7 6
```

`carray.out`
```
3
6
6
3
6
```

## Explanation

Arrays $4$, $5$, $6$, and $7$ contain the following elements, in order:
* array $4$: $3, 6$
* array $5$: $3, 6, 6$
* array $6$: $3, 6, 6, 3, 6, 6$
* array $7$: $3, 6, 6, 3, 6, 6, 9$
```

I have carefully translated and double-checked the statement for potential grammatical or syntactical errors.
