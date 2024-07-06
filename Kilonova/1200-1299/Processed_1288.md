Tom has three baskets of apples containing $a$, $b$, and $c$ apples, respectively. Each day, Tom eats exactly $6$ apples: three from one basket, two from another basket, and one from the third basket. He wonders how to choose the baskets so that the remaining apples are equal after a minimal number of days. Being passionate about logic problems, he wants to know the answer even if he had enormous baskets with millions of apples.

# Task

Write a program that reads the numbers $a$, $b$, and $c$ and determines:

1. The smallest natural number representing the number of days after which the $3$ baskets will have an equal number of apples;
2. Three natural values, the first value representing the total number of apples eaten from the first basket, the second value representing the total number of apples eaten from the second basket, and the third value representing the total number of apples eaten from the third basket, if such values exist, to achieve an equal number of apples in the three baskets in the minimal number of days.

# Input data

The input file `mere.in` contains the first line three natural numbers $a$, $b$, $c$, separated by a space, representing the number of apples in each basket, in this order.

# Output data

The output file `mere.out` will contain two lines. The first line will contain the smallest natural number representing the minimal number of days after which the three baskets will have an equal number of apples. On the second line, three natural values will be written, separated by a space, the first value representing the total number of apples taken from the first basket, the second value representing the total number of apples taken from the second basket, and the third value representing the total number of apples taken from the third basket, if such values exist. If it is not possible to achieve an equal number of apples in all baskets, all $4$ numbers written in the output file will have the value $-1$ (both the first and the second line will contain the value $-1$).

# Constraints and clarifications

* Numbers $a$, $b$, $c$ are non-zero natural numbers at most equal to $700\ 000\ 000$
* For solving the first requirement, $1$ receives $50\%$ of the score and for requirement $2$, $50\%$ of the score.

# Example 1

`mere.in`
```
15 20 10
```

`mere.out`
```
5
10 15 5
```

## Explanation

One way to choose the baskets is as follows:
($15$, $20$, $10$) $\rightarrow$ ($13$, $17$, $9$) $\rightarrow$ ($11$, $14$, $8$) $\rightarrow$ ($9$, $11$, $7$) $\rightarrow$ ($7$, $8$, $6$) $\rightarrow$ ($5$, $5$, $5$)

# Example 2

`mere.in`
```
100 200 3
```

`mere.out`
```
-1
-1 -1 -1
```

## Explanation

In at most $3$ days, the apples in basket $3$ are finished.

# Example 3

`mere.in`
```
100 103 100
```

`mere.out`
```
2
3 6 3
```

## Explanation

For example: ($100$, $103$, $100$) $\rightarrow$ ($99$, $100$, $98$) $\rightarrow$ ($97$, $97$, $97$)

# Example 4

`mere.in`
```
20 15 8
```

`mere.out`
```
-1
-1 -1 -1
```

## Explanation

It is not possible to achieve an equal number of apples that is also a natural number.