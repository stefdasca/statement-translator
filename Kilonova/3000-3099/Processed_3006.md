Gigel is playing with numbers again. He cuts a natural number into smaller pieces and sums up the pieces, noticing that different sums can be obtained. Obviously, if he rotates the digits of the number to the left or right and repeats the cutting operation, different sums are obtained. For example, the number $12345$ can be cut into pieces $1$, $2$, $3$, and $45$ or, if the number is rotated to the right by $2$ positions to get $45123$, it can be cut into pieces $4$, $512$, and $3$, and so on. He establishes the following properties for a cutting:

- only one of the pieces must contain at least two digits;
- the pieces can only be made up of zeros or start with the digit zero;
- after applying the cutting, at least $3$ pieces must be obtained;
- the *cost* of a cut is equal to the sum of the pieces obtained.

A *special cut* is a cut that also meets the following two conditions:
- the pieces have at most three digits;
- the *cost* is a prime number.

# Task

Write a program that reads a natural number and determines:
1. the maximum cost of a cut
2. the minimum cost of a *special cut*

# Input data

The input file `bucati.in` contains on the first line the task ($1$ or $2$). The next line contains a natural number $n$.

# Output data

The output file `bucati.out` will contain a single line with a natural number determined according to the task.

# Constraints and clarifications

* $999 < n < 1\ 000\ 000\ 000$
* For the test data, the existence of a solution is guaranteed
* $36$ points are awarded for task $1$, $54$ points for task $2$; $10$ points are awarded by default

# Example 1

`bucati.in`
```
1
12353
```

`bucati.out`
```
536
```

## Explanation

The task is $1$, and the maximum cost of a cut must be determined. The maximum cost is obtained for the number $53123$, obtained by rotating the initial number two times to the right, which is divided into pieces $531\ 2\ 3$. The cost obtained is: $536$

# Example 2

`bucati.in`
```
2
12533
```

`bucati.out`
```
23
```

## Explanation

The task is $2$, and the minimum cost of a special cut must be determined. It can be observed that there are multiple solutions to obtain the minimum cost $12\ 5\ 3\ 3$; $3\ 12\ 5\ 3$; $3\ 3\ 12\ 5$; $5\ 3\ 3\ 12$.

# Example 3

`bucati.in`
```
2
78409
```

`bucati.out`
```
109
```

## Explanation

The task is $2$, and the minimum cost of a special cut must be determined. The pieces are obtained from the number $84097$ obtained by rotating to the left by one position: $8\ 4\ 0\ 97$

# Example 4

`bucati.in`
```
2
908834033
```

`bucati.out`
```
857
```

## Explanation

The task is $2$, and the minimum cost of a special cut must be determined. The pieces can be: $9\ 0\ 8\ 834\ 0\ 3\ 3$