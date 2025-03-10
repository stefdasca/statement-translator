# Task

On a beautiful summer day, Vasile, a 12th-grade student preparing for the baccalaureate exam, was studying computer science. He is at his grandparents' house, where there is no internet, and spent the whole day solving matrix exercises. He decided to take a break, picked up the sheet with a matrix of dimensions $ N \times M $ containing integer values, and went into the yard to find a new activity.

Outside, he found an anthill and decided to play a little game with $F$ of the ants. He will take each ant, one by one, and place it in the bottom left corner of the matrix, considered to have coordinates $ ( 0, 0 ) $. He analyzes the path of each ant and notes some points through which it passes. If an ant passes through a cell of the matrix, then the value in that cell will be added to the ant's score.

The ants found by Vasile are intelligent, therefore they have the following properties:
- Each ant will head towards the point with coordinates $ ( M, N ) $;
- The ants move in a straight line between two consecutive points observed by Vasile;
- The coordinates of the points have real values with exactly two decimals;
- They do not want to waste time, so they will never deviate from their target (they stay on the grid). In other words, for two consecutive points $P$ and $Q$, $x_Q - x_P \ge 0$ and $y_Q - y_P \ge 0$.

***Attention! The path of the ants is described in the Cartesian plane. See the example drawing!***

Vasile is intrigued by these behaviors and wants to know the score for each ant.

# Input data

The first line will contain the dimensions of the matrix, $N$ and $M$. The next $N$ lines will contain $M$ integers $v_i$, representing the numbers in Vasile's game matrix. The next line will contain $F$, representing the number of ants participating in the race. The following $F$ lines will contain pairs of coordinates $ ( x_i, y_i ) $, real numbers with **exactly** two decimals, representing the observed points for ant $i$. The last coordinate for an ant will be $ ( M, N ) $.

# Output data

On line $i$, print the score of the ant number $i$.

# Constraints and clarifications

* $1 \leq N, M \leq 500$;
* $-5000 \leq v \leq 5000$;
* $1 \leq F \leq 10^5$;
* $0 \leq x_i \leq N$;
* $0 \leq y_i \leq M$;
* We denote by $L_{i}$ the length of the path of ant $i$
* $1 \leq L_{i} \leq 5\ 000$ for $i$ from $1$ to $F$
* The sum of $L_{i}$ for $i$ from $1$ to $F \leq 10^6$
* For tests worth $11$ points, for two consecutive points $P$ and $Q$, $x_Q - x_P = 0$ or $y_Q - y_P = 0$, and all points have integer coordinates;
* For tests worth $30$ points, $F \leq 100$, $1 \leq N, M \leq 50$;
* For tests worth $28$ points, all points have integer coordinates;
* For tests worth $42$ points, there are no additional restrictions;
* **If an ant moves along the edge of a cell and does not enter its interior, it will not receive the score of that cell.**
* **Attention!** The matrix of specific cell values is read in order from top to bottom (decreasing $y$), from left to right (increasing $x$). Intermediate points are given by their Cartesian coordinates ($x$, $y$).

# Example 1

`stdin`
```
5 5
2 8 4 8 -1
9 5 3 1 4
10 0 10 6 7
11 -1 7 10 9
5 0 20 -15 8
4
3.80 1.20 4.60 3.66 5.00 5.00
1.20 1.70 2.10 3.75 5.00 5.00
0.00 4.00 3.00 4.00 3.00 5.00 5.00 5.00
3.00 3.00 5.00 5.00
```

`stdout`
```
39
34
0
14
```

## Explanation

~[furnici.png|width=40%|height=40%] 
The first ant will pass through the following cells:
* $\\red{5 \\rightarrow 0 \\rightarrow 20 \\rightarrow -15 \\rightarrow 10 \\rightarrow 9 \\rightarrow 7 \\rightarrow 4 \\rightarrow -1} $
* $\\red{\\text{Total score} = 39}$

The second ant will pass through the following cells:
* $\\green{5 \\rightarrow 11 \\rightarrow -1 \\rightarrow 0 \\rightarrow 5 \\rightarrow 3 \\rightarrow 4 \\rightarrow 8 \\rightarrow -1} $
* $\\green{\\text{Total score} = 34}$

The third ant does not enter any cell, but only moves along their edges. Therefore, its score is $\\purple{0}$.
The fourth ant passes through the following cells:
* $\\blue{5 \\rightarrow -1 \\rightarrow 10 \\rightarrow 1 \\rightarrow -1} $
* $\\blue{\\text{Total score} = 14}$

The ant with the highest score is the first one, with a score of $\\red{39}$.

# Example 2

`stdin`
```
4 6
-7 -8 6 -3 1 10
10 -8 8 8 6 -1
-9 8 0 -10 0 -10
5 -9 -2 -7 -8 6
3
5.34 3.61 6.00 4.00
5.83 0.49 5.97 2.49 6.00 4.00
5.88 1.84 5.99 3.56 6.00 4.00
```

`stdout`
```
37
-16
-24
