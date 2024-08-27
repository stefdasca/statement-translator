# Reborn

In Tsuna's town, there are $N$ mafia houses numbered from $1$ to $N$, arranged one after another. Reborn has $M$ weapons. For each weapon $i$, you know the interval $[x_i, y_i]$ of houses where Reborn can kill Tsuna and revive him in another house within the same interval. Answer $Q$ questions of type $(a, b)$: what is the minimum number of weapons Reborn needs to use so that Tsuna can move from house $a$ to house $b$.

## Input Data

The input file `reborn.in` will contain on the first line $N$, $M$, and $Q$. The next $M$ lines will describe the intervals of the weapons (line $i + 1$ will contain the elements $x_i$ and $y_i$). The next $Q$ lines will contain 2 numbers $a$ and $b$ representing the $Q$ questions.

## Output Data

The output file `reborn.out` will contain $Q$ lines, the answer for each question. If it is not possible to reach from house $a$ to house $b$, print $-1$.

## Constraints

$1 \leq N \leq 200000$

$1 \leq M \leq 200000$

$1 \leq Q \leq 200000$

## Example

`reborn.in`

```plaintext
10 3 6
1 5
4 8
8 9
9 1
1 9
7 10
10 10
3 6
4 6
3 3
```

`reborn.out`

```plaintext
-1
0
2
1
```