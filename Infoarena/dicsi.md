## Task

Do you know how little kids cry? $WEEEEEEE$ Everyone knows the famous character, Dicsi. He just found out that he has $N$ children (with a special girl). Since Dicsi is a family man, he wants to get to know his children better, but this is not easy because Dicsi has a lot of children $( N \leq 100000 )$. Being a born programmer, Dicsi took 2 measures:
1. All children were indexed with distinct indices from $1$ to $N$
2. Each child was colored with a different color.

Two children are considered to resemble each other if the index of one is a divisor of the index of the other. Dicsi does not want to color two children who resemble each other with the same color because he would then confuse them. Help Dicsi determine the minimum number of colors needed to color his children so that he does not confuse them, as well as a valid coloring.

## Input data

The input file `dicsi.in` will contain a single natural number $N$, representing the number of children.

## Output data

The output file `dicsi.out` will contain on the first line a number $X$, representing the minimum number of colors needed. The second line will contain $N$ natural numbers from the interval $[1 \dots X]$, the $i$-th element representing the color of the $i$-th child. If there are multiple solutions, you can print any of them.

## Constraints

$1 \leq N \leq 100000$

## Example

`dicsi.in`

```
5
```

`dicsi.out`

```
3
2 1 1 2 3
```