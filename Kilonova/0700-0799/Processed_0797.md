The National Lottery has $N$ balls inscribed with distinct, non-zero natural numbers, each with at most $4$ digits. The lottery director receives a box containing the $6$ balls drawn in the last round, while the remaining undrawn balls are placed in a safe. Since he has a mischievous nature, he removes the ball with the smallest number from the box and keeps it in his coat pocket. He will replace it with an undrawn ball from the safe that has the number closest to it. Then, he continues the operation and removes the ball with the largest initially drawn number, which he places in his other pocket. He will also replace it with another initially undrawn ball from the safe that has the number closest to it.

# Task

Write a program that displays in ascending order the numbers on the balls remaining in the box after the changes made by the director.

# Input data

The input file `loto.in` contains on the first line the natural number $N$, the second line contains the $N$ natural numbers written on the balls, and the third line contains the $6$ natural numbers written on the balls drawn by the lottery employees. The values written on the same line are separated by spaces.

# Output data

In the output file `loto.out`, print on the first line, separated by spaces, the $6$ numbers obtained in the box after the changes made by the director, in ascending order.

# Constraints and clarifications

* $8 < N < 1\ 000$
* If a ball can be replaced by two balls equally close to it, it will be replaced by the ball with the higher number.
* For the test data, both the ball with the smallest number and the ball with the largest number can be replaced with other balls.

# Example 1

`loto.in`
```
10
231 212 32 123 453 675 1321 54 67 567
212 32 67 567 675 1321
```

`loto.out`
```
54 67 212 453 567 675
```

## Explanation

The director replaced the ball $32$ with the ball $54$ and the ball $1321$ with the ball having the closest number to it, namely $453$.

# Example 2

`loto.in`
```
12
3 4 6 7 8 9 2 1 10 18 22 26
2 9 3 4 22 6
```

`loto.out`
```
1 3 4 6 9 26
```

## Explanation

The director replaced the ball $2$ with the ball $1$. Then he replaced the ball $22$ with the ball $26$ ($18$ is as close as $26$ to the ball $22$, but $26$ is higher).