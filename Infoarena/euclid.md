Euclid

Euclid was a clever man who knew that the era of computing machines would come one day. He knew that people would organize competitions on these machines, so he wanted to contribute with a puzzle. Given a matrix of $m$ rows and $n$ columns of positive integers, find a rectangle with height at least $h$ and width at least $w$, such that the numbers within the rectangle have the largest gcd among all such rectangles.

## Task

## Input data

The input file will start with a line containing the number of tests, $T$. Each test will begin with a line containing $m$, $n$, $h$ and $w$. Next, there will be $m$ lines each containing $n$ positive integers, describing the above matrix.

## Output data

For each output file, contain one line containing "Case #$x$: ", followed by the largest gcd ($x$ represents the test number).

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq h \leq m$

$1 \leq w \leq n$

$1 \leq m,n \leq 400$

the numbers in the matrix are between $1$ and $10^9$

## Example

`euclid.in`

`3`

`2 2 1 1`

`1 2`

`3 4`

`3 3 3 1`

`1 2 3`

`4 5 6`

`7 8 9`

`2 2 2 2`

`1000000000 1000000000`

`1000000000 1000000000`

`euclid.out`

`Case #1: 4`

`Case #2: 3`

`Case #3: 1000000000`

## Explanation

For the first example, it is evident that the rectangle with the maximum gcd contains only the cell at coordinates $(1, 1)$ (coordinates are numbered from $0$).

For the second example, the rectangle with the maximum gcd is formed from the last column of the matrix; there is no other rectangle of greater or equal size that has a larger gcd.

In the case of the last example, we can choose the entire matrix.