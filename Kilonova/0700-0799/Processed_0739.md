
Let $a$ and $b$ be two natural numbers. Represent these two numbers in base $2$. Apply the following transformation to the two values obtained through their base $2$ representation: if the first digit (leftmost) in the base $2$ representation of number $a$ is equal to the last digit (rightmost) in the base $2$ representation of number $b$, then remove the first digit (leftmost) in the base $2$ representation of number $a$ and the last digit (rightmost) in the base $2$ representation of number $b$ and continue the transformations in the same way until the first digit (leftmost) in the base $2$ representation of number $a$ is different from the last digit (rightmost) in the base $2$ representation of number $b$. The values remaining after the transformations are represented in base $10$, obtaining two numbers: $c$ and $d$.

1. If no transformation is performed on the two base $2$ representations because the first digit in the representation of number $a$ is different from the last digit in the base $2$ representation of number $b$, then the number $c$ will be identical to number $a$, and $d$ will be identical to number $b$.
2. If as a result of a transformation the last digit in the base $2$ representation is removed, the resulting number is $0$.

# Task

Write a program that reads the numbers $a$ and $b$ and displays the value obtained by summing the two numbers $c$ and $d$.

# Input data

The file `numere.in` contains two integers, $a$ and $b$.

# Output data

The file `numere.out` will contain a single integer, the sum of the two numbers as per the statement.

# Constraints and clarifications

* $1 \leq a, b \leq 2^{15}$;

# Example 1

`numere.in`
```
13
27
```

`numere.out`
```
1
```

## Explanation

In base $2$, the number $13$ is written as $1101$ in base $2$, the number $27$ is written as $11011$.

After the first transformation, $101$ and $1101$ are obtained. The transformations continue and $01$ and $110$ are obtained. The transformation continues and $1$ and $11$ are obtained. The transformation continues and $0$ and $1$ are obtained. After conversion, $c = 0$ and $d = 1$ are obtained. Thus, the sum $c + d$ is $1$.

# Example 2

`numere.in`
```
13
25
```

`numere.out`
```
17
```

## Explanation

In base $2$, the number $13$ is written as $1101$, and the number $25$ is written as $11001$.

After the first transformation, $101$ and $1100$ are obtained. From this point on, no more transformations can be made. The number $101$ is converted to base $10$ resulting in $5$, and $1100$ is converted to base $10$ resulting in $12$. Thus, $c = 5$ and $d = 12$, so the sum $c + d$ is $17$.

# Example 3

`numere.in`
```
13
20
```

`numere.out`
```
33
```

## Explanation

In base $2$, the number $13$ is written as $1101$, and the number $20$ is written as $1100$. 

It is observed that the first digit in the representation of $a$ is different from the last digit in the representation of $b$. Therefore, no transformation is made. After conversion to base $10$, $c = 13$ and $d = 20$. Thus, the sum $c + d$ is $33$.
