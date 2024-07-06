# Task

Alex accessed European funds and started a profitable business consisting of raising silkworms. Silkworms feed on mulberry leaves, and Alex has many mulberry trees in his garden. He noticed that if he places a silkworm on a mulberry leaf, it will eat the entire leaf in a time that depends only on the size of the leaf surface.

Alex decided to give his silkworms an intelligence test. For this purpose, he implemented the following scientific experiment: on a narrow, linear bar, he arranged from left to right $n$ mulberry leaves with surfaces $s_1$, $s_2$, $\\dots$, $s_n$, at distances $x_1$, $x_2$, $\\dots$, $x_n$ millimeters from the left end. Alex placed a silkworm on the leaf numbered $k$. For any leaf $i$, the silkworm will eat the leaf in $s_i$ seconds, where $s_i$ is the size of the leaf surface. After eating an entire leaf, the silkworm immediately moves at a speed of $1$ millimeter/second to the next leaf, which can be on its left or right. In other words, it can change its direction of travel if necessary after eating a leaf.

Alex wants to know what the maximum number of mulberry leaves that the smartest silkworm can eat entirely within a maximum time of $t$ seconds.

# Task

Knowing $n$, $k$, $t$, the distances $x_1$, $x_2$, $\\dots$, $x_n$, and the surfaces $s_1$, $s_2$, $\\dots$, $s_n$ as described above, determine the maximum number of leaves that a silkworm can eat entirely in a time not exceeding $t$, if it is initially placed on leaf $k$.

# Input data

The input file `mts.in` contains the following:
- The first line contains three natural numbers $n$, $k$, $t$ separated by spaces, with the previously described meanings.
- The second line contains $n$ natural numbers $s_1$, $s_2$, $\\dots$, $s_n$ separated by spaces, representing the sizes of the surfaces of the $n$ leaves.
- The third line contains $n$ natural numbers $x_1$, $x_2$, $\\dots$, $x_n$ separated by spaces, representing the distances at which the $n$ mulberry leaves are placed from the left end of the bar.

# Output data

The first line of the output file `mts.out` will print a single natural number $f$ representing the maximum number of leaves that the smartest silkworm can eat in time $t$.

# Constraints and clarifications

* $1 \\leq k \\leq n \\leq 200 \\ 000$
* $1 \\leq s_1, s_2, \\dots, s_n \\leq 1 \\ 000$
* $1 \\leq x_1 < x_2 < \\dots < x_n \\leq 1 \\ 000 \\ 000$
* $1 \\leq t \\leq 2 \\ 000 \\ 000$
* As soon as the silkworm reaches the position of a mulberry leaf, it stops and starts eating that leaf. It will not leave that position until the leaf is eaten entirely.

# Example 1

`mts.in`
```
3 2 9
4 2 5
1 5 6
```

`mts.out`
```
2
```

## Explanation

The silkworm will eat $2$ leaves: those with the order numbers $2$ and $3$. The total time will be: $s_2 + s_3 + (x_3 - x_2) = 2 + 5 + 1 = 8$

If it tries to eat leaves $2$ and $1$, then the total time would be: $s_2 + s_1 + (x_2 - x_1) = 2 + 4 + (5 - 1) = 10 > 9$

# Example 2

`mts.in`
```
4 2 11
4 2 1 5
1 2 4 8
```

`mts.out`
```
3
```

## Explanation

The silkworm will eat $3$ leaves: those with the order numbers $2$, $1$, and $3$, exactly in this order, in a total time: $s_2 + s_1 + s_3 + 2 \\cdot (x_2 - x_1) + (x_3 - x_2) = 2 + 1 + 4 + 2 \\cdot (2 - 1) + (4 - 2) = 11$.