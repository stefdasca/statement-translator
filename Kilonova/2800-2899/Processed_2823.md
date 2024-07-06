~[rama1.png|align=right]

Chef Constantin has received an order for $M$ breaded worms, the house specialty. He looks into the worm chest and observes that he has $N$ worms of integer lengths $r_1, r_2, \dots, r_N$.

Being a skilled chef, Constantin can cut the worms into **integer** length pieces. He then fries each worm (or piece of worm) for each of the $M$ guests. The satisfaction of a guest is given by the length of the worm received, and Constantin's satisfaction, being an empathetic man, is the minimum satisfaction of all his customers.

# Task
If he cuts and distributes the worms optimally, what is the maximum satisfaction that Chef Constantin can achieve?

# Input data

The first line of standard input contains two numbers $N$ and $M$, with the meaning from the statement.

The next line contains $N$ numbers: $r_1, r_2, \dots , r_N$.

# Output data

The single line of standard output will contain a single number, the maximum satisfaction of Chef Constantin. If there is no possible division, his satisfaction is $0$.

# Constraints and clarifications

* $1 \leq N, M \leq 10^5$
* $1 \leq r_i \leq 10^6,\ \forall\ 1 \leq i \leq N$

| # | Points | Constraints          |
| - | ------ | ------------------- |
| 1 | 15     | $M = 2$ |
| 2 | 15     | $N = 2$ |
| 3 | 40     | $1 \leq N, M \leq 10^3$, $1 \leq r_i \leq 10^3, \ \forall\ 1 \leq i \leq N$ |
| 4 | 30     | No additional constraints |

# Example 1

`stdin`
```
1 2
255
```

`stdout`
```
127
```

# Example 2

`stdin`
```
10 6
15 43 72 59 18 8 24 97 61 27
```

`stdout`
```
43
```