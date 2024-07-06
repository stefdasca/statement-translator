A natural positive number $m$ is called *lucky* if its square can be written as the sum of $m$ consecutive natural numbers. A natural number $m$ is called *$k$-lucky* if it is equal to the product of exactly $k$ distinct prime numbers. Note that there is no connection between the two properties defined.

# Task

Given $k$ and $N$ natural numbers, write a program that determines:

1) The smallest and largest lucky number among the $N$ numbers read;
2) How many $k$-lucky numbers are in the sequence of $N$ numbers read.

# Input data

The input file `norocos.in` contains on the first line a natural number $C$. For all input tests, the number $C$ has one of the values $1$ or $2$. The second line of the file contains the natural numbers $N$ and $k$, with the significance given in the statement, and on the third line there are $N$ natural numbers, separated by a space.

# Output data

The output file is `norocos.out`.
**If $C = 1$, only task 1 will be solved**. In this case, the output file will contain, separated by a space, in this order, the smallest and largest lucky number among the $N$ numbers read. If there is no lucky number, the value $0$ will be printed. If there is only one lucky number, it will be printed twice.

**If $C = 2$, only task 2 will be solved**. In this case, the output file will contain a single number representing the number of $k$-lucky numbers read.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$
* $2 \leq k \leq 30$
* The numbers read on the third line of the file are natural numbers between $1$ and $2 \ 000 \ 000 \ 000$.
* 40 points are awarded for correctly solving the first task.
* 60 points are awarded for correctly solving the second task.

# Example 1

`norocos.in`
```
1
9 3
165 12 33 30 5 18 105 15 4
```

`norocos.out`
```
5 165
```

## Explanation

Note that $C = 1$, so only the first task will be solved.
The smallest lucky number is $5$
$5^2 = 25 = 3+4+5+6+7$

The largest lucky number is $165$
$165^2 = 27225 = 83+84+85+...+246+247$

Note that, although the value of $k$ is read, it is not used in solving task $1$.

# Example 2

`norocos.in`
```
2
5 3
165 31 165 105 44
```

`norocos.out`
```
3
```

## Explanation

Note that $C = 2$, so only the second task will be solved.
The three $k$-lucky numbers are $165$, $165$, $105$.