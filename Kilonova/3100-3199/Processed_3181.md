
Bahoi doesn't like odd numbers. He has an array with $N$ elements, and he can perform the following operation as many times as he wants:
* Choose an index $i$, increase the values of the array at positions $i, i + 1, \dots, n$ by $1$.

# Task

What is the minimum number of operations needed such that in the end there are no odd numbers in the array?

# Input data

The first line contains $t$, the number of test cases. The first line of each test case contains a number $N$, and on the following line exactly $N$ numbers.

# Output data

Print $t$ lines, each containing the answer for their respective test case.

# Constraints and clarifications

* $1 \leq N,t \leq 2 \cdot 10^5$
* The elements of the array are natural numbers and do not exceed $10^{18}$.
* It is guaranteed that the sum of all $N$'s across all test cases is $\leq 2 \cdot 10^5$.

# Example

`stdin`
```
10
9
8 4 3 4 5 3 10 2 1
9
9 5 2 7 4 10 3 8 4
5
4 4 8 7 2
4
10 2 5 1
9
6 8 1 10 1 2 3 4 5
3
9 5 3
3
6 5 3
10
1 2 1 9 5 6 3 8 9 1
3
6 7 5
4
8 5 5 6
```

`stdout`
```
5
6
2
1
7
1
1
7
1
2
```
