Gina and Mihai always play the game **Cuart** together. They have at their disposal an array of $2 \cdot N$ cards containing natural numbers. The first $N$ cards, from left to right, belong to Gina, and the next $N$ to Mihai. Gina traverses the array, from left to right, and writes on a piece of paper, on the first line, a sequence of numbers obtained from the numbers on her cards, from which she has removed all even digits. Mihai does the same, writing on his paper, on the first line, the sequence of numbers obtained from the numbers on his cards, from which he has removed all odd digits. If all digits were removed from a number, or only digits equal to $0$ remain, then the number is ignored, so nothing is written on the paper.

Each child writes on their paper, on the second line, another sequence of numbers obtained as follows: for each number $X$ written on the first line, the child will write the largest natural number $K$ such that $1 + 5 + 9 + 13 + ... + K \leq X$. In the children's game, the number $X$ is called **cuart** if $1 + 5 + 9 + 13 + ... + K = $X$.

~[cuart.png]

In the example above, Gina did not write any cuart numbers on the first line, while Mihai wrote only one ($6 = 1 + 5$).

The rules for winning the game are as follows:

The child who has written the most cuart numbers on the first line wins. In this case, the winning score of the game is equal to the number of cuart numbers written by the winning child.
If the two children wrote the same number of cuart numbers, then the one who has the first number written on the first line larger than the other's first number will win. This first number written by the winner will represent the winning score.
If neither Gina nor Mihai have written any numbers on paper, it is considered a tie and no one wins.

# Task

Write a program that reads the number $N$ representing the number of cards each child has, and the $2 \cdot N$ numbers on the cards, in order from left to right and determines:

1) The largest number from the $2 \cdot N$ cards, for which no number was written on the first line (it was omitted), neither on Gina's paper nor on Mihai's paper; if no number was omitted, write $0$;
2) The winner of the game and output the number $1$ if Gina won, $2$ for Mihai, or $0$ in case of a tie.
3) The winning score of the game, or $0$ in the case of a tie.

# Input data

The input file `cuart.in` contains the following:
The first line contains a natural number $P$. For all input tests, the number $P$ can only have the value $1$, $2$, or $3$. The second line of the input file `cuart.in` contains the natural number $N$ representing the number of cards each child has, and the third line, in order from left to right, contains the numbers on the $2 \cdot N$ cards, separated by a space.

# Output data

If the value of $P$ is $1$, only point 1) from the task will be solved. In this case, the output file `cuart.out` will contain on the first line a natural number representing the answer to task 1).
If the value of $P$ is $2$, only point 2) from the task will be solved. In this case, the output file `cuart.out` will contain on the first line a natural number representing the answer to task 2).
If the value of $P$ is $3$, only point 3) from the task will be solved. In this case, the output file `cuart.out` will contain on the first line a natural number representing the answer to task 3).

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$;
* $1 \leq$ number on the cards $\leq 10^8$;
* A correct solution for the first task is awarded $20$ points, for the second task $30$ points, and for the third task $50$ points.

# Example 1

`cuart.in`
```
1
4
1234 48 284260 75 756 1232515 153 98
```

`cuart.out`
```
284260
```

## Explanation

$P = 1$, for this test, task 1) is solved.

Gina wrote the following numbers on her paper, in two lines:
```
13 75
5 21
```
Mihai wrote the following numbers on his paper:
```
6 22 8
5 9 5
```
The largest omitted number is $284260$

# Example 2

`cuart.in`
```
2
4
1234 48 284260 75 756 1232515 153 98
```

`cuart.out`
```
2
```

## Explanation

$P = 2$, for this test, task 2) is solved.
Mihai won since he has one cuart number, while Gina has none.

# Example 3

`cuart.in`
```
3
1
154 2181
```

`cuart.out`
```
28
```

## Explanation

$P = 3$, for this test, task 3) is solved.
Gina wrote the following numbers on her paper, in two lines:
```
15
9
```
Mihai wrote the following numbers on his paper:
```
28
13
```
Both children wrote one cuart number, but Mihai won because his first number on the first line is larger than Gina's. The winning score of the game is $28$.