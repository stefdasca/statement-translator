In the neighborhood of mathematicians, there are exactly $n$ houses, arranged in a line. Each house has associated:

* a **number** (a non-negative integer);
* a **risk value**, which is equal to the sum of the divisors of the house's number, excluding the number itself.

A house is considered **perfect** if its number is strictly greater than $1$ and strictly greater than its risk value. A house can be bought for an amount of money equal to its number.

For example, the house with the number $10$ is perfect because its number is strictly greater than its risk value (its number is $10$ and its risk value is equal to the sum of its divisors excluding the number itself: $1+2+5=8$).

Two houses can have the same number. The numbers of the houses are given in any order.

As a good investor, Little Gates wants to buy the **maximum number of perfect houses without the total amount paid exceeding the value $S$** he has available. If multiple options are available, he will choose the sequence of houses for which he **pays the least**. Moreover, to reduce maintenance costs for the purchased houses, he will choose only a **sequence of neighboring houses**.

# Task

1. How many perfect houses are there in the neighborhood of mathematicians?
2. How many houses does Little Gates buy and what is the total amount spent by him?

# Input data

The first line of the input file `case.in` contains a number $c$ of the task, which can be only $1$ or $2$.
The second line contains $2$ positive integers, separated by a space, $n$ and $S$ ($n$ the number of houses, $S$ the amount of money he has available to buy houses).
The third line contains $n$ natural numbers representing the numbers of the houses in the neighborhood in the order they are arranged.

# Output data

The first line of the output file `case.out` will contain either the answer to task $1$, or the answer to task $2$.

# Constraints and clarifications

* $0 \\leq \\text{house number} \\leq 10 \\ 000$;
* $1 \\leq n \\leq 1 \\ 000 \\ 000$;
* $1 \\leq S \\leq 10 \\ 000 \\ 000 \\ 000$;
* For $48$ points, the task is $1$. For $25$ points, $n \\leq 100$;
* For $52$ points, the task is $2$.

# Example 1

`case.in`
```
1
9 10
6 15 7 4 4 4 4 5 14
```

`case.out`
```
8
```

## Explanation

The task is $1$.
The perfect houses are the ones with the numbers: $15$, $7$, $4$, $4$, $4$, $4$, $5$, $14$.

# Example 2

`case.in`
```
2
9 13
6 6 7 4 4 4 4 2 12
```

`case.out`
```
3 10
```

## Explanation

The task is $2$.
The longest sequence of perfect houses for which Little Gates pays the least (maximum $13$) consists of the houses with the numbers: $4$, $4$, $2$.
The total amount paid is $10$.