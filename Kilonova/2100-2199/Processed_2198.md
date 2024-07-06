Andrei and Bogdan are playing with a number $x$. They write it twice on the floor, as shown in the image below (for $x = 1234$). Andrei jumps over each digit of the upper number, while Bogdan jumps over the lower number. Initially, Andrei is on the first digit of the upper number, and Bogdan is on the first digit of the lower number. Then, Andrei moves to the next digit (to the right), until he exits the upper number. At that point, he moves to the first digit, and Bogdan advances by one digit. This process continues until Bogdan exits the lower number. We say that the number $x$ "made them happy" if at any point during the game, the sum of the digit Andrei is on and the digit Bogdan is on is a single-digit number.

~[saritura.png|align=center|width=30em]
$$
\text{The numbers written by Andrei (the upper one) and Bogdan (the lower one).}
$$

# Task

Given two numbers, $a$ and $b$. Display how many numbers $x$ from $a$ to $b$ "would make Andrei and Bogdan happy" if they played with it.

# Input data

The input file `saritura.in` contains two integers, $a$ and $b$.

# Output data

The output file `saritura.out` will contain a single integer, the number of numbers from $a$ to $b$ that have the required property.

# Constraints and clarifications

* $1 \leq a \leq b \leq 10 ^ 9$
* $1 \leq b - a \leq 10 \ 000$

# Example

`saritura.in`
```
10 20
```

`saritura.out`
```
6
```

## Explanation

The numbers that "make Andrei and Bogdan happy" from $10$ to $20$ are: $10$, $11$, $12$, $13$, $14$, $20$. In total, there are $6$ numbers.