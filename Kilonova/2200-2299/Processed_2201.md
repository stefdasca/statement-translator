Dorel has a house at point $0$. He visited $n$ cities that are at points $a_1, a_2, \dots, a_n$. We say that Dorel liked a city if the value of the point it is at is prime. He wants to know in how many ways he can choose $3$ distinct cities that he liked, such that the distance between any two cities is less than or equal to $x$.

# Task

Two integers $n$ and $x$ are given, and an increasing sequence of $n$ integers, $a_1 \leq a_2 \leq \dots \leq a_n$. Find the number of ways to choose three prime numbers from the sequence, be they $a_p, a_q, a_r \ (p < q < r)$, which have the following property: Consider the numbers $a_q - a_p$, $a_r - a_q$, $a_r - a_p$. We want all of them to be less than or equal to $x$.

# Input data

The first line of the input file `orase.in` contains two integers, $n$ and $x$. The second line contains the $n$ numbers $a_1, a_2, \dots, a_n$.

# Output data

The first line of the output file `orase.out` will contain a single integer, the result.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$
* $0 \leq a_1 \leq a_2 \leq .. \leq a_n \leq 10 ^ 6$
* $1 \leq x \leq 10 ^ 6$
* For $40$ points, $n \leq 100$.
* For another $30$ points, $n \leq 10 \ 000$.

# Example

`orase.in`
```
8 5
2 3 4 5 7 8 11 13
```

`orase.out`
```
4
```

## Explanation

The chosen triplets are: $(2, 3, 5)$, $(2, 3, 7)$, $(2, 5, 7)$, $(3, 5, 7)$.