Gigel, an avid fan of math and computer science problems, noticed that some prime numbers have an interesting property: if any digit is removed from such a number, the resulting number is still a prime number. He called such numbers extra prime numbers. For example, the number $317$ is an extra prime: it is a prime number and, in addition, if we remove the digit $3$, we get $17$, which is prime; if we remove $1$, we get $37$, which is prime; if we remove $7$, we get $31$, which is also a prime number.

# Task

We say that $x$ is between $a$ and $b$ if $a \leq x \leq b$. Given two natural values $a$ and $b$, determine how many extra prime numbers exist between $a$ and $b$, as well as the smallest and the largest extra prime number between $a$ and $b$.

# Input data

The first line of the input file `extraprime.in` contains the two natural values $a$ and $b$, separated by a space.

# Output data

The output file `extraprime.out` will have $3$ lines. The first line will contain a natural number $nr$ representing the number of extra prime numbers between $a$ and $b$. The second line of the output file will contain the smallest extra prime number between $a$ and $b$, and the third line of the output file will contain the largest extra prime number between $a$ and $b$.

# Constraints and clarifications

* $10 \lt a \leq b \leq 10 \ 000 \ 000$;
* The number $1$ is not prime;
* For the test data, there is always a solution;
* The answers to the three tasks must be written exactly on the indicated line; if you do not know the solution to one of the tasks, the value $-1$ will be written on the corresponding line;
* Correctly writing the number of extra prime numbers will give $40\%$ of the score; correctly determining and displaying the smallest extra prime number will give $30\%$ of the score; correctly determining and displaying the largest extra prime number will give $30\%$ of the score;
* Each line in the input file ends with the end-of-line character.

# Example

`extraprime.in`
```
10 100
```

`extraprime.out`
```
4
23
73
```

## Explanation

There are $4$ extra prime numbers greater than $10$ and less than $100$: $23$, $37$, $53$, and $73$.