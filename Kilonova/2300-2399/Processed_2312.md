
Grandmother Miruna has $N$ grandchildren who are lined up from left to right and are numbered in order with distinct natural numbers from $1$ to $N$. Since Children's Day is approaching, Miruna has bought several Kinder eggs for her grandchildren. These Kinder eggs are not all the same but come in $M$ types (numbered from $1$ to $M$) and two colors ($0$ - red and $1$ - blue). The type of the egg specifies how tasty the egg is (if type $t_1 < t_2$, then an egg of type $t_1$ will be tastier than an egg of type $t_2$).
Miruna will perform operations of the following $3$ types:

|Type|Name|Format|Effect|
|-|-|-|-|
|1|Update|$c \\ t \\ p \\ nr$|Child $c$ receives $nr$ eggs of type $t$ and color $p$|
|2|Update|$c \\ t$|Child $c$ takes each egg of type $t$ that is theirs and paints it in the opposite color (from $0$ to $1$ or from $1$ to $0$)|
|3|Query|$a \\ b \\ p \\ x$|Miruna looks at the eggs of color $p$ belonging to the children in the interval $[a, b]$ and wants to know the type of the $x$-th tastiest egg.|

# Task

Write a program that efficiently performs all the described operations.

# Input data

The input file `kinder.in` will contain on the first line $3$ natural numbers $N \\ M \\ T$, representing the number of grandchildren, the number of egg types, and the number of operations to be performed. Each of the following $T$ lines will describe an operation. The line describing an operation starts with a number ($1$, $2$, or $3$) which indicates the type of the operation, followed by $4$, $2$, or $4$ natural numbers according to the operation format. The values written on the same line are separated by a space.

# Output data

The output file `kinder.out` will contain one line for each $3$-type operation performed. On line $i$ is the answer for the $i$-th $3$-type operation from the input file.

# Constraints and clarifications

* $1 \\leq N \\leq 50\ 000$
* $1 \\leq M \\leq 50\ 000$
* $1 \\leq T \\leq 50\ 000$
* For type $1$ operations: $1 \\leq c \\leq N, 1 \\leq t \\leq M, 0 \\leq p \\leq 1, 1 \\leq nr \\leq 1\ 000$
* For type $2$ operations: $1 \\leq c \\leq N, 1 \\leq t \\leq M$
* It is guaranteed that child $c$ has at least one egg of type $t$
* For type $3$ operations: $1 \\leq a \\leq b \\leq N, 0 \\leq p \\leq 1$
* $1 \\leq x \\leq$ Total number of eggs of color $p$ held by the grandchildren in the interval $[a, b]$
* It is guaranteed that the grandchildren in the interval $[a, b]$ hold at least one egg of color $p$.

# Example

`kinder.in`
```
5 100 3
1 2 68 0 100
2 2 68
3 1 5 1 99
```

`kinder.out`
```
68
```

## Explanation

Miruna has $5$ grandchildren, $100$ types of eggs, and performs $3$ operations.
In the first operation, child $2$ receives $100$ eggs of type $68$ and color $0$
In the second operation, child $2$ paints the $100$ eggs of type $68$ they have in color $1$
In the third operation, Miruna sees that the $99$-th tastiest egg of color $1$ for the grandchildren in the interval $[1, 5]$ has type $68$
