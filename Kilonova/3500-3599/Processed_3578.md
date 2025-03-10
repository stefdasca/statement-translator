
# Task

You are given two natural numbers $a$ and $b$, with $a \leq b$, and your task is once again simple:

Find two nonzero numbers $x$ and $y$ such that $a \leq x+y \leq b$, and $\gcd(x, y) \neq 1$, where $\gcd(x, y)$ is the greatest common divisor of the two chosen numbers.

If there is no such solution, output $-1$.

As with the previous problem, you will need to solve the problem for $t$ such pairs.

# Input data

The first line of the input file `divizor.in` contains $t$, the number of pairs. 

For the next $t$ lines, each contains two numbers, $a$ and $b$, which represent the minimum and maximum value of the required sum.

# Output data

The output file `divizor.out` will have $t$ lines, containing the answers for the $t$ pairs of data.

# Constraints and clarifications

* $1 \leq t \leq 100$;
* $1 \leq a, b \leq 1 \ 000 \ 000 \ 000$;
* For tests worth $30$ points, $1 \leq a, b \leq 1 \ 000$.
* For other tests worth $30$ points, $1 \leq a, b \leq 100 \ 000$.

# Example 1

`divizor.in`
```
6
41 43
1 3
4 8
19 24
8 8
37 37
```

`divizor.out`
```
24 18
-1
2 6
12 10
4 4
-1
```
