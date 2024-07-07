
We consider a permutation of the set $\{1, 2, \ldots, N\}$. For this permutation, a single type of operation is defined: a subsequence is extracted from the permutation, and the elements of the subsequence are added (in the same order) to the beginning of the permutation. For example, for the permutation $(3, 1, 5, 2, 6, 4)$, the subsequence $(1, 2, 4)$ can be chosen, which is then inserted at the beginning of the permutation, obtaining $(1, 2, 4, 3, 5, 6)$.

# Task

Sort the elements of the permutation by performing as few operations as possible (not necessarily the minimum number).

# Input data

The file `specsort.in` contains on the first line the natural number $N$, and on the second line, separated by a space, the $N$ elements of the permutation.

# Output data

The file `specsort.out` contains a number of lines equal to the number of operations performed. On the $i$-th of these lines, there are $N$ natural numbers separated by a space, representing the permutation obtained after applying the $i$-th operation.

# Constraints and clarifications

* $1 \leq N \leq 50\ 000$
* The last line of the file must contain the sorted permutation.

# Example

`specsort.in`
```
7
7 4 5 1 3 6 2
```

`specsort.out`
```
6 7 4 5 1 3 2
4 5 6 7 1 3 2
1 2 4 5 6 7 3
1 2 3 4 5 6 7
```

## Explanation

The subsequences moved at each operation are:

$6$
$4 \ 5$
$1 \ 2$
$1 \ 2 \ 3$
```

I have translated the entire text, and preserved the mathematical values, variable names, general syntax, structure, and format as instructed. Please let me know if there are any additional modifications or checks needed!