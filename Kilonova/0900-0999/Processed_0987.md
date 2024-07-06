Here is the translated document with the specified instructions followed:

---

Let $N$ be a natural number.

# Task

Determine the sum of all natural numbers with the following properties:
- Their prime factorization contains the same prime factors as $N$;
- The sum of the exponents in their prime factorization is the same as that of $N$;
- They have the maximum number of divisors.

# Input data

The first line will contain the natural number $N$.

# Output data

The first line will contain a single natural number, representing the remainder of the sum when divided by $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq N \leq 10^{12}$;
* For 24 points, $1 \leq N < 10^{6}$;
* For 28 points, $10^6 \leq N < 10^{10}$;
* For 48 points, $10^{10} \leq N \leq 10^{12}$.

# Example 1

`stdin`
```
20
```

`stdout`
```
70
```

## Explanation

$20 = 2^2\cdot5^1$, $50 = 2^1\cdot5^2$, and both numbers have a maximum number of divisors, equal to $6$. 

The remainder of their sum when divided by $1 \ 000 \ 000 \ 007$ is equal to $70$. 

# Example 2

`stdin`
```
945
```

`stdout`
```
7455
```

## Explanation

* $1575 = 3^2\cdot5^2\cdot7^1$;
* $2205 = 3^2\cdot5^1\cdot7^2$; 
* $3675 = 3^1\cdot5^2\cdot7^2$.

All three numbers have a maximum number of divisors, equal to $18$. 

The remainder of their sum when divided by $1 \ 000 \ 000 \ 007$ is equal to $7455$. 

# Example 3

`stdin`
```
99999999
```

`stdout`
```
833333155
```

## Explanation

There are five natural numbers that meet the specified properties: $566 \ 666 \ 593$, $366 \ 666 \ 612$, $433 \ 333 \ 295$, $366 \ 666 \ 663$, and $99 \ 999 \ 999$. 

The sum of these numbers is equal to $1 \ 833 \ 333 \ 162$, and the remainder when this number is divided by $1 \ 000 \ 000 \ 007$ is equal to $833 \ 333 \ 155$.

---