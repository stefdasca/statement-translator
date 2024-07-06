After traveling together around the world, Păcală and Tândală gathered a cart full of gold coins, and now they are pouring them all out in the yard and dividing them into $N$ piles. Păcală counts the coins in each pile and dictates to Tândală $N$ natural numbers that he needs to write in order on a slate. After hours of work, Păcală realizes that Tândală has written on a single line, in order, from left to right, all the numbers dictated by him, but stuck together. Now there is just a long string of digits on the slate. What should Păcală do now?

# Task

Knowing the $N$ natural numbers dictated by Păcală, write a program that determines:

1. The number of digits written on the slate by Tândală;
2. The $K$-th digit on the slate, in order from left to right;
3. The largest number that can be formed with exactly $P$ adjacent digits from the slate, considered in order from left to right.

# Input data

The file `aur.in` contains:

* The first line contains a natural number $C$ which represents the task number and can have the values $1$, $2$, or $3$.
* The second line contains a natural number $N$ if the task is $1$, or two natural numbers $N$ and $K$ (separated by a space) if the task is $2$, or two natural numbers $N$ and $P$ (separated by a space) if the task is $3$.
* The third line contains $N$ natural numbers separated by a space, representing, in order, the numbers that Păcală dictates to Tândală.

# Output data

The file `aur.out` will contain a single natural number on the first line representing the result determined according to each task.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $1 \leq K \leq 900\ 000$;
* It is guaranteed that there are at least $K$ digits written on the slate.
* $1 \leq P \leq 18$;
* It is guaranteed that there are at least $P$ digits written on the slate.
* All numbers dictated by Păcală are non-zero and have at most $9$ digits each.
* For a correct resolution of the first task, $20$ points are awarded.
* For a correct resolution of the second task, $30$ points are awarded.
* For a correct resolution of the third task, $40$ points are awarded.
* $10$ points are given by default (the corresponding tests are identical to the first example).

# Example 1

`aur.in`
```
1
7
25 9 13 459 2 79 9
```

`aur.out`
```
12
```

## Explanation

The task is $1$. Tândală wrote on the slate: $259134592799$. The number of digits written by Tândală is $12$.

# Example 2

`aur.in`
```
2
7 10
25 9 13 459 2 79 9
```

`aur.out`
```
7
```

## Explanation

The task is $2$. $N$ has the value $7$ and $K$ has the value $10$. On the slate is written: $259134592799$, the tenth digit is $7$.

# Example 3

`aur.in`
```
3
7 4
25 9 13 459 2 79 9
```

`aur.out`
```
9279
```

## Explanation

The task is $3$. $N$ has the value $7$ and $P$ has the value $4$. Tândală wrote on the slate: $259134592799$. The largest number formed from four digits is $9279$.