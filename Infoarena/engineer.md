In a universe full of tractors, a skilled engineer is needed to maintain them. Every tractor on this planet needs affection, just like the one below. Of course, you're probably wondering how humanity came to depend so much on these smoke-spewing machines. After successfully implementing a robot capable of solving any algorithmic problem (using machine learning), including NP-complete ones, most programmers decided to spend their free time in agriculture. As a result, things changed drastically: instead of wanting to implement a problem as quickly or correctly as possible (as in an ACM competition), the winner of the duel is now the one whose plantation is the most productive. Since a perfect solution never exists, the way the productivity of a programmer's plantation is evaluated is not the most fair and differs from case to case. Each programmer owns a plantation that can be viewed as a subarray of an $N \times M$ matrix, where each cell $(i, j)$ with $1 \leq i \leq N$ and $1 \leq j \leq M$ holds a value representing the productivity index of that cell. In determining the average productivity of a programmer $i$, our engineer will have to calculate the $K_i$-th smallest value among those in his plantation. Before starting this nonconformist competition among programmers, we must ensure that our engineer is brave enough to calculate the productivity of each programmer.

## Task

Given an $N \times M$ matrix, we need to find the $K_i$-th smallest value for $Q$ given subarrays. A subarray is characterized by $(x_1, y_1, x_2, y_2)$, where the cells $(x_1, y_1)$ and $(x_2, y_2)$ represent the top-left and bottom-right corners. Any subarray can be viewed as an array, so the $K_i$-th value for a given subarray is the value that would be at position $K_i$ if we sorted the array.

## Input data

The input file `engineer.in` will contain on the first line two natural numbers $N$ and $M$, representing the dimensions of the matrix. The next $N$ lines will contain $M$ natural numbers each, representing the productivity indices of each cell. After these, there will be a line containing a number $Q$, representing the number of programmers. The next $Q$ lines will contain five natural numbers $(x_1, y_1, x_2, y_2, K_i)$, representing the top-left and bottom-right corners of the plantation allocated to each of the $Q$ programmers, as well as $K_i$, with the significance mentioned in the task.

## Output data

The output file `engineer.out` will contain $Q$ lines, each containing a value representing the average productivity for each programmer, with the solution for the $i$-th programmer on the $i$-th line.

## Constraints and clarifications

$1 \leq N \leq 1100$

$1 \leq M \leq 1100$

$1 \leq Q \leq 1000$

$1 \leq x_1 \leq x_2 \leq N$

$1 \leq y_1 \leq y_2 \leq M$

$1 \leq K_i \leq (x_2 - x_1 + 1) \times (y_2 - y_1 + 1)$

Values in the matrix are natural numbers between $1$ and $10^9$

Programmers can have the same plantations or their plantations can overlap

If two programmers $i$ and $j$ have exactly the same plantation, it is not guaranteed that $K_i$ is equal to $K_j$

## Example

`engineer.in`

```
2 2
3 2
1 2
4
1 1 2 2 1
1 1 2 2 2
1 1 2 2 3
1 1 2 2 4
```

`engineer.out`

```
1
2
2
3
```

## Explanation

All programmers have exactly the same plantation. The smallest value in the matrix is $1$, the second smallest is $2$, etc.