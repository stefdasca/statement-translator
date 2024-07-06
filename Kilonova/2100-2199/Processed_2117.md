```markdown
# Task

Mișu received from Moș Nicolae a set of $N \cdot M$ glasses, which he arranged in the form of a matrix$^1$ with $N$ rows and $M$ columns. He also has two types of milk in unlimited quantities, creatively named _milk A_ and _milk B_, with which he can fill the glasses. Any glass can be filled either with milk of type $A$ or type $B$. Mișu denotes with $L[i][j]$ the type of milk with which the glass at row $i$, column $j$ is filled.

Since he is a curious child, Mișu wants to see how many$^2$ distinct ways he can fill the $N \times M$ glasses, if he respects the following $Q$ restrictions of the type:

`a b c d` - Considering the submatrix determined by the coordinates of its corners as follows:

* bottom-left corner at the glass with coordinates $(a,b)$;
* top-right corner at the glass with coordinates $(c,d)$. 

The arrangement of the glasses inside the submatrix must be a mirror image relative to the horizontal axis and relative to the vertical axis. Formally, the following restrictions must be respected:

* $L[a + i][j] = L[c - i][j]$ for any $0 \leq i \leq c - a$ and $b \leq j \leq d$;
* $L[i][b + j] = L[i][d - j]$ for any $a \leq i \leq c$ and $0 \leq j \leq d - b$.

Since Mișu drank too much milk, he asks you to calculate the number of ways to fill the glasses such that all the $Q$ restrictions are respected, modulo $998\ 244\ 353$.

# Input data

The first line will contain three integers $N,M$ and $Q$ - the number of rows, columns, and respectively the number of restrictions that must be respected. The next $Q$ lines will each contain four numbers $a, b, c, d$ - the coordinates of the bottom-left and top-right corners of a restriction that must be respected.

# Output data

Print a single number representing the number of different ways Mișu can fill the glasses respecting all the $Q$ restrictions, modulo $998\ 244\ 353$.

# Constraints and clarifications

* $^1$The matrix is 1-indexed;
* $^2$Two ways $L$ and $L'$ of filling the glasses are different if there is at least one glass such that $L[i][j] \neq L'[i][j]$;
* $1 \leq N, M \leq 300$;
* $1 \leq Q \leq 30\ 000$;
* $1 \leq a_i \leq c_i \leq N$;
* $1 \leq b_i \leq d_i \leq M$.

# Subtasks

|#|Points|Constraints|
|-|-|-|
|0|0|Sample|
|1|11|$N = 1$|
|2|13|the submatrices from the $Q$ restrictions do not intersect|
|3|32|$1 \leq \sum\limits_1^Q (c_i-a_i + 1)\cdot(d_i-b_i + 1) \leq 200\ 000$|
|4|44|No additional constraints|

# Example 1

`stdin`
```
4 5 2
1 2 3 4
1 1 4 5
```

`stdout`
```
16
```

# Example 2

`stdin`
```
10 10 3
1 1 4 4
5 5 10 10
8 1 10 3
```

`stdout`
```
229805564
```
```