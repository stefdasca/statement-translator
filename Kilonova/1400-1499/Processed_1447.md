Olivius d’Info received a stack for his birthday and was very happy. He kept thinking about what to do with it and invented a logic game for his classmates.

**In the first phase** he wrote several notes, each containing a permutation of the first $n$ positive natural numbers: $1, 2, 3, ..., n$. The notes contain permutations for different values of $n$.

He classified these permutations into _stacked permutations_ and _unstacked permutations_.

A _permutation_ is _stacked_ if it can be obtained during the insertion into the stack of the numbers $1, 2, 3, ..., n$ in this order, by extracting the elements in the order indicated by the permutation.

An _unstacked permutation_ is a permutation that cannot be obtained through the above process.

According to Olivius' procedure, for $n=4$, the _stacked permutation_ $(2,1,3,4)$ can be obtained as follows:

~[7a64f52198785c1f76a59756661f15f9.png]

The sequences $(3,1,2,4)$ and $(4,2,1,3)$ are _unstacked permutations_.

**In the second phase**, some notes were shortened from the left and/or from the right. Thus, from the _stacked permutation_ $(2,1,3,4)$, shorter sequences can be obtained: $(1,3,4), (2,1,3), (1,3),(3)$, etc.

Any sequence that belongs to a _stacked permutation_ may also belong to an _unstacked permutation_. For example, the sequence $(2,1,3)$ belongs both to the _stacked permutation_ $(2,1,3,4)$ and to the _unstacked permutation_ $(4,2,1,3)$.

# Task

Given several sequences of distinct natural numbers, determine for each of them if they belong to at least one _stacked permutation_.

# Input data

The file `stiva.in` contains a set of five sequences of elements, as follows:

* The first line contains a natural number $k$, representing the number of elements in each of the five sequences;
* Each of the following five lines contains $k$ positive natural numbers, separated by spaces, representing the elements of a sequence.

# Output data

The file `stiva.out` will contain $5$ lines, each line containing one natural number as follows:

* `1` – if the current sequence belongs to a stacked permutation;
* `0` – if the current sequence does not belong to a stacked permutation.

The answers are written on one line each, in the order in which the sequences appear in the input file.

# Constraints and clarifications

* $1 \leq$ value of the elements in the sequence $\leq 2 \ 000 \ 000 \ 000$
* The difference between the largest and the smallest element of the sequence does not exceed $50 \ 000$
* For $50\%$ of the tests, the elements in the sequence do not exceed $50 \ 000$
* The elements in a sequence are distinct two by two.

# Example

`stiva.in`
```
3
1 3 4
2 1 3
3 1 2
1 2 4
1 4 2
```

`stiva.out`
```
1
1
0
1
0
```

## Explanation

$n=3$, we have **five** sequences of numbers, each of length $3$.

* The sequence $(1,3,4)$ belongs to a stacked permutation (correct answer $1$);
* The sequence $(2,1,3)$ belongs to a stacked permutation (correct answer $1$);
* The sequence $(3,1,2)$ does not belong to any stacked permutation (correct answer $0$);
* The sequence $(1,2,4)$ belongs to a stacked permutation (correct answer $1$);
* The sequence $(1,4,2)$ does not belong to any stacked permutation (correct answer $0$).