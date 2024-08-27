## 2-3-monotone Sequences

Let $N$ $(N \leq 1000)$ be a natural number. We define a 2-3-monotone sequence of length $N$ as a sequence $S_1 , S_2 , S_3 , \dots S_n$ consisting of $N$ elements from the set $\{1, 2, \dots N\}$ that satisfy the following two relations:

$S_i$ < $S_{i+2}$, for any $1 \leq i \leq N-2$

$S_i$ < $S_{i+3}$, for any $1 \leq i \leq N-3$ 

## Task

Let $X$ be the number of 2-3-monotone sequences of length $N$. Calculate the remainder of $X$ when divided by $1\000\000$ (1 million).

## Input data

The file `sir23.in` will contain on the first line the integer number $N$.

## Output data

The file `sir23.out` will contain the desired number on the first line.

## Examples

`sir23.in`
```
2
```

`sir23.out`
```
4
```

`sir23.in`
```
3
```

`sir23.out`
```
9
```

`sir23.in`
```
5
```

`sir23.out`
```
88
```