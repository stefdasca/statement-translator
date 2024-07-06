# Task

Consider the notation $[x; y]$, representing a sequence of non-zero natural numbers $x, x + 1, x + 2, \ldots, y$ with $x \leq y$.

We say that the sequence $[p; q]$ includes the sequence $[a; b]$ if the relation $p \leq a \leq b \leq q$ holds.

We are given $N$ _special_ sequences of the form $[a; b]$ and then $T$ _query_ sequences $[L; R]$. Any sequence that includes at least one special sequence is called a _super-special_ sequence. The number of super-special sequences that a sequence $[L; R]$ includes is called the _capacity of the sequence_ $[L; R]$.

# Task

For each query sequence, determine its capacity.

# Input data

The input file `secvente.in` contains:

- The first line contains the natural number $N$, representing the number of special sequences.
- The next $N$ lines each contain two non-zero natural numbers $a$ and $b$, separated by a space, representing the special sequences.
- On line $N+2$ contains the natural number $T$, representing the number of query sequences.
- The next $T$ lines each contain two non-zero natural numbers $L$ and $R$, separated by a space, representing the query sequences.

# Output data

The output file `secvente.out` will contain $T$ lines. On the $i$-th line of the file, there will be a single natural number representing the capacity of the $i$-th query sequence, in the order from the input file.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq a \leq b \leq 1\ 000\ 000\ 000$
* $1 \leq T \leq 100\ 000$
* $1 \leq L \leq R \leq 1\ 000\ 000\ 000$
* For tests worth $79$ points, $b \leq 1\ 000\ 000$
* For tests worth $32$ points, $N, T \leq 10\ 000$

# Example 1

`secvente.in`
```
2
2 4
3 3
3
2 4
1 5
2 5
```

`secvente.out`
```
4
9
6
```

## Explanation

The query sequence $[2;4]$ includes the super-special sequences $[2;3]$, $[2;4]$, $[3;3]$, and $[3;4]$. Note that $[2;2]$ is not a super-special sequence because it does not include either of the two special sequences ($[2; 4]$ and $[3; 3]$).

The query sequence $[1;5]$ includes the super-special sequences $[1;3]$, $[1;4]$, $[1;5]$, $[2;3]$, $[2;4]$, $[2;5]$, $[3;3]$, $[3;4]$, and $[3;5]$.

The query sequence $[2;5]$ includes the super-special sequences $[2;3]$, $[2;4]$, $[2;5]$, $[3;3]$, $[3;4]$, and $[3;5]$.