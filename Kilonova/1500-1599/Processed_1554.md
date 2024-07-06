~[optime.png|align=right]

Maria loves prime numbers. She writes on a sheet of paper, in strictly increasing order, a sequence formed from prime numbers that have at least $2$ digits. Then, from the numbers that have more than $2$ digits, she cuts off the digits from the left, so that only $2$ digits remain. If the number obtained after cutting off the digits is not between $10$ and $99$, the number is removed from the sequence. For example, the prime number $101$, which has $3$ digits, will not be written because cutting off the left digit results in the number $01$, that is, $1$, which does not have exactly $2$ digits, so after cutting it off, it will be removed from the sequence.

Maria fills a table with $2 \cdot k$ rows and $k$ columns, so that, traversing it by rows, from top to bottom, and each row from left to right, the numbers from the sequence are obtained. Studying the numbers in the table, she notices that among them there are numbers that are not prime.

For example, for $k=4$, the table looks like the image on the right.

# Task

Given a non-zero natural number $k$ and a natural number $x$, help Maria:
1. To determine the sum of the numbers in the table that are not prime. If there are no numbers that are not prime, the sum is $0$.
2. To choose $x$ consecutive columns from the table, such that they contain, in total, the maximum number of prime numbers. If there are several possibilities, the sequence of consecutive columns with the highest starting column value in the sequence will be chosen. Determine the number of the first column in the chosen sequence, as well as the total number of prime numbers in the sequence.

# Input Data

The input file `optime.in` contains on the first line a digit $C$ which can only be $1$ or $2$. If $C = 1$, the second line contains a non-zero natural number $k$ with the meaning given in the statement. If $C = 2$, the second line contains two non-zero natural numbers, $k$ and $x$, with the meaning given in the statement.

# Output Data

If the value of $C$ is $1$, then only point $1$ from the task will be solved. In this case, the output file `optime.out` will contain on the first line a natural number representing the value of the determined sum.

If the value of $C$ is $2$, only point $2$ from the task will be solved. In this case, the output file `optime.out` will contain on the first line a natural number representing the order number of the first column according to the task, and on the second line the number of prime numbers, according to the task.

# Constraints and clarifications

* $1 \leq x \leq k \leq 200$;
* For solving the first requirement, $30\%$ of the score is awarded, and for the second, $70\%$ of the score is awarded.

# Example 1

`optime.in`
```
1
4
```

`optime.out`
```
286
```

## Explanation

For $k = 4$, the table contains the following non-prime numbers: $27$, $39$, $49$, $51$, $57$, $63$, their sum being $286$.

# Example 2

`optime.in`
```
2
4 3
```

`optime.out`
```
2
19
```

## Explanation

Column $1$ contains $7$ prime numbers, column $2$ contains $6$ prime numbers, column $3$ contains $6$ prime numbers, and column $4$ contains $7$ prime numbers.

We can choose either columns $1,2,3$ or columns $2,3,4$, both options containing $19$ prime numbers. The second option is chosen because it has the higher value of the starting column of the sequence.