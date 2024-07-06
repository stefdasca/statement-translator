```markdown
The national team's footballers train on a rectangular-shaped field. On this field, $L$ horizontal lines and $C$ vertical lines were drawn so that the distance between any two lines is equal to $1$ meter. The lines were numbered from top to bottom with values from $1$ to $L$, and the columns were numbered from left to right with values from $1$ to $C$, and the entire field is made up of square cells with side $1$. The intersection between a line and a column is called a point. A point is specified by the line and column at whose intersection it is located.

Footballers can pass only from one point to another point. A pass can go through **one or more points**. A point through which a pass goes is called a **passable point**.

The football team's coach wants to create an application that analyzes players' passes from a match to improve the quality of passes given by the footballers from one match to another.

# Task

Knowing $P$ passes, each specified by the starting point and the ending point, determine the **square** areas on the field, of maximum and non-zero area, which do not contain any passable points either inside or on the edges.

Example: $L = 8$, $C = 10$, $P = 6$ and the passes:

$(2, 2) \rightarrow (2, 9)$; $(2, 2) \rightarrow (4, 8)$; $(5, 3) \rightarrow (8, 7)$; $(1, 8) \rightarrow (4, 8)$; $(5, 2) \rightarrow (3, 9)$; $(7, 9) \rightarrow (5, 10)$ then there is a single square area of maximum area = $9$, which does not contain any passable point, colored in the figure.

~[pic.png]

# Input data

The input file `pase.in` contains:
* The first line contains the natural numbers $L$ and $C$, with the meaning from the statement;
* The second line contains the natural number $P$, representing the number of passes;
* On the next $P$ lines are described the $P$ passes, one pass per line, each pass being described by four natural numbers $a \ b \ c \ d$, where $a \ b$ represent the line and column of the starting point, respectively, and $c \ d$ represent the line and column of the ending point $(1 \leq a, c \leq L, 1 \leq b, d \leq C)$.

The numbers on the same line of the file are separated by a space.

# Output data

The output file `pase.out` will contain, on the first line, the number $Z$ of determined maximum square area zones and on the second line the area $A$ of such a zone. In the next $Z$ lines, the determined zones, one zone per line; a zone will be specified by $4$ natural numbers separated by space, representing the coordinates of the point (line, column) from the top-left corner of the zone and the coordinates of the point (line, column) from the bottom-right corner of the zone. The rendering will be done in ascending order of the lines of the top-left corner of the square area, and for two equal lines, in ascending order of the column.

# Constraints and clarifications

* $1 \leq L, C \leq 1 \ 000$
* $1 \leq P \leq 1 \ 000$
* Passes can be sent from one point to the same point (with a lot of effect!)
* It is guaranteed that for the test data there is a solution of non-zero area.

|#|Score|Constraints|
|-|-|-|
|1|12|The input file contains only horizontal passes.|
|2|8|The input file contains only vertical passes.|
|3|4|The input file contains only passes where the starting point and the ending point coincide.|
|4|16|$1 \leq L, C \leq 100$; the input file also contains oblique passes|
|5|60| No additional constraints|

# Example

`pase.in`
```
8 10
6
2 2 2 9
2 2 4 8
5 3 8 7
1 8 4 8
5 2 3 9
7 9 5 10
```

`pase.out`
```
1
9
4 4 7 7
```

## Explanation

The data in the input file corresponds to the previous image.

There is a single square area of maximum area equal to $9$, having the top-left corner $(4, 4)$ and the bottom-right corner $(7, 7)$
```