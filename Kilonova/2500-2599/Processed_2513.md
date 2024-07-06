Ron Weasley wants to help Harry Potter build magic wands. Hermione is away, so Ron has to manage on his own and we know how his spells usually turn out... For this reason, he needs your help. Ron has elder branches of different lengths and a magic ruler marked, at each centimeter, with consecutive natural numbers starting from $1$. A natural number on the magic ruler is enchanted if it has the property of being the square of a prime number. The power of a branch is equal to the number of enchanted numbers covered by it on the magic ruler. To create a wand, Ron places the branches on the ruler with the left end of each branch exactly at the natural number marked on the ruler. If two or more branches overlap or touch, they form a single wand. If two or more elder branches placed on the ruler neither overlap nor touch, they result in different wands. For example, if Ron places an elder branch 7 centimeters long with the left end at position marked with number 4, the branch will have a power of 2 (because it will cover the enchanted numbers 4 and 9). If he then places another branch, 2 centimeters long, with the left end at the position marked with the number 11, this branch will have a power of 0 and the two branches placed will form together a wand because they touch. If he then places another branch, 1 centimeter long, with the left end at the position marked with the number 14, this branch will have a power of 0 and will form a wand alone because it neither overlaps nor touches other branches.

~[img1.png|align=center|width=80%]

# Task

Write a program that, knowing the number of elder branches and for each of these the position on the ruler at which the left end is placed and the length of the branch measured in centimeters, solves the following two tasks:

1. determine the highest power of one of the branches used by Ron;
2. determine the number of wands made by Ron.

# Input data

The input file `ron.in` contains on the first line the numbers $c$ and $n$ representing the task that must be solved ($1$ or $2$), respectively the number of elder branches. The next $n$ lines describe the elder branches, one branch per line, in the form of two natural numbers $poz$ and $l \ g$ representing, in this order, the natural number on the magic ruler in front of which the left end of the branch was placed, and the length in centimeters of the branch. The numbers written on the same line are separated by a space.

# Output data

The output file `ron.out` will contain a single line which will have a natural number representing the result for task $c$ from the input file.

# Constraints and clarifications

* $2 \le n \le 50\ 000$
* $1 \le poz, l \ g \le 10^{9}$

| # | Points | Constraints |
| - | - | ------------ |
| 1 | 22 | $C = 1$; $n \le 1\ 000$; $poz, l \ g \le 100\ 000$ |
| 2 | 20 | $C = 1$ and there are no additional constraints |
| 3 | 25 | $C = 2$; $n \le 1\ 000$; $poz, l \ q \le 100\ 000$ |
| 4 | 33 | $C = 2$ and there are no additional constraints |

# Examples

`ron.in`
```
1 4
19 9
6 1
9 17
8 1
```
`ron.out`
```
2
```

`ron.in`
```
2 4
19 9
6 1
9 17
8 1
```
`ron.out`
```
2
```

## Explanation

The first branch has a power of $1$ (covers the enchanted number $25$), the second branch has a power of $0$, the third branch has a power of $2$ (covers the enchanted numbers $9$ and $25$), and the fourth branch has a power of $0$. For the first example ($c = 1$), the maximum power of one of the branches used by Ron is $2$. For the second example ($c = 2$), two wands are obtained: the first, third, and fourth branches together form a wand because they overlap or touch. The second branch forms a wand alone.

~[img2.png|align=center|width=100%]