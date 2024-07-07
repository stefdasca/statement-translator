
Given a sequence of $n$ digits $c_1, c_2, \dots, c_n$, where $0 \leq c_i \leq 9$. From a sequence of digits, a sequence of $1 \leq m \leq n$ numbers $a_1, a_2, \dots, a_m$ can be obtained as follows:

* Initially, we consider each digit a number and obtain the sequence of $n$ numbers $a_i = c_i$.
* A new number can be obtained by concatenating a sequence of two or more neighboring numbers from the original sequence. Two elements in a sequence are called neighbors if they are located in adjacent positions in the sequence.
* The concatenation operation of two or more numbers can be performed multiple times as long as the obtained number is less than or equal to $2\ 000\ 000\ 000$, does not start with the digit $0$, and there are at least two numbers in the sequence.
* For example, the sequence [$3, 5, 0, 2, 7, 3$] can become [$35, 0, 2, 73$] by concatenating the numbers $3$, $5 \rightarrow 35$ and $7$, $3 \rightarrow 73$, which can later become [$3502, 73$] by concatenating the numbers $35, 0, 2 \rightarrow 3502$. But we cannot create the sequence [$35, 02, 73$] because we would have a number starting with $0$.

Two neighboring numbers are consecutive if the first is $1$ less than the second.

# Task

Given the initial sequence of digits, obtain the following results:

1. Assuming no digit concatenation is done, and each digit becomes a number in the sequence, i.e., $a_i = c_i$, determine how many pairs of consecutive neighboring numbers exist in the sequence;
2. Determine a way to concatenate the digits to obtain the two largest consecutive neighboring numbers and display the first of these numbers.

# Input data

The input file `vecine.in` contains on the first line two numbers $p$ and $n$, with $p$ representing task $1$ or $2$, and on the next line the $n$ digits, separated by spaces.

# Output data

The output file `vecine.out` will contain a single natural number. If $p = 1$, it will represent the response for task $1$. If $p = 2$, it will represent the response for task $2$.

# Constraints and clarifications

* For task $2$, it is guaranteed that the obtainable numbers will not exceed the value of $2\ 000\ 000\ 000$;
* Also for task $2$, it is guaranteed the existence of at least one pair of consecutive neighboring numbers.
* The digit $0$ can only form the number $0$ on its own.
* Two neighboring numbers are consecutive if the first is $1$ less than the second.
* $20$ points are awarded for $p = 1$, and $3 \leq n \leq 100\ 000$;
* $80$ points are awarded for $p = 2$, and $3 \leq n \leq 100\ 000$;

# Example 1

`vecine.in`
```
1 18
3 2 1 2 1 0 6 3 0 5 6 3 0 6 9 2 9 3
```

`vecine.out`
```
2
```

## Explanation

For the first example:
[$3, 2, 1, 2, 1, 0, 6, 3, 0, 5, 6, 3, 0, 6, 9, 2, 9, 3$]

There are two pairs of consecutive neighboring numbers formed from a single digit: $1, 2$ and $5, 6$.

# Example 2

`vecine.in`
```
2 18
3 2 1 2 1 0 6 3 0 5 6 3 0 6 9 2 9 3
```

`vecine.out`
```
6305
```

## Explanation

For the second example, we can concatenate the following sequences:
[$3, 2, 1, 2, 1, 0, 6, 3, 0, 5, 6, 3, 0, 6, 9, 2, 9, 3$] $\rightarrow$ [$3, 2, 1, 2, 1, 0, 6305, 6306, 9, 2, 9, 3$]

The pair with the largest two consecutive neighboring numbers is $6305$ and $6306$. According to the task, only the first number of the pair was written to the file.
