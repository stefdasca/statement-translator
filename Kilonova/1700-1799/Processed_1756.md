We have a sequence $X$ with $n$ natural numbers given in a base $b$. We need to determine a subsequence of the given sequence that has the following properties:
- Each digit of base $b$: $0$, $1$, $\dots$, $b - 1$, appears, in total, in the numbers of this subsequence the same number of times.
- In any prefix of the determined subsequence, the difference between the number of occurrences of any 2 digits between $0$ and $b - 1$ is at most $k$ (a prefix of the determined subsequence represents a sequence of values from the subsequence starting with the first element of the subsequence).

# Task

Determine the maximum number of elements of such a subsequence.

# Input data

The first line of the file `ssce.in` contains 3 natural numbers $n$, $b$, $k$, in this order, separated by a space, which have the significance from the statement. The second line contains, separated by a space, $n$ natural numbers, elements of the sequence $X$.

# Output data

The first line of the file `ssce.out` contains a single natural number that represents the required value.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$
* $2 \leq b \leq 4$
* $1 \leq k \leq 5$
* $0 \leq X_i \leq 100 \ 000$ (in base $b$)
* It is guaranteed that in all test files, the elements of sequence $x$ have digits between $0$ and $b - 1$, inclusive.

# Example

`ssce.in`
```
5 2 1
1 10000 100 1111 0
```

`ssce.out`
```
2
```

## Explanation

The solution is given by the elements $1$ and $100$. Both digits of base $b$ appear $2$ times in these numbers. If we considered the subsequence with all elements of the given sequence, the number of occurrences of both digits would be equal but the second constraint would not be met (for example, the prefix of length $2$ of this, formed from $1$ and $10000$, has a difference of $2$ between the number of occurrences of digit $0$ and the number of occurrences of digit $1$).