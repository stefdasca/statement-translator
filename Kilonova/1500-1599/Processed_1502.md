Sure, here's the translated text:

---

I am fascinated by prime numbers. I consider that prime numbers are the "skeleton" of all numbers or their "atoms," because any natural number greater than $1$ can be written as a product of prime numbers. Recently I also found out other interesting properties related to prime numbers, for example:

1. There are an infinite number of prime numbers in the Fibonacci sequence. Do you remember the Fibonacci sequence? $0$, $1$, $1$, $2$, $3$, $5$, $8$, $13$, $\\dots$ It is the sequence in which each term, except the first two, is obtained as the sum of the two preceding terms.
2. There are natural numbers called "economic" numbers. A natural number is economic if the number of digits needed to write it is greater than the number of digits needed to write its prime factorization (i.e., than the number of digits needed to write the prime factors and their powers). For example, $128$ is economic because $128$ is written with $3$ digits, and its prime factorization is written with two digits $(2^7)$; $4374$ is economic because it is written with $4$ digits, while its prime factorization is written with $3$ digits $(2 \cdot {3^7})$. Notice that when a prime factor appears to the power of $1$, it is not necessary to write it.
3. Many natural numbers can be written as the sum of two prime numbers. But not all. For example, $121$ cannot be written as the sum of two prime numbers.

# Task

Write a program that reads the natural number $n$ and a sequence of $n$ natural numbers, then solves the following tasks:
1. Determine and display how many of the numbers in the given sequence are prime numbers from the Fibonacci sequence;
2. Determine and display how many of the numbers in the given sequence are economic numbers;
3. Determine and display how many of the numbers in the given sequence **cannot** be written as the sum of two prime numbers.

# Input data

The input file `prime.in` contains in the first line a natural number $c$ which represents the task ($1$, $2$ or $3$). The second line contains the natural number $n$. The third line contains a sequence of $n$ natural numbers separated by spaces.

# Output data

The output file `prime.out` will contain a single line that contains the answer to the task from the input file.

# Constraints and clarifications

* $1 < n \leq 50$;
* If $c = 1$ or $c = 3$ the natural numbers in the sequence are greater than $1$ and less than ${10}^7$;
* If $c = 2$ the natural numbers in the sequence are greater than $1$ and less than ${10}^{14}$;
* For correctly solving task $1$, $20$ points are awarded;
* For correctly solving task $2$, $50$ points are awarded;
* For correctly solving task $3$, $30$ points are awarded.

# Example 1

`prime.in`
```
1
5
2 10 13 997 233
```

`prime.out`
```
3
```

## Explanation

The task is $1$. The $3$ prime numbers from the Fibonacci sequence present in the sequence are $2$, $13$ and $233$.

# Example 2

`prime.in`
```
2
4
128 25 4374 720
```

`prime.out`
```
2
```

## Explanation

The task is $2$. The sequence contains two economic numbers ($128$ and $4374$).

# Example 3

`prime.in`
```
3
5
57 30 121 11 3
```

`prime.out`
```
4
```

## Explanation

The task is $3$. There are $4$ natural numbers in the sequence that cannot be written as the sum of two prime numbers: $57$, $121$, $11$, $3$.

---