## Task

N fantastic characters want to visit the enchanted forest. The enchanted forest has $P$ glades connected by paths of different lengths. Initially, the characters are in glade $1$. We know that any two paths will intersect only at a glade, and the total number of paths will be $P - 1$. Each of the $N$ characters follows the following strategy to visit the forest: From the glade where they are currently located, they choose a path they have not traveled before and follow it. Also, if there are multiple characters in the same glade who want to proceed on the same path, they will move as a group - traveling on that path at the speed of the slowest one (Harap-Alb's horse is faster than Cinderella's!). If a character reaches a glade from which they cannot exit (no unvisited paths), then that character will stop. We will call such a glade a terminal glade. We know that in the forest, there are at most $N$ terminal glades. We define the magical energy of the forest as being equal to the sum of distance $\cdot$ speed for each path (if a path will not be traversed, this sum will be $0$). The fantastic characters want you to find the maximum magical energy that can be obtained. If you are worthy of solving this problem, you will be rewarded with unimaginable pleasures$\dots$and $100$p.

## Input data

The input file `drumetii.in` will contain on the first line the number $N$ representing the number of fantastic characters. The second line of the input will contain $N$ numbers $V_1, V_2, \dots, V_N$, representing the travel speeds of the $N$ characters. The third line of the input will contain the number $P$. Each of the lines from $4$ to $4 + P - 2$ will contain a pair of numbers $X, Y, L$ signifying that there is a path from $X$ to $Y$ of length $L$.

## Output data

In the output file `drumetii.out` you must print the maximum magical energy that can be obtained.

## Constraints and clarifications

$2 \leq N \leq 16$

$1 \leq P \leq 500$

$1 \leq L \leq 100\,000$

$1 \leq V_i \leq 1\,000$

It is guaranteed that it is possible to reach any other node of the forest from node $1$.

An edge can be traversed in both directions.

A character is not allowed to wait in a glade. In other words, the case in which two characters are in the same node and both choose to go on the same path, the first character goes and the second waits and goes after them is invalid.

## Example

`drumetii.in`

```
3
3 4 9
3
1 2 10
1 3 10
```

`drumetii.out`

```
120
```

## Example

`drumetii.in`

```
4
81 372 461 987
4
1 2 64270
1 3 56978
3 4 28202
```

`drumetii.out`

```
89278530
```

## Explanation

In the first example, characters $1$ and $2$ will travel together to glade $2$, and the third character will travel alone to glade $3$. The first two characters will traverse the edge $(1, 2)$ at speed $3$, and character $3$ will traverse the edge $(1, 3)$ at speed $9$. The total cost will be $3 \cdot 10 + 9 \cdot 10 = 120$.