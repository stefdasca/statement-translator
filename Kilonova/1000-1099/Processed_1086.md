# Task

Given two natural numbers $K$ and $S$ and a sequence of $N$ natural numbers $a_1$, $a_2$, $\dots$, $a_N$. A sequence of length $K$ is a subsequence composed of $K$ elements located in consecutive positions in the sequence: $a_i$, $a_{i+1}$, $\dots$, $a_{i+K-1}$. Traversing the sequence from left to right, starting with the first element, the first sequence of length $K$ is removed if the sum of its elements is strictly greater than the number $S$. After the removal, the sequence will have $N - K$ elements: $a_1$, $a_2$, $\dots$, $a_{N-K}$. The deletion operation continues according to the same rules until there are no more sequences that can be removed.

# Task

Write a program that, by reading the numbers $N$, $K$, $S$, and the $N$ elements of the sequence, solves the following tasks:
1. Determine the number of sequences that will be eliminated according to the condition described.
2. Assuming that in the read sequence it is not possible to remove any sequences according to the condition described, the program should determine the number of elements $a_i$ in the sequence with the following property: removing $a_i$ leads to obtaining a sequence in which at least one sequence of $K$ elements with a sum strictly greater than $S$ can be eliminated.

# Input data

The input file `secv.in` contains on the first line a natural number $P$; the number $P$ can have only the value $1$ or the value $2$. The second line contains, in this order, separated by spaces, the numbers $N$, $K$, and $S$. The third line contains, in order, the elements of the sequence, separated by spaces.

# Output data

If the value of $P$ is $1$, only the first task will be solved. In this case, the output file `secv.out` will contain on the first line a natural number representing the number of sequences eliminated.
If the value of $P$ is $2$, only the second task will be solved. In this case, the output file `secv.out` will contain on the first line a natural number representing the number of elements in the sequence that have the property that removing each of them individually would generate a sequence in which at least one sequence of $K$ elements with a sum strictly greater than $S$ can be eliminated.

# Constraints and clarifications

* $0 < K \leq N \leq 1 \ 000 \ 000$ 
* $0 < S \leq 1 \ 000 \ 000 \ 000$
* $0 \leq a_1, a_2, \dots, a_N \leq 1 \ 000$
* Correctly solving the first task will be awarded $40$ points, and correctly solving the second task will be awarded $60$ points.

# Example 1

`secv.in`
```
1
14 3 7
1 2 1 3 1 4 5 2 1 4 1 8 2 3
```

`secv.out`
```
3
```

## Explanation

The first sequence with a sum strictly greater than $7$ starts at position $4$ and consists of the elements $3 \ 1 \ 4$; after removing it, the sequence becomes:
$1$, $2$, $1$, $5$, $2$, $1$, $4$, $1$, $8$, $2$, $3$. The second sequence to be eliminated starts at position $2$ and consists of $2 \ 1 \ 5$; after removing it, the sequence becomes: $1$, $2$, $1$, $4$, $1$, $8$, $2$, $3$. The third sequence to be eliminated starts at position $4$ and consists of the elements $4 \ 1 \ 8$; after removing it, the sequence becomes: $1$, $2$, $1$, $2$, $3$ and no longer contains any sequence of $3$ adjacent elements with a sum greater than $7$.

# Example 2

`secv.in`
```
2
9 7 18
3 3 2 1 3 3 3 3 1
```

`secv.out`
```
2
```

## Explanation

Two elements have this property. If we eliminate the third element, with value $2$, we can obtain the sequence $3$, $3$, $1$, $3$, $3$, $3$, $3$, $1$ which contains a sequence of $7$ elements with a sum strictly greater than $18$, starting with the element at position $1$. If we eliminate the fourth element, with value $1$, we can obtain the sequence $3$, $3$, $2$, $3$, $3$, $3$, $3$, $1$ which contains a sequence of $7$ elements with a sum strictly greater than $18$, starting with the element at position $1$.