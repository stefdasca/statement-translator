
Didel learned today in math what a rectangle is. He defined the special number of a pair $(x, y)$ as follows: He drew a rectangle with length $x$ and width $y$. The special number will be the number of squares (with natural side lengths greater than $1$) included in the drawn rectangle.

~[special.png|align=center|width=400px]

$$
\text{The square drawn by Didel for} \ x = 3, \ y = 3
$$
In the figure above, there are $4$ squares with side $2$ and $1$ square with side $3$. Hence, the special number of the pair $(3, 3)$ will be $5$.

# Task

An array of $n$ integers, $a_1, a_2, \dots, a_n$, is given. $q$ updates of form $l \ r \ x \ y$ are given: Add to $a_l, a_{l + 1}, \dots, a_r$ the special number of the pair $(x, y)$. After all updates, find the maximum in the array $a$.

# Input data

The first line of the input file `special.in` contains two integers, $n$ and $q$, representing the number of elements in the array and the number of updates. The second line contains $n$ integers, separated by spaces, $a_1, a_2, \dots, a_n$. The following $q$ lines contain the $q$ updates (on the $(i + 2)$-th line you will find the numbers $l_i, r_i, x_i, y_i$ (separated by spaces), representing the form of the $i$-th update).

# Output data

The first line of the output file `special.out` will contain a single integer, the maximum in the array $a$.

# Constraints and clarifications

* $1 \leq n, q \leq 100 \ 000$
* $1 \leq a_i \leq 10 ^ 9$ (for $1 \leq i \leq n$)
* After all updates, $1 \leq a_i \leq 10 ^ {18}$.
* $1 \leq l_i \leq r_i \leq n$ (for $1 \leq i \leq q$)
* $1 \leq x_i, y_i \leq 10 ^ 9$ (for $1 \leq i \leq q$)

# Example

`special.in`
```
5 4
1 2 3 4 5
1 4 6 7
1 2 3 4
4 5 2 1
2 4 5 1
```

`special.out`
```
80
```

## Explanation

The array $a$ becomes: $79 \ 80 \ 73 \ 74 \ 5$. The maximum is $80$.
