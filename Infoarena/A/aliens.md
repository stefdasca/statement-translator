## Task

Aliens are among us. Gica has been abducted by aliens. On the mothership, he learns something about their new civilization. He discovers that the mathematics known to these aliens is somewhat limited. By studying their manuals, he finds that they have only discovered numbers that can be written as the product of $2$, $3$, or $5$. Additionally, the aliens are familiar with the number $1$. For example, the aliens know the numbers $45$ or $60$, but not the numbers $11$ or $42$.  
One day, after a long harmonious coexistence, the aliens decide to release Gica, if and only if he demonstrates exceptional intelligence. For this purpose, he is given $N$ fractions of the form $x_i / y_i$ (evidently, all numbers $x_i$ and $y_i$ are known to the aliens) and is asked to choose certain fractions from the $N$ such that the product of the fractions is as large as possible, and, moreover, this product is a natural number. Receiving $N$ fractions with numerators and denominators known to the aliens, determine the fractions that must be selected so that their product is a natural number and is as large as possible.

## Input data

The input file is named `aliens.in`. The first line of this file contains the number $N$. Each of the following $N$ lines contains a pair of numbers known to the aliens, identifying a fraction.

## Output data

The first and only line of the output file `aliens.out` contains the natural number $P$, the maximum product that can be obtained by multiplying some of the given fractions.

## Constraints and clarifications

$1 \leq N \leq 50$

Each given number does not exceed $400000000$

Each fraction can be selected at most once

It is guaranteed that there is at least one solution

## Example

`aliens.in`

```
6
4 15
16 25
30000 729
5 4
10 30
75 2
```

`aliens.out`

```
30
```

## Explanation

The fractions $16/25$, $5/4$ and $75/2$ are selected.