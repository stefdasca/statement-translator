
Consider $N$, a non-zero natural number. We want to write $N$ as the sum of two non-zero natural numbers $x$ and $y$, such that the sum of the digits of the numbers $x$ and $y$ is maximized.

# Task

Write a program that solves the following requirements:

1. Determine the maximum sum of the digits of two numbers $x$ and $y$ with the property that $x + y = N$;
2. Determine two non-zero natural numbers $xmax$ and $ymax$ with the property that $xmax \geq ymax$, $xmax + ymax = N$, the sum of their digits is maximal, and the difference $xmax - ymax$ is maximal;
3. Determine two non-zero natural numbers $xmin$ and $ymin$ with the property that $xmin \geq ymin$, $xmin + ymin = N$, the sum of their digits is maximal, and the difference $xmin - ymin$ is minimal.

# Input data

The input file `nxy.in` contains on the first line the natural number $c$, representing the task ($1$, $2$, or $3$). The second line contains the natural number $N$.

# Output data

The output file `nxy.out` will contain a single line. If $c=1$, the first line will contain a natural number $s$, representing the maximum sum of the digits of two non-zero natural numbers $x$ and $y$ for which $x + y = N$. If $c=2$ or $c=3$, the first line will contain two non-zero natural numbers separated by a single space, representing the solution for the respective task ($xmax$ and $ymax$ for $c=2$, and $xmin$ and $ymin$ for $c=3$).

# Constraints and clarifications

* $1 \lt N \leq 10^{18}$
* For tests worth 20% of the score, the task is 1. For tests worth 40% of the score, the task is 2. For tests worth 40% of the score, the task is 3.

# Example 1

`nxy.in`
```
1
25
```

`nxy.out`
```
16
```

## Explanation

The maximum sum that can be obtained by adding the digits of two numbers $x$ and $y$ for which $x + y = 25$ is $16$.

# Example 2

`nxy.in`
```
2
25
```

`nxy.out`
```
19 6
```

## Explanation

The maximum sum that can be obtained by adding the digits of two numbers $x$ and $y$ for which $x + y = 25$ is $16$. The pair of numbers $xmax \geq ymax$ for which $xmax - ymax$ is maximal ($13$) and for which the sum of the digits is maximal is $xmax=19$ and $ymax=6$.

# Example 3

`nxy.in`
```
3
25
```

`nxy.out`
```
16 9
```

## Explanation

The maximum sum that can be obtained by adding the digits of two numbers $x$ and $y$ for which $x + y = 25$ is $16$. The pair of numbers $xmin \geq ymin$ for which $xmin - ymin$ is minimal ($7$) and for which the sum of the digits is maximal is $xmin=16$ and $ymin=9$.
