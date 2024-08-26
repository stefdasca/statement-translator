# Prime Numbers

Gheorghe learned about prime numbers at school. He learned that a number is prime if it is divisible only by $1$ and itself ($1$ is not considered a prime number). He found out that there are very efficient algorithms that can determine if a number is prime or not, even in sub-polynomial time. Unfortunately, these algorithms are very complicated, and Gheorghe thought of an approximation. His idea is to consider a number prime if it is not divisible by the first $K$ prime numbers. 

## Task

Demonstrate that Gheorghe's idea is merely an approximation. Given a number $K$, find the smallest number $N$ greater than $1$ that is not divisible by the first $K$ prime numbers but is not a prime.

## Input data

The input file `prim.in` will contain the number $K$.

## Output data

The output file `prim.out` will contain the number $N$ you are looking for.

## Constraints and clarifications

$1 \leq K \leq 100\,000$

## Examples

`prim.in` `prim.out`
$1$ $9$

### Explanation

$9$ is not divisible by $2$ and is also not prime.

## Examples

`prim.in` `prim.out`
$3$ $49$

### Explanation

The first $3$ prime numbers are $2, 3, 5$. Numbers that are not divisible by $2, 3$, or $5$ are: $7, 11, 13, 17, 19, 23, 31, 37, 41, 47, 49, \ldots$
$49$ is the smallest number that is not prime.