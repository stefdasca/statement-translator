```markdown
The reverse of a natural number is the value obtained by reading its digits from right to left. For example, the reverse of the number $245$ is $542$. A number is a palindrome if it is equal to its reverse. For example, $121$ is a palindrome, while the number $21$ is not a palindrome.

Consider the **initial sequence** of natural numbers $0, 1, 2, 3, 4, \dots$

From this sequence, numbers divisible by $10$ are removed, and after each non-palindromic number, its reverse is inserted. The **new sequence** thus obtained is $1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 13, 31, \dots$

# Task

Write a program that reads:

1. a natural number $n$ and displays the $n$th eliminated number from the initial sequence;
2. a natural number $x$ and displays the following three numbers: $n_1$ – the number of occurrences in the new sequence of the number obtained from $x$ by removing its last digit; $n_2$ – the number of occurrences in the new sequence of the number obtained from $x$ by removing its last two digits; $n_3$ – the number of occurrences in the new sequence of the number obtained from $x$ by removing its last three digits.
3. a natural number $k$ and displays the number of values with $k$ digits in the new sequence.

# Input data

The input file `numere.in` contains on the first line a natural number $C$, which can be $1, 2$, or $3$. The second line contains the natural number $n$, if $C=1$, or the natural number $x$, if $C=2$, or the natural number $k$, if $C=3$, with the numbers having the meaning from the statement.

# Output data

If the value of $C$ is $1$, resolve only task $1$. In this case, the output file `numere.out` will contain the $n$th eliminated number.
If the value of $C$ is $2$, resolve only task $2`. In this case, the output file `numere.out` will contain three numbers, $n_1, n_2, n_3$, with the meaning from the statement, in this order, separated by a space.
If the value of $C$ is $3$, resolve only task $3`. In this case, the output file `numere.out` will contain the number of values with $k$ digits in the new sequence.

# Constraints and clarifications

* $1 \leq n \leq 2\ 000\ 000\ 000$;
* $1\ 000 \leq x \leq 2\ 000\ 000\ 000$;
* $1 \leq k \leq 50$; ( $1 \leq k \leq 18$ , for tests worth $20$ points)
* For the correct solution of the first task, $10$ points are awarded, for the correct solution of the second task, $25$ points are awarded, and for the correct solution of the third task, $55$ points are awarded.

# Example 1

`numere.in`
```
1
2
```

`numere.out`
```
10
```

## Explanation

$n=2$ and the second eliminated number is $10$. (Since $C$ is $1$, only task $1$ is resolved)

# Example 2

`numere.in`
```
2
1205
```

`numere.out`
```
0 2 1
```

## Explanation

$x=1205$, the number $120$ does not appear in the sequence, so $n_1=0$.

$12$ appears twice, so $n_2=2$.

$1$ appears once, so $n_3=1$ (Since $C$ is $2$, only task $2$ is resolved).

# Example 3

`numere.in`
```
3
2
```

`numere.out`
```
153
```

## Explanation

$k=2$ and in the new sequence there are $153$ numbers with $2$ digits. (Since $C$ is $3$, only task $3$ is resolved)
```