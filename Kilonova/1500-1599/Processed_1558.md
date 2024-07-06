# Task

Write a program that, knowing the information about the $N$ orders, determines the minimum loss and an optimal scheduling.

# Input data

The input file `venus.in` contains on the first line the natural number $N$, representing the number of orders, and the natural number $T$, representing the number of hours Vasile needs to complete an order. The following $N$ lines contain the information about the orders, one order per line, in the form:
`V day month hour`
where $V$ is the value of the order, `day` is the day by which the order must be completed (a natural number between $1$ and the number of days in the month), `month` is the name of the month, and `hour` is a natural number between $0$ and $23$. The values written on the same line are separated by a space.

The orders are considered numbered from $1$ to $N$ in the order in the input file.

# Output data

The output file `venus.out` will contain the natural number `pmin` on the first line, representing the minimum loss. The second line will contain $N$ distinct natural numbers between $1$ and $N$, separated by a space, representing an optimal scheduling.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$;
* $1 \leq T \leq 500$;
* $1 \leq V \leq 10\ 000$;
* The names of the months will be written in lowercase. The year 2020 is a leap year, meaning the month of February has **29** days;
* If there are multiple optimal schedulings, any correct solution will be accepted;
* $50\\%$ of the score for each test will be awarded for determining the value of `pmin`. The full score for each test will be awarded for solving both requirements (`pmin` and an optimal scheduling).

# Example

`venus.in`
```
4 25
90 10 january 20
50 2 january 8
20 4 january 3
70 2 january 9
```

`venus.out`
```
50
4 1 3 2
```

## Explanation

- Starting from January 1 at 00:00, Vasile executes order $4$ and finishes on January 2 at 01:00.
- Then he executes order $1$, which he finishes on January 3 at 02:00.
- Then he executes order $3$, which he finishes on January 4 at 03:00.
- Then he executes order $2$, which he finishes on January 5 at 04:00, which means he missed the delivery deadline, so he loses its value ($50$).

There are other possible optimal schedulings. For example, `4 3 1 2`.

