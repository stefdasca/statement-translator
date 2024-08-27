## Density

Dubota the sheep has learned from the math teacher sheep about prime numbers. Besides the definition of prime numbers (a prime number can only be divided by $1$ and itself), the teacher also mentioned a few words about the prime number theorem. One result of this theorem is that approximately one in $13$ numbers between $1$ and $500000$ are primes. Dubota cannot believe that there are so many prime numbers and does not trust the teacher, so he decided to investigate the problem using normal methods, with the help of a computer (because he does not know math). However, Dubota is a beginner programmer and asks you to help him quickly answer $Q$ questions of the type: How many prime numbers are there between $a$ and $b$, where $a, b \leq N$.

## Input data

The input file `densitate.in` will contain on the first line $N$ and $Q$. The next $Q$ lines contain $2$ numbers each, $a_i, b_i$ with the meaning explained in the task.

## Output data

The output file `densitate.out` will contain $Q$ lines, on which the answers to Dubota's questions are printed in order.

## Constraints and clarifications

$N < 500000$

$Q < 100000$

$1 \leq a \leq b \leq N$

## Example

`densitate.in`

`30 10 1 4 1 10 1 11 1 12 1 13 1 30 7 19 8 18 7 20 8 29 2 4 5 5 6 10 5 3 5 6`

`densitate.out`

`2 4 5 5 6 10 5 3 5 6`

## Explanations

The prime numbers between $1$ and $30$ are: $2, 3, 5, 7, 11, 13, 17, 19, 23, \text{and} 29$.