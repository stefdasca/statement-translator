```markdown
The heights of $N$ peaks, arranged from left to right, are known in a mountain range. If a sentinel is placed on a peak of a certain height, it watches over that peak and up to $K$ peaks to the left and up to $K$ peaks to the right of it, but only if the heights of these watched peaks are less than or equal to the height of the peak on which the sentinel is located. If there is a peak with a strictly greater height at a distance less than or equal to $K$, then the sentinel watches only up to that peak (excluding that peak).

# Task

Given $N$, $K$, and the heights of the $N$ peaks, determine:
1. The maximum number of consecutive peaks, starting from the first peak of the mountain range (including this peak), that can be watched with a single sentinel.
2. The minimum number of sentinels needed to watch over all the peaks.

# Input data

The input file `santinele.in` contains:
- The first line contains the number of the task, $1$ or $2$.
- The second line contains the numbers $N$ and $K$, with the meaning specified in the statement.
- The third line contains $N$ numbers, $h_{1}, h_{2}, \ldots, h_{N}$, representing the heights of the $N$ peaks, in the order they are arranged from left to right in the mountain range. The numbers on the same line of the input file are separated by a space.

# Output data

The output file `santinele.out` contains a single number. If the task is $1$, it contains the maximum number of peaks determined for this task. If the task is $2$, it contains the minimum number of sentinels determined for this task.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $0 \le K < N$;
* $1 \leq h_i \leq 1\ 000\ 000$.

|# | Score | Constraints|
| - | - | ----------|
|1|14|$C = 1$|
|2|14|$C = 2$, $N$ even, $K = N/2$.|
|3|16|$C = 2$ and $h_1 < h_2 < \ldots < h_N$|
|4|13|$C = 2$ and there exists $1 < p < N$, for which $h_1 < \ldots < h_{p-1} < h_p > h_{p + 1} > \ldots > h_N$|
|5|14|$C = 2$, $N \leq 15$|
|6|29|$C = 2$, no additional constraints.|

# Example 1

`santinele.in`
```
1
8 2
6 10 5 7 8 5 4 4
```

`santinele.out`
```
4
```

## Explanation

The task is $1$ and $K = 2$. The sentinel watches the peak it is placed on, up to two peaks to the left and up to two peaks to the right. With a single sentinel, we can cover up to four peaks, starting with the first peak, by placing the sentinel on the second peak.

# Example 2

`santinele.in`
```
2
10 2
10 5 5 10 6 7 4 1 6 7
```

`santinele.out`
```
4
```

## Explanation

The task is $2$ and $K = 2$. A minimum of $4$ sentinels is needed, which can be placed on the following peaks: the first, the $4$-th, the $7$-th, and the $10$-th.

# Example 3

`santinele.in`
```
2
15 3
5 3 1 12 11 9 15 11 10 9 2 7 10 11 7
```

`santinele.out`
```
3
```

## Explanation

The task is $2$ and $K = 3$. A minimum of $3$ sentinels is needed. They can be placed on the following peaks: the first, the $7$-th, and the $14$-th.

~[santinele_ex.png|align=center]

# Example 4

`santinele.in`
```
2
20 5
7 12 23 21 20 24 28 21 4 16 27 1 6 8 20 3 3 5 11 5
```

`santinele.out`
```
3
```

## Explanation

The task is $2$ and $K = 5$. A minimum of $3$ sentinels is needed. They can be placed on the following peaks: the $3$-rd, the $7$-th, and the $15$-th.
```