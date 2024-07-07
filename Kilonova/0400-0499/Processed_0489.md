
# Task
Baker Ilie has just finished his $N$ wonderful breads. Each dough can be represented in the Cartesian coordinate system as a triangle with vertices at integer coordinate points.
Costel, the mischievous son of the baker, has just taken a large knife and started cutting the breads. Each cut that Costel makes corresponds to a horizontal line $(y = c)$ or a vertical line $(x = c)$ in the coordinate system.
\
Help the baker evaluate the damage caused by Costel's cuts. Your task is to determine, for each cut made by Costel, how many breads are cut. (A bread is considered cut if both pieces determined by the cut have areas greater than 0).
\
**Note: Input data is read from the keyboard, and output data is displayed in the console.**

# Input data
The first input line contains the natural number $N$, the number of breads.
Each of the next $N$ lines contains six natural numbers less than $10^6$. These numbers are, in order, the coordinates $(x1, y1), (x2, y2), (x3, y3)$ of the vertices of the breads. The three vertices will not all be on the same line. The pastries can touch and overlap.
The next line contains the natural number $M$, the number of cuts made by Costel. Each of the next $M$ lines contains a single equation of the cut line: $(y = c)$ or $(x = c)$, where $c$ is a natural number less than $10^6$.

# Output data
For each cut, print on a separate line the number of breads cut by Costel.

# Constraints and clarifications
- $2 \le N \le 100\ 000$
- $2 \le M \le 100\ 000$
- $(x_{1k}, y_{1k}), (x_{2k}, y_{2k}), (x_{3k}, y_{3k}) \le 10^6$
- For tests worth 40 points, $M \le 300$.
- For other tests worth 40 points, the coordinates of the breads, $(x_{1k}, y_{1k}), (x_{2k}, y_{2k}), (x_{3k}, y_{3k}) \le 1000$.
- For the remaining 20 points, there are no other constraints.
- It is worth noting that Costel's cuts are almost harmless and do not modify the breads.

# Example 1
`stdin`
```
3
1 0 0 2 2 2
1 3 3 5 4 0
5 4 4 5 4 4
4
x = 4
x = 1
y = 3
y = 1
```

`stdout`
```
0
1
1
2
```

# Example 2

`stdin`
```
4
2 7 6 0 0 5
7 1 7 10 11 11
5 10 2 9 6 8
1 9 10 10 4 1
4
y = 6
x = 2
x = 4
x = 9
```
`stdout`
```
3
2
3
2
```
