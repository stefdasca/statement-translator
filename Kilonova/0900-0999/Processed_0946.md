On a wonderful spring day, $P$ ducks went for a walk on the lake. A military pelican, who was sitting on the shore, decided to train the innocent ducks. To do this, he immediately mapped the lake and represented it as a matrix with $N$ rows (numbered from $0$ to $N - 1$ from top to bottom) and $N$ columns (numbered from $0$ to $N - 1$ from left to right). Thus, the position of any duck on the lake can be identified by the row and column the duck is on. The ducks are facing one of the directions North, South, East, West. The pelican encoded the directions $1$, $2$, $3$, $4$ as shown in the figure.

~[pelican_01.png]

When the pelican shouts: “Commands to me!” the ducks must simultaneously execute the $K$ commands given by the pelican. The pelican's commands are encoded as follows:

* $A \\ nr$ – The duck advances $nr$ positions in the direction it is facing. If advancing exceeds the edge of the game board, it will enter from the opposite side. For example, on a $5$ x $5$ lake, a duck placed in position ($1, 3$) facing $1$ (North), executing the command $A \\ 3$ will move as follows: ($1, 3$) $\\rightarrow$ ($0, 3$) $\\rightarrow$ ($4, 3$) $\\rightarrow$ ($3, 3$).
* $R \\ nr$ – The duck rotates by $nr \\cdot 90 \\degree$ clockwise, where $nr \\in \{1,2,3,4\}$. For example, if the initial orientation of the duck is $1$ (North), the command $R \\ 2$ will change the orientation to $3$ (South).
* $Z \\ nr$ – The duck flies to row $nr / N$ and column $nr$ mod $N$, retaining its orientation. It is guaranteed that $nr / N \\in \{0,1, ..., N - 1\}$. For example, on a $5$ x $5$ lake, after executing the command $Z \\ 7$, the duck will end up on row $1$ and column $2$.

# Task

Write a program that, knowing the initial position on the lake of the $P$ ducks and the sequence of the pelican's commands, determines the final position of each duck.

# Input data

The input file `pelican.in` contains on the first line three natural numbers $N \\ P \\ K$, with the significance from the statement. The following $P$ lines contain $3$ natural numbers $i \\ j \\ d$ with the significance that on row $i$ and column $j$ there is a duck facing direction $d$. The last $K$ lines contain the $K$ commands, one command per line, in the specified format in the statement (a character from the set {'A', 'R', 'Z'} and a natural number). Values written on the same line are separated by a space.

# Output data

The output file `pelican.out` will contain $P$ lines. Each line $i$ will contain the position of the $i$-th duck from the input file (row and column separated by a single space) after executing in order the $K$ commands.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000$;
* $1 \\leq P \\leq 10 \\ 000$;
* $1 \\leq K \\leq 100 \\ 000$;
* $0 \\leq i, j < N$; and $1 \\leq d \\leq 4$;
* Multiple ducks can occupy the same position.
* It is guaranteed that the input file data is correct.
* For tests worth $76$ points, the input file does not contain the command $Z$.
* For tests worth $20$ points, $N \\leq 100$, $P \\leq 100$ and $K \\leq 1 000$.
* For tests worth $36$ points, $N > 100$, $1 \\ 000 \\leq P \\leq 5 000$; and $K \\leq 50 \\ 000$.

# Example

`pelican.in`
```
5 3 4
1 1 2
2 3 1
3 1 4
A 3
R 3
A 1
A 3
```

`pelican.out`
```
2 4
4 4
2 3
```

## Explanation

The lake has $5$ rows and $5$ columns. There are $3$ ducks positioned as shown in the figure.

~[pelican_02.jpg]

The pelican gives $4$ commands which all $3$ ducks execute in order. The ducks execute command $A \\ 3$

~[pelican_03.jpg]

The ducks execute command $R \\ 3$ (rotate by $270 \\degree$ clockwise)

~[pelican_04.jpg]

The ducks execute command $A \\ 1$

~[pelican_05.jpg]

The ducks execute command $A \\ 3$

~[pelican_06.jpg]