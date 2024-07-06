~[image2.png|align=left] Consider a card game with an unlimited number of columns. Initially, in the first column, there are $N$ cards with distinct numbers from the set ${1, 2, \dots, N}$ arranged in a certain order, while the subsequent columns are empty (without any cards). We call a sequence from the end of the column the last one or the last two or the last three, etc. cards in the column that have consecutive numbers written on them in increasing order, considered from bottom to top. For example, in Figures $1$ and $2$, two such columns with $6$ cards each containing numbers between $1$ and $6$ are represented. In Figure $1$, the sequence from the end of the column consists of only the card $1$. In Figure $2$, the sequence from the end of the column consists of the cards $3$, $4$, and $5$. It is observed that in the column from Figure $1$, there is also a sequence formed of the cards $2$, $3$, and $4$, but this is not at the end of the column.

The allowed game operations are:
* $A$. moving the sequence of cards from the end of a column to a new column, if that column is empty (contains no cards);
* $B$. moving the sequence of cards from the end of a column to the end of another column with cards, only if the moved sequence forms a sequence of consecutive numbers with those on the card or cards at the end of that column.

It is desired, through a minimum number of allowed operations, to obtain on one of the columns all the numbers from $1$ to $N$ in increasing order, considered from bottom to top.

For example, from the initial configuration in Figure $2$, configuration $1$ below can be obtained through an operation $A$. Then, through an operation $B$, configuration $2$ is obtained; through a new operation $B$, configuration $3$ is obtained; then the sequence $2,3,4,5,6$ is moved to an empty column (operation $A$); and then the sequence $1$ is moved over the sequence $2,3,4,5,6$ (operation $B$), obtaining the desired final configuration on the second column.

~[image.png|algin=left]

# Task

Knowing the value of $N$ and the values of the cards in the first column, determine the minimum number of operations required to obtain the sequence $1, 2, \dots, N$ on one of the columns.

# Input data

The file `solitar.in` contains on the first line the natural number $N$ and on the following line $N$ distinct natural numbers from the set ${1, 2, \dots, N}$, separated by a space, given in the order from the column, from top to bottom.

# Output data

The file `solitar.out` will contain a single line with a natural number $M$ representing the minimum number of operations required to obtain the desired sequence.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$

# Example

`solitar.in`
```
6
1 6 2 5 4 3
```

`solitar.out`
```
5
```

## Explanation

The $5$ moves are described in the problem statement.