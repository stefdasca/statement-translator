Here is the translated competitive programming problem statement in English, following the given specifications:

```markdown
A two-dimensional array consisting of $N$ rows and $N$ columns is considered, containing free cells encoded with the value $0$ and blocked cells encoded with the value $1$. $M$ players are positioned in different cells of the matrix. A player can be positioned in a free cell or a blocked cell. Starting from moment $t_0 = 0$, at each integer moment $t$, each player colors the free cells at distance $t$ from the position they are in.

We define the distance between two cells $(i_1, j_1)$ and $(i_2, j_2)$ as equal to $max(|i_1 - i_2|, |j_1 - j_2|)$, where $i_1$ and $i_2$ correspond to the row indices and $j_1$ and $j_2$ correspond to the column indices of the cells.

# Task

Write a program that reads a natural number $N$, the values of the matrix and the initial positions of the players, and outputs the answer to $Q$ questions of the form: "What is the first moment in time after which we have at least $P$ colored cells in the matrix?" If for a question it is not possible to color $P$ free cells (no matter how much time passes), the answer for that question will be $-1$.

# Input data

The first line contains the number $N$, and each of the following $N$ lines contains $N$ numbers separated by a space, corresponding to the types of cells on the corresponding row in the matrix.

The line $N + 2$ contains the number of players $M$, and each of the following $M$ lines contains two natural numbers, separated by space, representing the row number and the column number in which each of the $M$ players is located.

The line $M + N + 3$ contains the natural number $Q$, representing the number of questions, and the last line contains $Q$ natural numbers separated by a space, representing the values of $P$, for each of the $Q$ queries.

Since the volume of input data is very large, if using the iostream library from the C++ standard for reading, we recommend adding the following instructions at the beginning of the main function:

```cpp
std::ios_base::sync_with_stdio(false);
std::cin.tie(0);
```

# Output data

The output consists of a single line, which will contain $Q$ numbers, separated by a space, corresponding to the answers to the given questions, in the order they were read.

# Constraints and clarifications

* $3 \leq N \leq 1500$
* $1 \leq M, Q \leq N^2$
* $1 \leq P \leq 10^9$
* Rows and columns are indexed starting from $1$.

|#|Points|Constraints|
|-|-|--------|
|1|12|$1 \leq N \leq 20$|
|2|33|$1 \leq M \leq 10$|
|3|21|$3 \leq N \leq 600$|
|4|34|No additional restrictions|

# Example

`stdin`
```
8
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 1
2
3 3
6 6
3
35 16 1000
```

`stdout`
```
2 1 -1
```

## Explanation

After the moment $t = 0$, only the cell $(3, 3)$ will be colored. (Total: $1$)

After the moment $t = 1$, the following cells will be additionally colored: $(2, 2)$, $(2, 3)$, $(2, 4)$, $(3, 2)$, $(3, 4)$, $(4, 2)$, $(4, 3)$, $(4, 4)$, $(5, 6)$, $(5, 7)$, $(6, 5)$, $(6, 7)$, $(7, 5)$, $(7, 6)$, $(7, 7)$. (Total: $16$)

After the moment $t = 2$, a total of $40$ cells will be colored.

For the first query, the first moment in time after which we have at least $35$ colored cells is $2$.

Similarly, for the second query, the answer is $1$.

It will never be possible to color $1000$ cells, so the answer is $-1$.
