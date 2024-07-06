For a non-zero natural number, we define its factorial as the product of all non-zero natural numbers less than or equal to it, and we denote it $N!$ (that is, $N! = 1 \cdot 2 \cdot \ldots \cdot N$). For a numerical base $B$ and a non-zero natural number $N$, we need to determine the last non-zero digit of the representation in base $B$ of $N!$.

# Task

We read $5$ pairs of the form $(N_i, B_i)$, where $1 \leq i \leq 5$. For each of the $5$ pairs read, determine the last non-zero digit of the representation in base $B_i$ of the factorial of the number $N_i$.

# Input data

The input file `fact.in` contains $5$ lines, each containing two non-zero natural numbers $N_i$ and $B_i$, written in base $10$, separated by a space.

# Output data

The output file `fact.out` will contain $5$ lines. Line $i$ will contain the digit corresponding to a pair $(N_i, B_i)$ read from line $i$ of the input file.

# Constraints and clarifications

* $1 \leq N_i \leq 1\ 000\ 000$, for $1 \leq i \leq 5$;
* $2 \leq B_i \leq 36$, for $1 \leq i \leq 5$;
* If $B_i > 10$, digits greater than $9$ will be represented by capital letters of the English alphabet $(10='A', 11='B', \ldots, 35='Z')$;
* A test will be scored only if all $5$ required results are correct.

# Example

`fact.in`
```
5 10
7 10
7 20
8 16
9 8
```

`fact.out`
```
2
4
C
8
6
```

## Explanation

$5! = 120$, in base $10$, so the last non-zero digit is $2$;
$7! = 5040$, in base $10$, so the last non-zero digit is $4$;
$7! = CC0$, in base $20$, so the last non-zero digit is $C$;
$8! = 9D80$, in base $16$, so the last non-zero digit is $8$;
$9! = 1304600$, in base $8$, so the last non-zero digit is $6$.