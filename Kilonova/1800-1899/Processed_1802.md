Here is the competitive programming problem statement translated into English:

---

Given a tree with $N$ nodes numbered from $1$ to $N$, rooted at node $1$, and an array $V$, where $V_i$ represents the value of node $i$.

A sequence of length $N$ is called a *permutation of order $N* if it contains all the numbers from $1$ to $N$, in any order. For example, the sequences $[1, 2, 3]$, $[2, 1, 3]$, and $[3, 2, 1]$ are permutations of order $3$, but the sequences $[1, 4, 3]$ and $[1, 2, 2]$ are not.

# Task

You are given $Q$ queries of the type: If we form a sequence with all the values of the nodes in the subtree of node $X$, is this sequence a permutation of order $K$, where $K$ represents the number of nodes in the subtree of node $X$?

Answer these queries.

# Input data

The first line contains the natural number $N$. The next line contains $N$ natural numbers, separated by a space, representing the array $V$. The following lines contain $N - 1$ pairs of natural numbers $(a, b)$, separated by a space, representing that there is an edge between nodes $a$ and $b$. The next line contains the natural number $Q$. The next $Q$ lines contain the nodes $X$, as described above.

# Output data

The next $Q$ lines contain the message `YES` or `NO`, representing the answers to the $Q$ queries.

# Constraints and clarifications

* $1 \leq N, Q \leq 500\ 000$
* $1 \leq a, b \leq N$
* $1 \leq V_i \leq N$, for $1 \leq i \leq N$
* $1 \leq X \leq N$

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|21|$N, Q \leq 100$|
|2|23|The tree is a line|
|3|27|$N, Q \leq 100\ 000$|
|4|29|No additional constraints|

## Note

Due to very large input data, the following instructions should be used at the beginning of the `main()` function in the C++ program:
```c++
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Example

`stdin`
```
8
6 5 4 7 8 2 1 3
1 2
1 3
2 4
2 5
3 6
6 7
6 8
6
1
2
6
3
5
7
```

`stdout`
```
YES
NO
YES
YES
NO
YES
```

## Explanation

For the first query, we can obtain the sequence $[1, 2, 3, 4, 5, 6, 7, 8]$, which is a permutation of order $8$.

For the second query, we can obtain the sequence $[5, 7, 8]$, which is not a permutation of order $3$, because it does not contain all the numbers from $1$ to $3$.

For the last query, we obtain the sequence $[1]$, which is a permutation of order $1$.

