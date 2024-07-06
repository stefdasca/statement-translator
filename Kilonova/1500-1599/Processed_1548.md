Given the Fibonacci sequence defined by $F_1$ = 1, $F_2$ = 1 and the recurrence relation $F_k = F_{k-1} + F_{k-2}, \\ k \geq 3$. Consider a natural number $N$.

# Task

Write a program that determines the number $F$ of different irreducible subunit fractions that can be formed using the first $N$ terms of the Fibonacci sequence.

# Input data

The input file `fibofrac.in` contains on the first line the number $N$.

# Output data

The output file `fibofrac.out` will contain on the first line the number $F$, with the meaning described above.

# Constraints and clarifications

* $1 \leq N < 1\, 000\, 000$;
* $0 \leq F < 2^{63}$;
* Two irreducible fractions $\frac{a}{b}$ and $\frac{c}{d}$ are different if $a \ne c$ or $b \ne d$;
* For tests worth $24$ points, $1 \leq N < 80$;
* For tests worth $40$ points, $1 \leq N \leq 1\, 100$;
* For tests worth $56$ points, $1 \leq N \leq 50\, 000$.

# Example 1

`fibofrac.in`
```
7
```

`fibofrac.out`
```
14
```

## Explanation

$N=7$; The first $7$ terms of the Fibonacci sequence are: $1, 1, 2, 3, 5, 8, 13$

We can form $14$ different irreducible subunit fractions: $\frac{1}{2}$, $\frac{1}{3}$, $\frac{1}{5}$, $\frac{1}{8}$, $\frac{1}{13}$, $\frac{2}{3}$, $\frac{2}{5}$, $\frac{2}{13}$, $\frac{3}{5}$, $\frac{3}{8}$, $\frac{3}{13}$, $\frac{5}{8}$, $\frac{5}{13}$, $\frac{8}{13}$ 

# Example 2

`fibofrac.in`
```
2019
```

`fibofrac.out`
```
1547722
```

## Explanation

We can form $1547722$ different irreducible subunit fractions using the first $2019$ terms of the Fibonacci sequence.

# Example 3

`fibofrac.in`
```
500000
```

`fibofrac.out`
```
94988288219
```

## Explanation

We can form $94988288219$ different irreducible subunit fractions using the first $500000$ terms of the Fibonacci sequence.