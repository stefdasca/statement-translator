Beauty

Who doesn't like beautiful numbers? Let $N$ be a number in base $10$. We define the beauty degree of $N$ as being the number of sequences of length $2$ full of $1$s existing in its binary representation. For example: $11$ $(10)$ = $1011$ $(2)$, so the beauty degree of $11$ is $1$. $27$ $(10)$ = $11011$ $(2)$, so the beauty degree of $27$ is $2$. $15$ $(10)$ = $1111$ $(2)$, so the beauty degree of $15$ is $3$. We are given $T$ - the number of tests, and for each test two natural numbers, $K$ and $N$. For each test, answer the following question: How many natural numbers $X$, $0 \leq X \leq N$, have a beauty degree equal to $K$? The answer must be provided modulo $666013$.

## Input data

The input file `frumusete.in` contains on the first line the natural number $T$. On each of the next $T$ lines, there will be two natural numbers, $K$ and $N$, having the significance from the statement. Because we are in the holiday season, the number $N$ is given to you in base $2$.

## Output data

In the output file `frumusete.out`, there will be $T$ lines, each line containing the response for test $i$.

## Constraints and clarifications

$T = 20\,000$

$0 \leq K \leq 1\,000$

$0 \leq N < 2^{1\,000}$

We recommend using `gets` to read the numbers from the input file, not `cin`.

## Example

`frumusete.in`

```
3
3 11111
4 1010101
0 10
```

`frumusete.out`

```
2
2
3
```

## Explanation

There are two numbers less than or equal to $31 = 11111$ with a beauty degree of $3$: $15 = 1111$ and $30 = 11110$. There are two numbers less than or equal to $85 = 1010101$ with a beauty degree of $4$: $31 = 11111$ and $62 = 111110$. There are three numbers less than or equal to $2 = 10$ with a beauty degree of $0$: $0 = 0$, $1 = 1$, $2 = 10$.