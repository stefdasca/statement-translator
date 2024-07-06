We consider $N$ arrays with integer elements, numbered from $1$ to $N$, sorted in ascending order, each array having a specified number of elements.

# Task

Answer $Q$ questions of the type:
1. `1 i j` — what is the minimum of the absolute differences between any two elements, the first element belonging to the array numbered $i$, and the second element belonging to the array numbered $j$?
2. `2 i j` — what is the value found at the median position in the array obtained by merging the arrays having the order numbers $i, i+1, \dots, j$, $(i < j)$?

# Input data

The input file `qvect.in` contains the first line with two natural numbers $N$ and $Q$, separated by a space, representing the number of arrays, and the number of questions, respectively.

Each of the following $N$ lines contain the description of an array in the form: $k, a_1, a_2, \dots, a_k$, where $k$ represents the number of elements, and $a_1, \dots, a_k$ represent the elements of the array, separated by a space.

Each of the following $Q$ lines contain the description of a question in the form of a triplet of natural numbers: $t, i, j$, separated by a space, where $t$ represents the type of question and can only take the values $1$ or $2$, and $i$ and $j$ have the significance specified in the task.

# Output data

The output file `qvect.out` will contain $Q$ integers, one per line, representing in order, the answers to the $Q$ questions.

# Constraints and clarifications

* $1 \leq N, i, j \leq 100$
* $1 \leq Q \leq 1 \ 000$
* $1 \leq t \leq 2$
* $1 \leq k \leq 5 \ 000$
* $-10^9 \leq a_1, a_2, \dots, a_k \leq 10^9$.
* The value found at the median position of an array $a$ with $k$ elements is understood as the value of the element at position $\lfloor \frac{k}{2} \rfloor$, i.e., the integer part of $\frac{k}{2}$.
* $15\%$ of the tests will contain only questions of type $1$.
* $15\%$ of the tests will contain only questions of type $2$.

# Example 1

`qvect.in`
```
3 3
7 1 4 5 8 11 18 19
6 2 4 5 10 21 29
4 13 14 15 15
2 2 3
1 2 3
2 1 3
```

`qvect.out`
```
13
3
10
```

## Explanation

The first question is of type $2$. The new array obtained by merging the arrays numbered $2$ and $3$ is $2, 4, 5, 10, 13, 14, 15, 15, 21, 29$ and contains $6 + 4 = 10$ elements, the value of the median element is $13$.

The second question is of type $1$. The minimum difference is obtained for the pair $(10,13)$, where the value $10$ belongs to the array numbered $2$, and the value $13$ belongs to the array numbered $3$.

The third question is of type $2$. The median position in the new array obtained by merging is $\frac{7+6+4}{2} = 8$, so the value found at the median position is $10$.