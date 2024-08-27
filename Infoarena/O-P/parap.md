## Parap

Given $N$ natural numbers $a_1, a_2, \dots, a_N$. A pair $(a[j], a[k])$ with $1\leq j < k \leq N$ is called a special pair if it has the property that from $a[j]$ and $a[k]$ by "concatenation" a number $X$ is formed in which the digits contained appear an even number of times. For example, the numbers $123$ and $21223$ if concatenated produce the number $12321223$ in which $1$ appears $2$ times, $2$ appears $4$ times, and $3$ appears $2$ times.

## Task

Determine the number of special pairs.

## Input data

The first line of the text file `parap.in` contains the natural number $N$ representing the number of elements in the given sequence. The second line contains the elements of the sequence separated by a space.

## Output data

The first line in the output file `parap.out` will contain a natural number representing the number of special pairs.

## Constraints and clarifications

$2 \leq N \leq 10^5$

$1 \leq a[k] \leq 10^{18}$

## Example

`parap.in`
```
10
4 1 13 5 42 2 1 2 112 212
```

`parap.out`
```
6
```

## Explanation

The special pairs are $(1,1), (1,212), (2,2), (2,112), (1,212), (2,112)$