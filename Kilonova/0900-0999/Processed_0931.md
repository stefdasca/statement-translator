

Given a sequence of $N$ positive integers. The sequence elements are numbered from left to right starting from position $1$.

# Task

Write a program that determines the answer to questions of the following types:

1. What is the leftmost position that contains a value strictly greater than all those to its right? – question of type $1$
2. What are the positions that contain values strictly greater than all those to their left? – question of type $2$
3. If for each element between the first and last occurrence of the maximum we increase its value to be equal to the maximum, what is the total sum of the added values? – question of type $3$

# Input data

The input file `sir.in` contains on the first line a number $C$ (which can be $1$, $2$, or $3$), indicating the type of question. The second line contains a natural number $N$, representing the number of elements in the sequence. The third line of the input file contains $N$ positive integers, representing the elements of the sequence, given from left to right (the leftmost has position $1$ and the rightmost has position $N$). The numbers on this line are separated by spaces.

# Output data

If $C = 1$, the output file `sir.out` must contain a natural number that represents the answer to a question of type $1$. If $C = 2$, the output file must contain, separated by a space and in ascending order, the indices determined as the answer to a question of type $2$. If $C = 3$, the output file must contain a number that represents the answer to a question of type $3$.

# Constraints and clarifications

* $1 \leq C \leq 3$;
* $1 \leq N \leq 100\ 000$;
* The numbers in the given sequence range between $1$ and $10\ 000$ inclusive.
* For tests worth $24$ points, we have $C = 1$.
* For tests worth $32$ points, we have $C = 2$.
* For tests worth $44$ points, we have $C = 3$.

# Example 1

`sir.in`
```
1
7
3 2 2 5 3 5 4
```

`sir.out`
```
6
```

## Explanation

The leftmost position of a value that is greater than all those to its right is $6$ (where the value $5$ is).

# Example 2

`sir.in`
```
2
7
3 2 2 5 3 5 4
```

`sir.out`
```
1 4
```

## Explanation

$1$ and $4$ are the positions where the values are greater than all those to their left.

# Example 3

`sir.in`
```
3
8
3 2 2 5 3 1 5 4
```

`sir.out`
```
6
```

## Explanation

The maximum being $5$, according to the explanation for question of type $3$, two elements need to be increased to become equal to $5$. These are the elements at position $5$ (increased by $2$) and at position $6$ (increased by $4$). The sum of the values needed to increase is $2$ + $4$ = $6$.

# Example 4

`sir.in`
```
3
5
3 2 7 5 3
```

`sir.out`
```
0
```

## Explanation

The maximum is $7$ and appears only once, so no value is increased.
