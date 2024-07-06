Here's the translated and reformatted problem statement:

---

In Macarie's garden, there is a sequence of $N$ carrots, numbered from $1$ to $N$. To know where they are planted, Macarie has made a small mound of soil in front of each carrot and noted the height of each expressed in centimeters. Thus, carrot $i$ has a mound of soil in front of it with a height of $h_i$ centimeters. A restless mole digs tunnels underground below Macarie's carrots. When it digs a tunnel towards a carrot, it brings all the resulting soil to the surface, thus modifying the height of the mound corresponding to that carrot, but also the heights of the mounds of the other carrots in the garden. If, following the digging of a tunnel towards the carrot at position $pos$, the height of the mound for it increased by $x$ centimeters, then the heights of the mounds of all carrots are modified according to the following rule, which depends on a number $K$:

* The height of the mound of the carrot at $pos - 1$ is modified by $x - K$ centimeters, while for the carrot at $pos + 1$ it is modified by $x + K$ centimeters;
* The heights of the mounds for the carrots at $pos - 2$ and $pos + 2$ are modified by $x - 2 \\cdot K$ and $x + 2 \\cdot K$ centimeters, respectively.

In general, the height is modified according to the following rules for each carrot in the garden:

* The height $h_{pos - i}$ becomes $h_{pos - i} + x - i \\cdot K$, for each $i$, $1 \\leq i \\leq pos - 1$;
* The height $h_{pos + i}$ becomes $h_{pos + i} + x + i \\cdot K$, for each $i$, $1 \\leq i \\leq N - pos$.

# Task

The initial heights of all $N$ mounds and the $U$ modifications made by the mole on the mound heights of the carrots are given.

We know that within a continuous sequence of carrots, the mole finds the most tempting carrot to be the one with the smallest mound height.

Help Macarie identify the height of the mound of the most tempting carrot, for several given intervals, after all the modifications made by the mole have been completed.

# Input data

The input file `cartita.in` contains the following data:
* The first line contains a natural number $N$ with the significance given in the description.
* The next line contains $N$ natural numbers separated by a space representing, in order, the heights of the soil mounds, the $i$-th number representing the initial height $h_i$ of the mound corresponding to carrot $i$.
* The third line contains a natural number $U$ representing the number of carrots towards which the mole has dug tunnels.
* The next $U$ lines each contain a triplet of natural numbers $pos$, $x$, $K$, separated by a space, meaning that, following a tunnel dug towards the carrot at $pos$, the height of its mound increased by $x$ centimeters, and the other heights modified according to the rule described in the problem statement.
* The next line contains the number $Q$ representing the number of intervals where the minimum height of a mound corresponding to the most tempting carrot is to be identified.
* The next $Q$ lines contain two natural numbers $L$, $R$, separated by a space, representing the ends of the investigated interval of carrots.

# Output data

The output file `cartita.out` will contain $Q$ lines, each containing, in order, the response to the investigated intervals.

# Constraints and clarifications

* $1 \\leq N \\leq 100 \\ 000$
* $1 \\leq U \\leq 300 \\ 000$
* $1 \\leq Q \\leq 200 \\ 000$
* $1 \\leq L \\leq R \\leq N$
* Initially $1 \\leq h_i \\leq N$, for each $i$, $1 \\leq i \\leq N$.
* $1 \\leq pos \\leq N$, $1 \\leq x \\leq 400$ and $-21 \\leq K \\leq 21$, $K \\neq 0$.

|#|Score|Constraints|
-|-|-
|1|12|$N, U, Q \\le 2 \\ 000$|
|2|9|$N, U \\le 2 \\ 000$ and $Q \\le 200 \\ 000$|
|3|25|$N, U \\le 75 \\ 000$ and $Q \\le 15$|
|4|17|$N, U, Q \\le 75 \\ 000$|
|5|16|$N \\le 100 \\ 000$, $U \\le 300 \\ 000$ and $Q \\le 15$|
|6|7|$N \\le 100 \\ 000$, $U \\le 300 \\ 000$ and $Q \\le 10 \\ 000$|
|7|14|No additional constraints|

# Example

`cartita.in`
```
6
1 6 2 4 3 4
3
4 5 2
2 4 1
4 2 8
3
1 6
2 4
4 4
```

`cartita.out`
```
-19
-3
17
```

## Explanation

After the first tunnel dug towards carrot $4$, the sequence of heights of the $N = 6$ mounds became $(0, 7, 5, 9, 10, 13)$.
After the second tunnel dug towards carrot $2$, the sequence of heights of the $N = 6$ mounds became $(3, 11, 10, 15, 17, 21)$.
After the third tunnel dug towards carrot $4$, the sequence of heights of the $N = 6$ mounds became $(-19, -3, 4, 17, 27, 39)$.
On the interval $[1, 6]$, the minimum height is $-19$, on the interval $[2, 4]$, the minimum height is $-3$, and for the last investigated interval $[4, 4]$ the minimum height is $17$.

---

Please let me know if you need any further adjustments.