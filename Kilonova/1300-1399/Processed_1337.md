Ionel has $n$ domino pieces of various heights. While playing, he places the pieces vertically in a sequence (on a graduated ruler), at not necessarily equal distances from each other. Ionel touches the first piece, it falls and may cause other pieces in the sequence to fall. If there are still pieces standing, he goes to the first piece that did not fall and touches it. This piece falls and may cause other pieces to fall as well. He continues this process until there are no more standing pieces.

# Task

Write a program that reads the natural number $n$ of pieces, the position on the ruler, and the height of each piece, in this order, and determines the minimum number of touches needed to make all the domino pieces fall as well as the maximum number of pieces toppled with a single touch.

# Input data

The input file `domino.in` contains:

* The first line contains the natural number $n$
* Each of the following $n$ lines contains two natural numbers $p$ and $h$, separated by a space, where $p$ represents the position of the piece on the ruler and $h$ represents the height of the domino piece, in this order.

# Output data

The output file `domino.out` will contain a single line with two natural numbers $a$ and $b$, in this order, separated by a space, where $a$ represents the minimum number of touches needed to topple all the pieces, and $b$ represents the maximum number of pieces toppled with a single touch of a piece.

# Constraints and clarifications

* The numbers $n$, $p$, and $h$ are non-zero natural numbers
* $1 \leq n \leq 1 \ 000$
* $1 \leq p \leq 5 \ 000$
* $1 \leq h \leq 5 \ 000$
* A domino piece at position $p$ with height $h$ will topple pieces up to position $p + h$ inclusive.
* The input file contains data in increasing order of the positions of the domino pieces.
* At a given position on the ruler, there can be only one domino piece.
* Ionel always starts with the piece placed at the smallest position.
* $50\\%$ of the score is awarded for correctly solving each requirement.

# Example

`domino.in`
```
5
10 10
14 10
27 2
28 10
37 5
```

`domino.out`
```
2 3
```

## Explanation

When the first piece is touched, the first two pieces will fall;
Touching the piece at position $27$ will topple the piece at position $28$ and this will also topple the last one.
The number of touches is $2$, and the maximum number of pieces toppled with a single touch is $3$.
~[domino.png|align=center]