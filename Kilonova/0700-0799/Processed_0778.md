Marius, a middle school student, has developed a taste for problems involving prime numbers. He didn't miss the lesson where the teacher showcased the Sieve of Eratosthenes. But he wondered: if he were to create his special sequence, what should he call it—"Marius's Sieve"? How should this sequence look? He should start with a few prime numbers and then construct a sequence formed from those natural numbers which only have divisors among the initially given prime numbers. All numbers in the new sequence will be strictly ascending. For example, if he used $4$ prime numbers: $2$, $5$, $7$, $11$, then he could form the following sequence: $2$, $4$, $5$, $7$, $8$, $10$, $11$, $14$, $16$, $20$, $22$, etc. The sequence will not contain, for example, the value $6$, because $6$ has prime divisors $2$ and $3$, but the prime number $3$ is not among the initially given prime numbers. In the above example, in this newly formed sequence, the value at the third position is $5$, and at the tenth position is $20$. But at any given position in the sequence, what value will it be?

# Task

Given a sequence consisting of $n$ prime numbers and a natural number $m$, determine the value at position $m$ in the sequence formed from strictly ascending values that only have divisors from the initial sequence of given prime numbers.

# Input data

The input file `numar.in` contains on the first line two natural numbers separated by a space $n \\ m$, meaning: $n$ number of prime values, and $m$ the position of the value in the described sequence. The second line contains the $n$ prime numbers given in strictly ascending order, separated by spaces.

# Output data

The output file `numar.out` contains a single value, the $m$-th value in the sequence of numbers generated according to the described rule.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* $1 \leq m \leq 15 \ 000$;
* The problem data will be such that the representation of the highest value can be described on 31 bits.

# Example

`numar.in`
```
4 19
2 3 5 7
```

`numar.out`
```
27
```

## Explanation

The sequence of determined values is: $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$, $10$, $12$, $14$, $15$, $16$, $18$, $20$, $21$, $24$, $25$, $27$

