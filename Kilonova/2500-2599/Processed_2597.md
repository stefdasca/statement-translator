In Sosmania, there are $N$ sauce factories, numbered from $1$ to $N$. These factories use a set of their own ingredients for making the sauce. Nationally, $M$ types of ingredients are accepted, numbered from $1$ to $M$.

A sequence consisting of two or more factories is considered **compatible** if all factories in the sequence use at least one common ingredient. A sequence of factories $(i, j)$ with $1 \leq i < j \leq n$ consists of all factories whose order numbers $x$ are such that $i \leq x \leq j$.

For example, consider factories $1, 2, 3$ and $4$ which use the following ingredients:
1: $1, 2, 5, 3, 8$
2: $4, 2, 6$
3: $2, 4, 5, 8, 10$
4: $10$

$(1, 3)$ is a compatible sequence because all factories in the sequence use ingredient $2$, but the sequence $(1, 4)$ is not compatible because there is no ingredient that is used by all $4$ factories.

# Task

Given $N$, $M$, and the set of ingredients used by each of the $N$ factories, determine the number of compatible subarrays.

# Input data

The input file `sos.in` contains the natural numbers $N$ and $M$ on the first line. The next $N$ lines describe the sets of ingredients used by the $N$ factories, one set per line, in the following format:
* The first number on the line is $lg$ and represents the number of ingredients used by the factory;
* The next $lg$ numbers represent the ingredients used, in strictly increasing order.

Numbers on the same line are separated by a space.

# Output data

The output file `sos.out` will contain a single line that will contain the number of compatible subarrays.

# Constraints and clarifications

* $1 \leq N \leq 70 \ 000$
* $1 \leq M \leq 1 \ 000 \ 000$
* $1 \leq lg \leq 20$

|#|Score|Constraints|
|-|-|-|
|1|30|$1 \leq N \leq 100$|
|2|30|$100 < N \leq 1 \ 000$|
|3|40|$1 \ 000 < N \leq 70 \ 000$|

# Example

`sos.in`
```
4 15
3 2 5 12
6 1 2 5 7 10 13
2 2 4
7 1 3 4 6 11 14 15
```

`sos.out`
```
4
```

## Explanation

There are $4$ subarrays that satisfy the required property: $(1, 2), (1, 3), (2, 3), (3, 4)$.