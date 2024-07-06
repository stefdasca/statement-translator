From a sequence of $N$ digits, numbered from $1$ to $N$, Ionel takes exactly $M$ digits located in consecutive positions. He sticks the selected digits together or shuffles them and then sticks them together to obtain the largest possible number.

# Task

Given $N, M$ and the $N$ digits from the sequence, determine:

1. the largest number that can be obtained from the first $M$ of the given $N$ digits;
2. where Ionel will take $M$ digits in consecutive positions to obtain a maximum number; if there are several positions corresponding to a maximum number, the choice will be made such that the number formed from the remaining digits, in the order they were, is as large as possible; if there are still several solutions, the maximum position is chosen.

# Input data

From the file `maxim.in`, read: $P$ from the first line, representing the task ($1$ or $2$), $N$ and $M$ from the second line, separated by a space, with the meaning from the statement, and from the third line, read the $N$ digits, separated by spaces.

# Output data

In the file `maxim.out`, write:

* for $P = 1$: the maximum number that can be obtained using the first $M$ digits out of the given $N$ digits, without spaces between the digits of the number;
* for $P = 2$: a number representing the required position.

# Constraints and clarifications

* $M, N$ are natural numbers, $1 \leq N \leq 500\ 000$, $1 \leq M \leq 1\ 000$, $M < N$
* The $N$ values on the third line are natural numbers between $0$ and $9$
* The sequence of $N$ digits can start with at most $M-1$ zeroes.
* $30$ points will be obtained by solving task $1$, and $60$ points will be obtained by solving task $2$.
* $10$p will be granted automatically, provided the program compiles and executes normally within the allocated time.
* For $50$% of the tests, $N < 1000$ and $M < 10$.

# Example 1

`maxim.in`
```
1
10 3
7 2 8 1 0 0 4 7 8 1
```

`maxim.out`
```
872
```

## Explanation

Task $1$ is solved. With the first $3$ digits out of the given $10$ digits, you can form the numbers: $728, 782, 287, 278, 827, 872$, the largest being $872$.

# Example 2

`maxim.in`
```
2
10 3
7 2 8 1 0 0 4 7 8 1
```

`maxim.out`
```
7
```

## Explanation

Task $2$ is solved. By choosing the digits starting from position $7$ (digits $4, 7$ and $8$), the number $874$ is formed, which is the largest possible.

# Example 3

`maxim.in`
```
2
10 2
0 7 2 8 4 8 7 1 7 8
```

`maxim.out`
```
9
```

## Explanation

Task $2$ is solved. By choosing the digits starting from position $6$ (digits $8$ and $7$) or the digits starting from position $9$ ($7$ and $8$), the number $87$ is formed, which is the largest number of two consecutive digits. However, removing the digits at positions $6$ and $7$, the remaining sequence is $07284178$ (with the value $7284178$), whereas removing the digits at positions $9$ and $10$ leaves the number $7284871$, which is larger.

# Example 4

`maxim.in`
```
2
10 2
5 9 6 9 6 8 2 6 6 8
```

`maxim.out`
```
4
```

## Explanation

Task $2$ is solved. Choosing the digits at positions $2,3$ or $3,4$ or $4,5$ forms the number $96$, which is the largest number of two consecutive digits possible. However, removing the digits at positions $2$ and $3$, the remaining number is $59682668$, removing the digits at positions $3$ and $4$ the remaining number is $59682668$, and removing the digits at positions $4$ and $5$ the remaining number is $59682668$. Position $2$, $3$, or $4$ can be displayed, but the maximum position $4$ is chosen.