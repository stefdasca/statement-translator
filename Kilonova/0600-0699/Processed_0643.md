~[0.png|align=right|width=13em]
Although he usually doesn't draw, Adrian has a unique passion: he likes to sketch imaginary cities on paper... specifically, how they would look from above. This year, on his birthday, he received a parchment as a gift! Naturally, he decided to use it to draw the sketch of the largest city he has imagined so far.

The parchment is as wide as a sheet of paper, but its length is unexpectedly large. Furthermore, the parchment is divided into squares so that along its length, there are exactly $N$ squares, and along its width, there are exactly $K$ squares. Thus, Adrian has exactly $N \cdot K$ squares at his disposal to color.
\
He decides to color only the city streets because he doesn't have time for more and plans to use two types of streets:
1) Horizontal streets
  - They will be drawn as a continuous sequence of blue squares.
  - On each row from $1$ to $N$, there will be **exactly** one horizontal street. So, in the end, there will be **exactly** $N$ horizontal streets.
  - Each street will span a single row.
  - The length of each street will be at least one square and at most $K$ squares and is equal to the number of squares that make it up.
  - The street can start on any square on the row and can have any length as long as it does not exceed the limits of the parchment.
2) Vertical streets
  - They will be drawn as a continuous sequence of red squares.
  - Adrian will draw exactly $Q$ vertical streets, spreading across any of the columns from $1$ to $K$.
  - There can be multiple vertical streets on a column, provided they do not overlap. It is not mandatory to have vertical streets on all columns.
  - The length of each street will be at least one square and at most $N$ squares and is equal to the number of squares that make it up.
  - The street can start on any square on the column and can have any length as long as it does not exceed the limits of the parchment.

\
In the end, Adrian notices that certain squares have turned purple because they are part of both a vertical street and a horizontal street, so they were colored both red and blue. Adrian is fascinated by their appearance and wants to know how many purple squares are in his drawing. Being too tired to count them, he asks you to help him.

# Task
Knowing the numbers $N$, $K$, $Q$, as well as the positioning of the $N$ horizontal streets and the $Q$ vertical streets, determine the number of purple squares on the parchment.

# Input data
The input file `pergament.in` contains on the first line three natural numbers separated by a space, $N$, $K$, $Q$, with the significance mentioned in the statement.

The second line contains four natural numbers separated by a space, $A$, $B$, $C$, $D$.

The third line contains two natural numbers $X_1$ and $Y_1$, where $X_1$ represents the column of the starting square of the horizontal street on row 1, and $Y_1$ represents its length.

The data of the next $N-1$ streets will be calculated using the formulas below, where $X_i$ represents the column of the starting square of the horizontal street on row $i$ ($2 \leq i \leq N$), and $Y_i$ represents its length:
- $X_i = 1 + (X_{i-1} \cdot A + B)\ \% K$
- $Y_i = 1 + (Y_{i-1} \cdot C + D)\ \% (K - X_i + 1)$

The next $Q$ lines contain three natural numbers $J$, $R$, and $L$, where $J$ represents the column where the vertical street is located, $R$ represents the row where the starting square of the street is located, and $L$ represents the length of the street.

# Output data
The output file `pergament.out` will contain a single natural number representing the number of purple squares in Adrian's drawing.

# Constraints and clarifications
- $1 \leq N \leq 10\ 000\ 000$
- $1 \leq K \leq 50$
- $1 \leq Q \leq 100\ 000$
- $1 \leq A,B,C,D \leq 10\ 000\ 000$
- $1 \leq X_i \leq K$
- $1 \leq Y_i \leq K-X_i+1$
- $1 \leq J \leq K$
- $1 \leq R \leq N$
- $1 \leq L \leq N-R+1$
- Rows are numbered from $1$ to $N$, and columns are numbered from $1$ to $K$.
- For 40 points, $N \leq 20\ 000$.
- For another 30 points, $N \leq 500\ 000$.
- For another 30 points, there are no additional conditions.

# Example
`pergament.in`
```
6 3 2
1 1 1 1
1 2
2 2 4
1 4 3
```
`pergament.out`
```
3
```
~[1.png|align=right|width=15em]
The adjacent image represents the parchment drawn by Adrian from the example.
According to the formulas, we will have the following horizontal streets:
- Line 1: $X_1 = 1$ and $Y_1 = 2$
- Line 2: $X_2 = 3$ and $Y_2 = 1$
- Line 3: $X_3 = 2$ and $Y_3 = 1$
- Line 4: $X_4 = 1$ and $Y_4 = 3$
- Line 5: $X_5 = 3$ and $Y_5 = 1$
- Line 6: $X_6 = 2$ and $Y_6 = 1$

It can be seen that there are exactly 3 purple squares.