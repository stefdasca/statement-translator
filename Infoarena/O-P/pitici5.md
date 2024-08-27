# Dwarves5

In a forest, there are two types of dwarves: white dwarves and black dwarves. They want to stand in an Indian file, but each dwarf has a requirement: he wants to see in front of him a dwarf of a specific color, either white or black. Since they are very stubborn, they want to find an arrangement that satisfies each one's requirement. Since none of them know algorithmics, they ask you to write a program to generate such an arrangement for them. They mentioned that if you succeed in helping them, they will offer you 100 points.

## Task

It is known that the dwarves are numbered with distinct values from $1$ to $N$, where $N$ represents their total number. Each dwarf from number $1$ to number $N$ is given in order, and you are required to find a possible arrangement that satisfies all the above restrictions. At the same time, the sequence of values obtained after rearranging the dwarves should be lexicographically minimal. It is also known that the first dwarf is of color $C$, has the order number $0$, and is not among the initial dwarves. Moreover, he has no requirements.

## Input data

The input file `pitici5.in` contains on the first line the value $N$, representing the number of dwarves, and a character $C$ representing the color of the first dwarf who will remain first even after rearrangement, while the others will line up behind him. This character will have either the value `'A'`, which means the first dwarf is white, or the value `'N'`, which means he is black. On the next $N$ lines, there will be exactly two characters separated by a space. Each of these pairs of characters represents the information corresponding to each dwarf. The first character will state the color that the dwarf wants to see in front of him, and the second character will state the dwarf's own color.

## Output data

The output file `pitici5.out` will print on the first and only line a permutation of the first $N$ natural numbers. This permutation will represent the reordering of the $N$ dwarves such that all the described restrictions are met.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

It is guaranteed that there always exists a possible arrangement that satisfies the restrictions of the $N$ dwarves.

We say that an array $A=(a_1, a_2, \dots, a_N)$ is lexicographically smaller than an array $B=(b_1, b_2, \dots, b_N)$ if there exists a position $p$ such that $x_p < y_p$ and $x_1 = y_1$, $x_2 = y_2$, $\dots, x_{p-1} = y_{p-1}$.

## Example

`pitici5.in` 
```
6 A
N N
A A
N A
N N
N N
N A
```

`pitici5.out` 
```
2 4 1 3 6 5
```

## Explanation

The first dwarf in the sequence is already fixed and is white. The next $N$ dwarves will rearrange as follows: the second dwarf will be first, the fourth dwarf will become second, the first dwarf will be third, and so on. The sequence of initial positions, resulting in a minimal lexicographical arrangement that respects all the $N$ dwarves' restrictions is $2 4 1 3 6 5$. Other arrangements of the dwarves are also possible (for example $2 4 1 5 3 6$), but the sequences associated with these arrangements are not lexicographically minimal.