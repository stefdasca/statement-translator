# Task

Lavinia has an affinity for permutations, so she and Andrei proposed the following game:
Given a number $N$ and $N+1$ elements from the set $\{0, 1, -1\}$, you must generate a permutation of length $2 \cdot N + 1$, which satisfies the following conditions:

* If the element $x$ from the given sequence is $0$, the median of the first $2 \cdot x - 1$ elements of the permutation must be equal to the mean of the first $2 \cdot x - 1$ elements of the permutation.
* If the element $x$ from the given sequence is $1$, the median of the first $2 \cdot x - 1$ elements of the permutation must be less than the mean of the first $2 \cdot x - 1$ elements of the permutation.
* If the element $x$ from the given sequence is $-1$, the median of the first $2 \cdot x - 1$ elements of the permutation must be greater than the mean of the first $2 \cdot x - 1$ elements of the permutation.

# Input data

The input file `permutare.in` contains the natural number $N$ as mentioned above. The next line will contain $N + 1$ numbers from the set $\{0, 1, -1\}$ with the meaning mentioned above.

# Output data

The output file `permutare.out` must contain $2 \cdot N + 1$ natural numbers representing the required permutation's elements.

# Constraints and clarifications

* $N \leq 100 \ 000$
* For $50\%$ of the tests $N \leq 2 \ 000$

# Example

`permutare.in`
```
4
0 -1 0 1 0
```

`permutare.out`
```
3 5 6 7 4 9 2 1 8
```

## Explanation

For the first $3$ elements, the mean is $\frac{14}{3} = 4.66$, and the median is $5$, so the median is greater than the mean.
For the first $5$ elements, the mean is $\frac{25}{5}$, and the median is $5$, so the median is equal to the mean.
For the first $7$ elements, the mean is $\frac{36}{7} = 5.14$, and the median is $5$, so the mean is greater than the median.