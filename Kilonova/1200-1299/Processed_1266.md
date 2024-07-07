
We consider the following sequence of natural numbers: $1$, $1$, $2$, $1$, $2$, $3$, $1$, $2$, $3$, $4$, $1$, $2$, $3$, $4$, $5$, $\\dots$. The numbers in the sequence are grouped such that each group always starts with the number $1$ and ends with the number immediately before the next occurrence of the number $1$ in the given sequence. The number of the first group is $1$ and it consists of a single number ($1$). The number of the second group is $2$ and it consists of two numbers ($1, 2$), and so on.

Let $n$, $k$, and $p$ be three non-zero natural numbers.

# Task

* Display the sum of the component numbers of all groups that are formed only from numbers less than or equal to $n$ and that have the property that the sum of the numbers in each group has a number of divisors greater than or equal to $k$. If there is no such group, display the sum of the numbers of the groups formed only from numbers less than or equal to $n$, groups whose sum of component numbers is an even number.
* Display the number at position $p$ in the given sequence and the number of the group in which this number is found.

# Input Data

The input file `numere.in` contains a single line with three natural numbers, $n$, $k$, and $p$, in this order, separated by a space.

# Output Data

The output file `numere.out` contains three lines: the first line contains the requested sum, the second line contains the number in the sequence found at position $p$, and the last line contains the number of the group in which the number at position $p$ in the given sequence is found.

# Constraints and clarifications

* $2 \\leq n, k, p \\leq 10\\ 000$;
* 40\% of the points will be awarded for solving task 1, 30\% for task 2, and 30\% for task 3.

# Example 1

`numere.in`
```
5 3 10 
```

`numere.out`
```
31
4
4
```

## Explanation

The formed sequence is $1$, $1$, $2$, $1$, $2$, $3$, $1$, $2$, $3$, $4$, $1$, $2$, $3$, $4$, $5$. The sums of the groups are: $1$, $3$, $6$, $10$, $15$. Among these, $1$ has 1 divisor, $6$ has 4 divisors ($1$, $2$, $3$, $6$), $10$ has 4 divisors ($1$, $2$, $5$, $10$), and $15$ has 4 divisors ($1$, $3$, $5$, $15$). The total requested sum is $31$. The value found in the sequence at position $10$ is $4$, and the number of the group to which it belongs is also $4$, our sequence having the first 10 values: $1$, $1$, $2$, $1$, $2$, $3$, $1$, $2$, $3$, $4$.

# Example 2

`numere.in`
```
4 6 5 
```

`numere.out`
```
16
2
3
```

## Explanation

The formed sequence is $1$, $1$, $2$, $1$, $2$, $3$, $1$, $2$, $3$, $4$. The sums of the groups are: $1$, $3$, $6$, $10$. Among these, no number has more than $6$ divisors. In this case, the value displayed will be $16$ (because only $6$ and $10$ are even numbers). The value found in the sequence at position $5$ is $2$, and the number of the group to which it belongs is $3$, our sequence having the first 5 values: $1$, $1$, $2$, $1$, $2$.
