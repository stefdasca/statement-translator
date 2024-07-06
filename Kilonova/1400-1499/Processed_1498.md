About the natural number $N$, we say it has the **okcpp** property if, no matter how we choose $K$ of its digits, we will always find among them at least $P$ distinct digits (any $k\geq p$).

# Task

1. Given the natural numbers $K$, $P$, $A$, and $B$, calculate and display the number of **okcpp** numbers in the interval $[A,B].$
2. Given the natural numbers $K$, $P$, and $N$, calculate and display the smallest **okcpp** number that is greater than or equal to $N.$

# Input data

The input file `okcpp.in` contains on the first line the number $C$. If $C=1$, then the second line contains, separated by space, the natural numbers $K$, $P$, $A$, and $B$. If $C=2$, then the second line contains, separated by space, the natural numbers $K$, $P$, and $N$.

# Output data

If $C=1$, then in the output file `okcpp.out` print the number of **okcpp** numbers in the interval $[A;B].$ If $C=2$, then in the output file `okcpp.out` print the smallest natural **okcpp** number that is greater than or equal to $N.$

# Constraints and clarifications

* $1 \leq P \leq 10$;
* $P \leq K \leq$ the number of digits of $N \leq 18$;
* For $20\%$ of the tests the task will be $C=1$;
* For task $C=1$ we have $0 \leq A < B < 10^{18}$ and $B-A \leq 10\ 000$;
* For task $C=2$ it is guaranteed that there is always a solution.

# Example 1

`okcpp.in`
```
1
5 2 99997 100001
```

`okcpp.out`
```
3
```

## Explanation

We have $K=5$ and $P=2$. In the interval $[99\ 997; 100\ 001]$ there are three **okcpp** numbers: $99\ 997$, $99\ 998$, and $100\ 001.$

# Example 2


`okcpp.in`
```
2
5 3 99997
```

`okcpp.out`
```
100023
```

## Explanation

We have $K=5$, $P=3$, and $N=99\ 997$. It is easy to observe that the numbers $99\ 997$, $99\ 998$, $\dots$, $100\ 022$ do not match. The first number that meets the requirements is $100\ 023.$