## Task
Given a number $N$ in base 10. A number $M$ is called close to $N$ if it meets the following three conditions:
1) It has the same number of digits as $N$.
2) Its representation in base 10 differs from that of $N$ in exactly one position. In other words, not more, not less, a single digit differs.
3) This digit is either $1$ smaller or $1$ larger than the corresponding digit in $N$.

For example, suppose $N = 1903$. An example of a number $M$ that is close to $N$ is $1913$, because it differs (only) in the tens place, and the difference between $0$ (the tens digit in $N$) and $1$ (the tens digit in $M$) is $1$. The numbers $1903$, $903$, and $1893$ are not close to $N$.

## Task
Knowing the number $N$, write a program that determines:
1) the number of digits of this number;
2) the number of numbers close to $N$;
3) the number of numbers close to at least one number close to $N$.

## Input data
The input file `aproape.in` contains:
1. On the first line, a number $V$ whose value can only be $1$, $2$, or $3$.
2. On the second line, the natural number $N$.

## Output data
If the value of $V$ is $1$, then the output file `aproape.out` will contain a single number representing the number of digits of $N$.

If the value of $V$ is $2$, then the output file `aproape.out` will contain a single number representing the number of numbers close to $N$.

If the value of $V$ is $3$, then the output file `aproape.out` will contain a single number representing the number of numbers close to a number close to $N$.

## Constraints and clarifications
- $0 \leq N < 1\ 000\ 000\ 000$
- For tests worth 20 points, we have $V = 1$.
- For tests worth 30 points, we have $V = 2$.
- For tests worth 50 points, we have $V = 3$.
- Make sure not to count any number more than once!

## Examples
`aproape.in`
```
1
1903
```
`aproape.out`
```
4
```
\
`aproape.in`
```
2
1903
```
`aproape.out`
```
5
```
Numbers close to $1903$ are: $1803$, $1902$, $1904$, $1913$, and $2903$.
\
`aproape.in`
```
3
1903
```
`aproape.out`
```
15
```
The 15 numbers are: $1703$, $1802$, $1804$, $1813$, $1901$, $1903$, $1905$, $1912$, $1914$, $1923$, $2803$, $2902$, $2904$, $2913$, and $3903$.