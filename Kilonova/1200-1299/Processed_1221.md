# Robinson has a Square Field

Robinson has a square-shaped field, like a two-dimensional board, with a side of $m$ units (with $m^2$ plots). A plot is an elementary square of the board. The rows and columns are numbered from $1$ to $m$: rows from top to bottom, and columns from left to right. He planted wheat and prayed for a bountiful harvest. His prayer was answered, and the wheat sprouted as follows: in the plots in the first row, the harvests were from left to right: $n$, $n+1$, $n+2$, $\dots$ grains of wheat, and in the plots on the first column, the harvests were from top to bottom: $n$, $n+1$, $n+2$, $\dots$ grains of wheat.

Then, if we traverse the other plots row by row starting from the second row, and within a row, starting from the second column, the harvest in row $i$ and column $j$ was equal to the sum of the harvests at positions ($i-1,j$) and ($i,j-1$). If these sums exceed $999$, then they will be replaced by the numbers formed from the last $3$ digits of the respective sum (for example, if $sum=1234$, the number $234$ will be retained).

With the fulfillment of his prayer, Robinson had a dream in which, to have luck the next year, he was asked to gather the wheat on the first day as follows: he starts from a given position (row $l$ and column $c$), from where he will gather all the grains on that position. Then he will calculate the remainder of the number of grains at that position divided by $4$. The next position for gathering will be the neighboring one to the North if the remainder is $0$, the neighboring one to the East if the remainder is $1$, the neighboring one to the South if the remainder is $2$, or the neighboring one to the West if the remainder is $3$.

This path he dreamed of will stop either when the next position is out of the field, or when the next position is one from which the harvest has already been gathered.

# Task

Write a program that reads the numbers $m$, $n$, $l$, and $c$ and determines:
* the harvests from each plot;
* the sequence of visited plots, in the order in which the wheat was gathered on the dreamed path;

# Input data

The first line of the input file `robinson.in` contains the numbers $m \ n \ l \ c$ in this order, separated by a space; $l$ and $c$ indicate a correct position on the board.

# Output data

The first line of the output file `robinson.out` will print the value $a_{mm}$. The following lines will contain two natural numbers separated by a space indicating the coordinates of each plot on the traversed path: the first number indicates the row and the second number indicates the column of the visited plot.

# Constraints and clarifications

* $m$, $n$, $l$, $c$ are natural numbers,
* $1 \leq m \leq 20$
* $1 \leq n \leq 100$;
* For the correct determination of the value $a_{mm}$, $30\%$ of the score is awarded.
* For the correct indication of the traversed path, an additional $70\%$ of the score is awarded.

# Example 1

`robinson.in`
```
4 55 1 3
```

`robinson.out`
```
130
1 3
1 4
2 4
2 3
```

## Explanation

$m=4$, meaning the square board has a side of $4$ units. $n=55$, so the first row is: $55$, $56$, $57$, and $58$. Similarly, the first column: $55$, $56$, $57$, $58$, from top to bottom. Then the second row is completed as follows: $a_{22} = a_{12}+a_{21}=56+56=112$, then $a_{23} = a_{13}+a_{22}=57+112=169$; then $a_{24}=a_{14}+a_{23}$ etc. The third row, will be completed as follows: $a_{32}=a_{22}+a_{31}$; then $a_{33}=a_{23}+ a_{32}$, then $a_{34}=a_{24}+ a_{33}$ etc.

Attention: $a_{44}=a_{34}+a_{43}=565+565=1130$ and $a_{44}=130$, meaning the number formed from the last $3$ digits of $1130$.

b) Starting position: $a_{13}=57$, with remainder $1$, so the direction is East. Here we have $a_{14}=58$, which has remainder $2$, so the direction is South. Here is $a_{24}=227$, with remainder $3$, so the direction is West, where we have $a_{23}=169$. This has remainder $1$ and the direction is East, so it should return to the position ($2,4$) which has already been visited. The positions ($1,3$), ($1,4$), ($2,4$), and ($2,3$) were displayed.

If instead of $l=1$ and $c=3$, we had $l=3$ and $c=4$, then $a_{34} = 565$, with remainder $1$, so the direction is East and it should go out of the field. This path would have one step.
