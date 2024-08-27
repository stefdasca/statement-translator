## Task

Gigel is in love with arithmetic progressions. He thinks about them all day, so when he saw the problem Progressions 2, he couldn't be happier. He wanted to know exactly how many arithmetic progressions of a certain length $N$ he could form with numbers from $1$ to $V$. Shortly after, however, he realized that the solution to that problem was not useful to him at all because he has $K$ numbers that he does not like, so he would like not to see them in any arithmetic progression. These $K$ numbers are quite close to each other, the largest distance between them being at most $50\ 000.$ Given $V$, $N$, and the $K$ numbers, you must tell Gigel how many arithmetic progressions with positive ratio of length $N$ can be formed with the numbers from $1$ to $V$ minus the $K$ given numbers. In return, he will give you $100$ points. Because this number can be quite large, Gigel only wants the remainder of this number when divided by $1\ 000\ 000\ 009$ (one billion and nine).

## Input data

The input file `progresii3.in` will contain 3 natural numbers $V$, $N$, and $K$ on the first line. The next line will contain $K$ natural numbers $A_1$, $A_2$, $\dots$, $A_K$ representing the $K$ numbers that Gigel does not like.

## Output data

The output file `progresii3.out` must contain a single natural number, the number of arithmetic progressions of length $N$ which contains numbers from $1$ to $V$ minus the $K$ given numbers in the input file.

## Constraints

$2 \leq V \leq 1\ 000\ 000\ 000\ 000$ $(10^{12})$

$2 \leq N \leq 5000$

$1 \leq K \leq 50$

$K, N \leq V$

For $20$ points

$V \leq 100\ 000,$

$N \leq 50,$

$K \leq 30$

and the maximum distance between any two of the $K$ values is at most $500$

For another $20$ points

$V \leq 10\ 000\ 000,$

$100 \leq N \leq 150,$

$K \leq 30$

and the maximum distance between any two of the $K$ values is at most $500$

For another $20$ points

$N, K \leq 20$

and the maximum distance between any two of the $K$ values is at most $500$

## Example

`progresii3.in`

```
5 2 1
3
```

`progresii3.out`

```
6
```

`progresii3.in`

```
100 10 4
16 25 49 64
```

`progresii3.out`

```
308
```

## Explanation

For the first example, the $6$ arithmetic progressions of $2$ elements formed by the values $\{1, 2, 4, 5\}$ are $(1,2), (1,4), (1,5), (2,4), (2,5), (4,5)$