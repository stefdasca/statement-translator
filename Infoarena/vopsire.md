# Painting

GS (The Supreme Gecko) has made an introspection into the social construction of reality and started painting fences. More precisely, GS has $M$ sets of interval boundaries $x_1$, $x_2$, $y_1$ and $y_2$ (with $x_1 < x_2$ and $y_1 < y_2$). Additionally, GS has $N$ intervals represented by $x$ and $y$. We say that an interval $x y$ matches a set of interval boundaries $x_1 x_2 y_1 y_2$ if $x_1 \leq x \leq x_2$ and $y_1 \leq y \leq y_2$. GS wants to know for each of the $N$ intervals how many of the $M$ sets of interval boundaries match it.

## Input data

The input file `vopsire.in` contains on the first line two numbers $M$ and $N$, as described in the statement. On the next $M$ lines, there are 4 numbers representing the interval boundaries, $x_1 x_2 y_1 y_2$. On the next $N$ lines, there are two numbers representing the intervals $x y$. 

## Output data

The output file `vopsire.out` will contain $N$ lines. On line $i$, it will contain the number of sets of interval boundaries that match the $i$-th interval out of the $N$, in the order they appear in the input file.

## Constraints and clarifications

$1 \leq N$, $M \leq 50000$

All numbers in the input file are less than or equal to $500\ 000$

All values are positive

## Example

`vopsire.in`

```
3 4
1 7 5 10
2 4 6 9
5 7 3 8
3 8
5 5
1 9
7 4
```

`vopsire.out`

```
2
2
1
1
```