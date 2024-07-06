If you want to change your ID card, you need to go to the Population Records Service. There, you need to take an order number and wait for your turn. The order numbers are issued by a robot, in the order $1$, $2$, $3$, $\\dots$. Programmer Vasile, who developed the software for the robot and provides system maintenance (for a fee), intentionally created a bug in the system. Vasile has a favorite natural number $N$. An order number $x$ will be issued if and only if $x$ is a subsequence of $N$ (i.e., all digits of $x$ appear in $N$ in the order of $x$, not necessarily in consecutive positions). If the current order number $x$ does not meet this condition, the robot gets blocked and no longer issues order numbers.

# Task

Write a program that, given the value of $N$, Vasile's favorite natural number, solves the following two tasks:

* determines how many digits the order number $x$ which leads to the robot blocking has;
* determines the order number $x$ which leads to the robot blocking.

# Input data

The input file `bug.in` will contain on the first line the task $C$ that needs to be solved ($1$ or $2$). The second line contains the natural number $N$.

# Output data

The output file `bug.out` will contain a single line where the answer to the task $C$ will be written.

# Constraints and clarifications

* $N$ is a non-zero natural number having at most $100 \ 000$ digits.

|#|Score|Constraints|
|-|-|--------|
|1|23|$C = 1$|
|2|10|$C = 2$ and $N$ has at most $18$ digits.|
|3|10|$C = 2$, $N$ has at least $20$ digits and the result has at most $7$ digits.|
|4|30|$C = 2$, $N$ has at least $101$ and at most $10 \ 000$ digits.|
|5|27|$C = 2$ and there are no other constraints.|

# Example 1

`bug.in`
```
1
1032
```

`bug.out`
```
1
```

## Explanation

The smallest non-zero natural number that is not a subsequence of $1 \ 032$ has one digit.

# Example 2

`bug.in`
```
2
1032
```

`bug.out`
```
4
```

## Explanation

The smallest non-zero natural number that is not a subsequence of $1 \ 032$ is $4$.

# Example 3

`bug.in`
```
1
25632012312458761560789
```

`bug.out`
```
2
```

## Explanation

The smallest non-zero natural number that is not a subsequence of $25632012312458761560789$ has two digits.

# Example 4

`bug.in`
```
2
25632012312458761560789
```

`bug.out`
```
42
```

## Explanation

The smallest non-zero natural number that is not a subsequence of $25632012312458761560789$ is $42$.
