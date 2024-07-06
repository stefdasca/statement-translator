Below is the translated statement from Romanian to English, following your instructions:

---

A sequence with $n$ natural numbers on positions from $1$ to $n$ is given.

We define the influence of a number (denoted by $k$) as equal to the number of factors that appear in its writing as a product of prime numbers. For example, the influence of the number $24$ is $4$, because $24 = 2 \cdot 2 \cdot 2 \cdot 3$. When it manifests its influence, a number in the sequence affects the element at its position, the elements at most $k$ positions to its left, and the elements at most $k$ positions to its right. All these values are increased by $k$.
For each position $p$ from $1$ to $n$, the number in the initial sequence at position $p$ manifests its influence only once. All these operations take place at the same time.

# Task

Write a program that solves the following tasks:
1. What is the largest prime number in the initial sequence?
2. What is the sum of the smallest and largest numbers in the sequence obtained after all the numbers in the initial sequence manifest their influence?

# Input data

The input file `influent.in` contains on the first line a value $c$ which can be only $1$ or $2$, the second line contains a non-zero natural number $n$, the third line contains a sequence of $n$ non-zero natural numbers, separated by a space.

# Output data

If the value of $c$ is $1$, then only task 1 from the prompt will be solved. In this case, the output file `influent.out` will contain on the first line the required number.
If the value of $c$ is $2$, then only task 2 from the prompt will be solved. In this case, the output file `influent.out` will contain on the first line the sum required.

# Constraints and clarifications

* $n$ is a natural number, $1 \leq n \leq 50 \ 000$;
* The numbers on the third line of the file are natural numbers between $2$ and $100 \ 000$;
* For 12 points, we have $c = 1$ and all numbers in the sequence are prime;
* For another 22 points, $c = 1$;
* For 28 points, we have $c = 2$ and all numbers in the sequence are prime;
* For 38 points, we have $c = 2$.

# Example 1

`influent.in`
```
1
6
291 11 992 456 71 13
```

`influent.out`
```
71
```

## Explanation

The task is 1. The largest prime number in the sequence is $71$.

# Example 2

`influent.in`
```
2
5
12 10 100 5 6
```

`influent.out`
```
125
```

## Explanation

The task is 2.
For example, the number in the initial sequence at position $2$, with a value of $10$, has an influence of $2$ ($10 = 2 \cdot 5$) and affects the value at position $2$ (its position), the value at position $1$, and the values at positions $3$ and $4$. We notice that to the left a single value is affected as there are fewer than $k$ values.
The final sequence is: $(21, 19, 112, 17, 13)$.
The sum of the smallest and the largest number in it is $13 + 112 = 125$.

---