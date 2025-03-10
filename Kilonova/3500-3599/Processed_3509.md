# Task

Little Gates has a problem to solve in computer science. He receives a sequence of $n$ natural numbers and must respond to the following tasks:

1. Determine how many numbers in the sequence have exactly two digits.
2. Determine the $k$-th digit that appears in the sequence of numbers. If it does not exist, print the message `nu exista`. The numbering of digits is done from left to right, starting with position $1$.
3. Determine the largest number that can be formed from at most $m$ consecutive digits found in the numbers from the given sequence, traversing the digits from left to right.

# Input data

The first line of the input file `numere.in` contains the number $c$ of the task, which can only be $1$, $2$, or $3$.

If the task is $1$, the second line contains the non-zero natural number $n$ and the third line contains $n$ natural numbers, separated by a space.
If the task is $2$, the second line contains the numbers $n$ and $k$ separated by a space, with the meaning given in the statement. The third line contains the $n$ natural numbers, separated by a space.
If the task is $3$, the second line contains the numbers $n$ and $m$ separated by a space, with the meaning given in the statement. The third line contains the $n$ natural numbers, separated by a space.

# Output data

The first line of the output file `numere.out` will contain the value determined according to the task.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* The numbers in the array are natural numbers with at most $9$ digits each.
* $1 \leq k \leq 900 \ 000$;
* $1 \leq m \leq 9$;
* For task $1$, $16$ points are awarded;
* For task $2$, $52$ points are awarded (for 8 points, the numbers in the array have a single digit);
* For task $3$, $32$ points are awarded, of which:
  * $m=1$ for $4$ points;
  * For another 28 points, $m \geq 2$ and $m \leq 9$.

# Example 1

`numere.in`
```
1
4 
23 4567 12 345
```

`numere.out`
```
2
```

## Explanation

The task is $1$.
We observe that there are two numbers in the sequence that have two digits ($23$ and $12$).

# Example 2

`numere.in`
```
2
3 10
23 4567 12345
```

`numere.out`
```
4
```

## Explanation

The task is $2$.
Traversing the numbers in the sequence, digit by digit, from left to right, we encounter the digits `2 3 4 5 6 7 1 2 3 4 5`. The $10$-th digit in this sequence is $4$.

# Example 3

`numere.in`
```
3
3 4
23 4507 12345
```

`numere.out`
```
7123
```

## Explanation

The task is $3$.
Traversing the numbers in the sequence, digit by digit, from left to right, several numbers of at most $4$ digits can be obtained, such as: $2345$, $3450$, $4507$, $5071$, $712$, $7123$, $1234$, $2345$. Among these, the largest number of at most 4 consecutive digits in the given sequence is: $7123$.