# Powers

Let $M = \{ 2^i \cdot 3^j \cdot 5^k \mid i, j, k \; \; \text{natural numbers} \}$. You are given $N$ numbers, each belonging to the set $M$. Determine how many pairs of numbers can be selected from these $N$ such that the product of the numbers in the pair is a power. A natural number $X$ is a power if and only if there exist natural numbers $a$ and $b$ such that $X = a^b$ and $b > 1$.

## Input data

The first line of the file `puteri.in` contains $N$, the number of given numbers. Each of the next $N$ lines contains a triplet of natural numbers $(a, b, c)$ separated by exactly one space. The triplet $(a, b, c)$ on line $i+1$ means: $a$ indicates the power of $2$, $b$ the power of $3$, and $c$ the power of $5$ in the $i$-th given number.

## Output data

The first line of the file `puteri.out` will contain $P$, the number of pairs among the given numbers where the product of the numbers in the pair is a power.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

Any triplet in the input file meets $0 \leq a, b, c \leq 64$

In a triplet, $a$, $b$, and $c$ will not all be zero simultaneously

The given numbers are not necessarily distinct two by two

## Example

`puteri.in`
```
5
1 0 0
1 0 3
2 2 0
0 0 1
2 0 0
```

`puteri.out`
```
3
```

## Explanation

The given numbers are $2$, $250$, $36$, $5$, and $4$. The pairs that meet the given requirements are: $(2, 4)$, $(250, 4)$, and $(36, 4)$. For the first pair, the product is $8 = 2^3$, for the second $1000 = 10^3$, and for the last pair $144 = 12^2$.