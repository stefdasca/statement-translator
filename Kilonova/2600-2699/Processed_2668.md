> On a camel, I go forward through the sandstorm...

Robert got lost in the desert, and due to the storm, he cannot see far.

The desert can be represented as a matrix with $N$ rows and $M$ columns. In each cell of the matrix, there is a type of objective (for example, pyramids, labyrinthine ruins, cacti, dunes) which is represented by a lowercase letter of the English alphabet.

To figure out where he is, Robert sends a message to Georgian with the type of objective he sees in the cell he is in and walks to find more information. More precisely, he starts on a random cell, sends Georgian the letter of that cell. He then moves to adjacent cells north, east, south, or west, and each time he enters a neighboring cell, he sends Georgian the respective letter. He can pass through the same cell multiple times and will send Georgian a message each time.

Georgian notices that Robert is under a curse, which makes him seem to walk in circles. Specifically, the string of characters that Robert sends is in the form $S \cdot K$ (the string $S$ concatenated $K$ times).

Help Georgian figure out where Robert is!

# Task

Given the matrix representing the desert map, the string of characters $S$, and $Q$ queries $K_i$, answer how many positions it is plausible for Robert to be knowing that the string of characters received by Georgian is $S \cdot K_i$. It is plausible for Robert to be in a cell of the matrix if there is a path from any cell to the considered one that does not exit the matrix, and the string of characters described by the path is equal to $S \cdot K_i$.

# Input data

The input file `piramida.in` contains:

On the first row, two numbers separated by a single space $N$ and $M$ representing the number of rows and columns of the given matrix.

The following $N$ rows will contain a string of length $M$ representing each line of the given matrix.

On the $N + 2$-nd row contains the string of characters $S$.

On the $N + 3$-rd row contains a single integer $Q$ representing the number of queries.

On the next row contain $Q$ integers $K_i$ representing the queries to which Georgian has to respond.

# Output data

The output file `piramida.out` contains on a single row the responses in order to the $Q$ queries, separated by a space.

# Constraints and clarifications

* $2 \leq N, M \leq 200$
* $1 \leq \text{\textbar}S\text{\textbar} \leq 200$
* $1 \leq Q \leq 100\ 000$
* $1 \leq K_i \leq 1\ 000\ 000\ 000$ for $i$ from $1$ to $Q$
* $K_i \leq K_{i+1}$ for $i$ from $1$ to $Q - 1$. In other words, the sequence $K$ is given in ascending order.

| # | Points | Constraints |
| - | ------- | ------------ |
| 1 |    6    | $N, M, \text{\textbar}S\text{\textbar} \leq 5$, $Q = 1$, $K_1 = 1$ |
| 2 |   13    | $\text{\textbar}S\text{\textbar} \leq 25$, $Q, K_i \leq 100$ |
| 3 |   10    | $N, M, \text{\textbar}S\text{\textbar} \leq 20$ |
| 4 |    9    | $N, M, \text{\textbar}S\text{\textbar} \leq 55$ |
| 5 |   16    | $N, M, \text{\textbar}S\text{\textbar} \leq 100$ |
| 6 |   46    | No additional constraints |

# Example 1

`piramida.in`
```
3 4
cbaz
azzz
bczz
abc
3
1 2 3
```

`piramida.out`
```
2 1 0
```

## Explanation

In the first example, for the first query, Robert observes the string `abc`. He can be at the end in the cell on the first row and first column or in the cell on the third row and second column.
Thus, the answer to the first query is $2$.

For the second query, Robert observes the string `abcabc`. This means he can end up in the cell on the third row and second column. Thus, the answer is $1$.

For the third query, Robert observes the string `abcabcabc`. There is no cell where he could be in the matrix, thus the answer is $0$ (Robert is a lost cause).

# Example 2

`piramida.in`
```
1 5
aabaa
aaab
2
1 2
```

`piramida.out`
```
1 1
```

## Explanation

In the second example, for the first query, Robert observes the string `aaab`. He can start either from the second column or the fourth column and both cases end up on the third column. 

The answer is thus $1$. Note that if he starts from the first or the last column, there is no path to reflect the string of characters sent by Robert.

For the second query, Robert observes the string `aaabaaab`. All valid paths that Robert will take will end up in the cell on the third column. 

Thus, the answer is $1$.