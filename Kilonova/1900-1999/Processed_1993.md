```markdown
# Task

You are given a sequence of $N$ natural numbers, which must be sorted in ascending order. The only allowed operation is to consider elements from positions $i, i+1, \dots, j$ (for arbitrary $i$ and $j$, $i<j$), and reverse the order of these elements (i.e., the element at position $i$ moves to position $j$, $i+1$ moves to position $j-1$, $\\dots$, $j$ moves to position $i$). The cost of such an operation is the number of elements in the reversed subsequence, specifically $j-i+1$.

Write a program that determines a sequence of operations that sorts the given sequence in ascending order with a total cost as low as possible (but not necessarily minimal).

# Input data

The input file `invsort.in` contains on the first line the number $N$, and then $N$ lines with the elements of the given sequence (not necessarily distinct).

# Output data

The output file `invsort.out` will contain on each line the description of an operation. An operation is described by the numbers $i$ and $j$, separated by a space. These numbers satisfy $1 \leq i < j \leq N$.

# Constraints and clarifications

* $2 \leq N \leq 32 \ 000$
* the values of the sequence to be sorted are between $0$ and $31 \ 999$
* if the sequence of operations (executed in the order from the output file) does not sort the input, you receive $0$ points
* if the total cost is at most $4 \ 000 \ 000$ (four million), you receive maximum points
* if the total cost is at most $40 \ 000 \ 000$ (forty million), you receive $40\%$ of the test's score
* in $50\%$ of the tests the input sequence contains only the elements $0$ and $1$
* for all tests used for correction, $N = 32 \ 000$

# Example

`invsort.in`
```
5
1
0
1
1
0
```

`invsort.out`
```
3 5
1 3
```

## Explanation

* the first operation has the effect: $1 \ 0 \ [1 \ 1 \ 0] \rightarrow 1 \ 0 \ 0 \ 1 \ 1$
* the second operation has the effect: $[1 \ 0 \ 0] \ 1 \ 1 \rightarrow 0 \ 0 \ 1 \ 1 \ 1$
* the total cost is $3 + 3 = 6$
```

Double-checked and translated correctly while preserving the structure and custom image format.
