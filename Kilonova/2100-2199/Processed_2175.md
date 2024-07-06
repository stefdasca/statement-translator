```markdown
# Task

Given the set $M= \{1, 2, 3, \dots , n \}$. We define a *bipermutation of order $n$* as a matrix $a$ with two rows and $n$ columns, in which each number $k$ of the set $M$ appears in the matrix **in two distinct columns** (figures $1$, $2$, $3$, and $4$ each contain a bipermutation, while the matrix in figure $0$ is not a bipermutation).
In a bipermutation we can perform the following operations:
1. Swap two elements in the same column (figure $1 \rightarrow$ figure $2$)
2. Swap two columns (figure $1 \rightarrow$ figure $3$)
3. Swap two distinct values $x$ and $y$ in the bipermutation (figure $1 \rightarrow$ figure $4$)

~[echival.png]

Two bipermutations are equivalent if there exists a sequence of operations through which the first bipermutation can be transformed into the second bipermutation. In the figures above, all four bipermutations are equivalent. 
If two bipermutations are equivalent, they belong to the same *equivalence class*.

Given a natural number $n$, determine the number of distinct equivalence classes modulo $1 \ 114 \ 111$.

# Input data

The input file `echival2.in` contains on the first line the natural number $n$, with the meaning described above.

# Output data

The output file `echival2.out` will contain on the first line the number of equivalence classes modulo $1 \ 114 \ 111$.

# Constraints and clarifications

* $3 \leq n \leq 100 000$;
* The problem is worth $50$ points in the contest.

# Example

`echival2.in`
```
5
```

`echival2.out`
```
2
```

## Explanation

The set of bipermutations of order $5$ decomposes into two equivalence classes.
```

I have translated the problem statement from Romanian to English, maintaining the custom format and checking for grammar and syntax errors.