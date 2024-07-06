Ionel is a fourth-grade student, and his parents thought of an efficient method for him to learn large numbers and how they are formed. For this purpose, they bought him a game with tokens. For each digit, there are $10$ tokens inscribed on one side with the respective digit. Ionel can form numbers by placing the tokens next to each other. His parents ask him to form numbers, in sequence, that have the digit sum $S$ and are less than $10^a$. Since it is difficult to follow him in forming the numbers, his parents want to know how many such distinct numbers Ionel can form.

# Task

How many distinct numbers did Ionel form?

# Input data

In the file `jetoane.in`, the first line contains the number $S$, and the second line contains the number $a$.

# Output data

In the file `jetoane.out`, the number will be printed on a single line.

# Constraints and clarifications

* $1 \leq S \lt 10$
* $1 \leq a \lt 10$
* $S$ and $a$ are natural numbers

# Example 1

`jetoane.in`

```
2
3
```

`jetoane.out`

```
6
```

## Explanation

Ionel forms the numbers: $2, 11, 20, 101, 110, 200$

# Example 2

`jetoane.in`

```
5
5
```

`jetoane.out`

```
126
```

