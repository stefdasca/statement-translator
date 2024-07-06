Sure, here is your translated text:

A numeric indicator is an electronic display device intended for displaying a **digit**. It contains 7 segments labeled `a`, `b`, `c`, `d`, `e`, `f`, `g`, as in the adjacent figure.

Displaying a digit is done by lighting up a combination of segments:
~[0.png|width=10em|align=right]
- Digit 0: `a`, `b`, `c`, `d`, `e`, `f`
- Digit 1: `b`, `c`
- Digit 2: `a`, `b`, `d`, `e`, `g`
- Digit 3: `a`, `b`, `c`, `d`, `g`
- Digit 4: `b`, `c`, `f`, `g`
- Digit 5: `a`, `c`, `d`, `f`, `g`
- Digit 6: `a`, `c`, `d`, `e`, `f`, `g`
- Digit 7: `a`, `b`, `c`
- Digit 8: `a`, `b`, `c`, `d`, `e`, `f`, `g`
- Digit 9: `a`, `b`, `c`, `d`, `f`, `g`

# Task
Given a natural number $N$ displayed using several numeric indicators, write a program that determines:
1. The number of lit segments to display the number $N$.
2. The number of distinct numbers **greater** than $N$ that can be formed by lighting at least one additional segment compared to those used to display the number $N$, without using other numeric indicators and without turning off any of the already lit segments.

# Input data
The input file is `cifre.in`.

The first line of the input file contains the natural number $V$ whose value can only be $1$ or $2$.

The second line of the input file contains the natural number $N$.

# Output data
The output file is `cifre.out`.

If the value of $V$ is $1$, then the output file will contain on the first line a single natural number that represents the number of lit segments to display the number $N$.

If the value of $V$ is $2$, then the output file will contain on the first line a single natural number representing the number of distinct numbers greater than $N$ that can be formed by lighting at least one additional segment compared to those used to display the number $N$, without using other numeric indicators.

# Constraints and clarifications
- $10 \leq N \leq 10^{19}$
- $20\%$ of the tests will have $V = 1$, and $80\%$ of the tests will have $V = 2$.

# Example 1
`cifre.in`
```
1
823
```
`cifre.out`
```
17
```
## Explanation
$V = 1$, so **ONLY** the first task is solved. $N = 823$.

To display the digit $8$, $7$ segments are lit, to display the digit $2$, $5$ segments are lit, and for the digit $3$, also $5$ segments are lit. In total, $17$ segments are lit.

# Example 2
`cifre.in`
```
2
823
```
`cifre.out`
```
5
```
## Explanation
**V = 2**, so **ONLY** the second task is solved. $N = 823$.

From the digit $8$, no other digits can be obtained by lighting new segments.
From the digit $2$, digit $8$ can be obtained by lighting new segments.
From the digit $3$, digits $8$ and $9$ can be obtained by lighting new segments.

Therefore, $5$ numbers greater than $823$ can be obtained, namely $828$, $829$, $883$, $888$, $889$.