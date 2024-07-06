For a natural number $N$, consider the array $a = (1, 2, 3, ..., N)$, so $a_i = i$ for any $i$, $1 \leq i \leq N$.
There are two types of operations that can be applied to this array:

1. The **type 1** operation specifies two values $i$ and $j$, with $1 \leq i \leq j \leq N$. The effect of this operation on the array is to reverse the sequence in the array that starts with the element at position $i$ and ends with the element at position $j$. For example, if in the array $a = (1, 2, 3, 4, 5, 6, 7)$ the operation $3 \ 6$ is applied, then the array becomes $a = (1, 2, 6, 5, 4, 3, 7)$. And in the array $a = (1, 4, 3, 2, 5, 6, 7)$, if the operation $4 \ 6$ is applied, then $a = (1, 4, 3, 6, 5, 2, 7)$.
2. The **type 2** operation consists of an index $i$, $1 \leq i \leq N$, and asks to display the value of the element that is currently at position $i$ in the array.

There are $M$ such operations in a given order.

# Task

Write a program that determines and displays the result for each type $2$ operation.

# Input data

The input file `oglinda.in` contains on the first line two natural numbers $N$ and $M$, separated by a space. Each of the next $M$ lines specifies one operation of type $1$ or $2$. A line can contain two or three numbers, as follows: `1 i j` (indicating a type $1$ operation) or `2 i` (indicating a type $2$ operation). The values on the same line are separated by a space.

# Output data

The output file `oglinda.out` contains a number of lines equal to the number of type $2$ operations that are defined in the input file. Each line contains a natural number representing the result for a type $2` operation present in the input file, in the order in which these are defined.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq M \leq 2 \ 000$
* For test values of $40$ points, we will have $1 \leq N \leq 2 \ 000$.
* It is guaranteed that $1 \leq i \leq j \leq N$ for type $1` operations and $1 \leq i \leq N$ for type $2` operations.
* It is guaranteed that there is at least one type $2` operation.

# Example

`oglinda.in`
```
10 4
2 3
1 2 7
2 3
2 1
```

`oglinda.out`
```
3
6
1
```

# Explanation

The initial array is: $1 \ 2 \ 3 \ 4 \ 5 \ 6 \ 7 \ 8 \ 9 \ 10$
The result of the operation $2 \ 3$ is to display the element at position $3$ (which is 3).
The result of the operation $1 \ 2 \ 7$ is to transform the array into: $1 \ 7 \ 6 \ 5 \ 4 \ 3 \ 2 \ 8 \ 9 \ 10$.
The result of the operation $2 \ 3$ is to display the element at position $3$ (which now is $6$).
The result of the operation $2 \ 1$ is to display the element at position $1$ (which now has the value $1$).