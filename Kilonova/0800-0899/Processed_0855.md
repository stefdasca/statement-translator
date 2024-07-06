Maria discovered that natural numbers that start with the digit $1$ and have all digits strictly increasing and consecutive, or start with the digit $9$ and have all digits strictly decreasing and consecutive, are called **special** numbers. Interested in discovering the relationship between special numbers with the same number of digits, she noticed that she could construct the following table:
| | |
|-|-|
| 1 | 1 x 8 + 1 = 9 |
| 2 | 12 x 8 + 2 = 98 |
| 3 | 123 x 8 + 3 = 987 |
| 4 | 1234 x 8 + 4 = 9876 |
| 5 | 12345 x 8 + 5 = 98765 |
| 6 | 123456 x 8 + 6 = 987654 |
| 7 | 1234567 x 8 + 7 = 9876543 |
| 8 | 12345678 x 8 + 8 = 98765432 |
| 9 | 123456789 x 8 + 9 = 987654321 |

# Task

Write a program that, given four natural numbers $K$, $N$, $A$ and $B$, determines:

* the largest **special** number located on row $K$ of the table;
* the **special** number obtained by deleting one digit from the number $N$;
* the number of **special** numbers in the set {$A , A+1, A+2, A+3, ..., B-1, B$}.

# Input data

The input file `speciale.in` contains on the first line a natural number $P$. For all input tests, the number $P$ can only be $1$, $2$, or $3$. The second line of the `speciale.in` file contains, in this order, the natural numbers $K$, $N$, $A$, and $B$, separated by a space.

# Output data

If the value of $P$ is $1$, only point 1) of the task will be solved. In this case, the output file `speciale.out` will contain on the first line a natural number representing the largest special number located in the table on row $K$.

If the value of $P$ is $2$, only point 2) of the task will be solved. In this case, the output file `speciale.out` will contain on the first line a natural number representing the special number obtained from the number $N$ by deleting one digit, or $0$ if such a number cannot be obtained.

If the value of $P$ is $3$, only point 3) of the task will be solved. In this case, the output file `speciale.out` will contain on the first line a natural number representing the number of special numbers in the set {$A, A+1, A+2, A+3, ..., B-1, B$}.

# Constraints and clarifications

* $1 \leq a, b \leq 1\ 000\ 000$;
* $1 \leq K \leq 9$;
* $1 \leq N \leq 999\ 999\ 999$;
* $1 \leq A \leq B \leq 999\ 999\ 999$;
* For correctly solving the first task, $20$ points are awarded, for the correct solution of the second task, $40$ points are awarded, and for the correct solution of the third task, $40$ points are awarded.

# Example 1

`speciale.in`
```
1
3 125345 320 888888
```

`speciale.out`
```
987
```

## Explanation

$P = 1$, for this test, only point 1) of the task is solved.

The special numbers on the third row of the table are $123$ and $987$, the largest being $987$.

# Example 2

`speciale.in`
```
2
3 125345 320 888888
```

`speciale.out`
```
12345
```

## Explanation

$P = 2$, for this test, only point 2) of the task is solved.

By deleting the digit $5$ located at the third position in $125345$, the special number $12345$ is obtained.

# Example 3

`speciale.in`
```
3
3 125345 320 888888
```

`speciale.out`
```
6
```

## Explanation

$P = 3$, for this test, only point 3) of the task is solved.

There are $6$ special numbers in the set {$320, 321, ..., 888888$}, namely $987$, $1234$, $9876$, $12345$, $98765$, $123456$.