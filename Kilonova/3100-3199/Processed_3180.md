We call an array $A$ with $N$ elements $\textbf{good}$ if the prefix [xor](https://en.wikipedia.org/wiki/Exclusive_or) sums form an array with distinct elements. Formally, if $xr_i = A_1 \oplus A_2 \oplus \dots \oplus A_i$ (here, the symbol $\oplus$ denotes the xor operation), then the array $xr$ contains exactly $N$ distinct elements.

# Task

Given an array $A$ and a number $N$, you want to make it $\textbf{good}$ using any number (possibly $0$) of the following operations:
* Choose two numbers $i$ and $x$ such that $1 \leq i \leq N$ and replace $a_i$ with $x$.

Find the minimum number of operations required to transform the array into a $\textbf{good}$ array.

# Input data

The first line contains $t$ (the number of test cases). The first line of each test case contains a number $N$, and the next line contains exactly $N$ numbers separated by a space.

# Output data

There will be $t$ lines containing the answers to the $t$ test cases.

# Constraints and clarifications

* $1 \leq t \leq 10^4$
* $1 \leq N \leq 2 \cdot 10^5$
* $0 \leq A_i \leq 10^9$
* It is guaranteed that the sum of the $N$ values for all test cases is $\leq 2 \cdot 10^5$.

# Example

`stdin`
```
4
3
1 3 0
2
0 0 
3
1 2 3
10
100 34 2 4 1 5 0 12 9 10
```

`stdout`
```
1
1
0
2
```

## Explanation

The $xr$ array from the first test case looks like this: $1,2,2$. If we choose $i = 3$ and $x = 4$, then the $xr$ array will look like this: $1,2,6$.

In the 3rd test case, the $xr$ array already has all distinct elements.