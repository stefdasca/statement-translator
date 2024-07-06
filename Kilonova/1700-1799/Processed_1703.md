Let $x$ be a subunitary real number with at most $9$ decimal places and $N$ a natural number.

# Task

Determine the irreducible fraction $\\frac{a}{b}$ with the properties:

* best approximates the real number $x$, meaning the expression $|x - \\frac{a}{b}|$ has the minimum value
* $1 \leq b \leq N$

# Input data

The input file `aprox.in` contains in the first line the real number $x$, and in the second line the natural number $N$, with the above meaning.

# Output data

The output file `aprox.out` will contain a single line where the natural numbers $a$ and $b$ representing the numerator and denominator of the sought irreducible fraction will be written, separated by a space.

# Constraints and clarifications

* $0 < x < 1$
* $1 < N < 1\ 000\ 000\ 000$
* For tests worth $14$ points: $1 \leq N \leq 500$
* For other tests worth $31$ points: $1 \leq N \leq 1\ 000\ 000$
* For other tests worth $55$ points: $1\ 000\ 001 \leq N \leq 1\ 000\ 000\ 000$

# Example 1

`aprox.in`
```
0.318
100
```

`aprox.out`
```
7 22
```

## Explanation

The irreducible fraction that best approximates the number $0.318$ and has a denominator less than or equal to $100$ is $\\frac{7}{22}$.

# Example 2

`aprox.in`
```
0.998977661
999999991
```

`aprox.out`
```
756463905 757238059
```

## Explanation

The irreducible fraction that best approximates the number $0.998977661$ and has a denominator less than or equal to $999999991$ is $\\frac{756463905}{757238059}$.