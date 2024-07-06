```markdown
Consider the matrix $A$ with $n$ rows and $n$ columns. A formation is composed of a subarray of a row $l$ and a subarray of a column $c$ of the matrix. The formation is determined by three aspects:
* Two indices $i_1$ and $i_2$, $1 \leq i_1 \leq i_2 \leq n$, which represent the starting and ending indices of the subarray on column $c$.
* Two indices $j_1$ and $j_2$, $1 \leq j_1 \leq j_2 \leq n$, which represent the starting and ending indices of the subarray on row $l$.
* The row $l$ and column $c$ intersect at an element $A[l][c]$, $i_1 \leq l \leq i_2, j_1 \leq c \leq j_2$, called the nucleus, which must have the minimum value among all the elements in the formation.

The power of a formation is calculated as the product of the value of the nucleus and the sum of the elements in the formation.

# Task
1) Determine the total number of formations in the matrix $MOD \ 10^{9} + 7$.
2) Determine the sum of all the powers of the formations in the matrix $MOD \ 10^{9} + 7$.

# Input data
The input file `formatie.in` will contain on the first line a natural number $C$, with values $1$ or $2$, representing the number of the task.
The second line will contain a natural number $n$, representing the number of rows and columns.
The following $n$ lines will each contain $n$ numbers, representing the elements of the matrix.

# Output data
The output file `formatie.out` will contain on the first line a single integer $s$, representing the required result.

# Observations
* A formation can be composed of a single element.
* If $i_1 = i_2$ or $j_1 = j_2$, each occurrence of a nucleus will determine a new formation.
* There is no formation in which the intersection between row and column is empty.

# Constraints and clarifications

* $1 \leq n \leq 500$
* $1 \leq A[i][j] \leq 1 \ 000$, $\forall i, j, 1 \leq i \leq n, 1 \leq j \leq n$

# Scoring

|No. |Points|Task|Additional Constraints|
|-|-|-|-|
|1|5|$C=1$|$n \leq 8$|
|2|10|$C=1$|$n \leq 80$|
|3|15|$C=1$|No additional constraints|
|4|5|$C=2$|$n \leq 8$|
|5|25|$C=2$|$n \leq 80$|
|6|40|$C=2$|No additional constraints|

# Example 1

`formatie.in`
```
1
3
9 8 4
3 3 4
1 9 5
```

`formatie.out`
```
50
```

# Example 2

`formatie.in`
```
2
3
9 8 4
3 3 4
1 9 5
```

`formatie.out`
```
2231
```

## Explanations

~[img1.jpg]

In the drawing above, all the formations that can be formed are highlighted. In total, there are $50$ formations.
**For the second example:**
The power of the first formation is $9 \cdot 9 = 81$.
The power of the second formation is $8 \cdot 8 = 64$.
The power of the third formation is $8 \cdot (8 + 9) = 8 \cdot 17 = 136$.
The power of the fourth formation is $4 \cdot 4 = 16$.
.
.
.
The power of the 35th formation is $3 \cdot (3 + 3 + 4 + 9 + 8) = 81$.
. . .
The power of the 50th formation is $5 \cdot (9 + 5) = 70$.
In total, the sum of all powers is equal to $2231$.

|Formation|Explanation|
|-|-|
|~[img2.jpg]|The formation is delimited in the green contour, and has $l = 2$, $c = 2$, $i_1 = 1$, $i_2 = 3$, $j_1 = 1$, $j_2 = 3$. The nucleus is at position $l = 2$, $c = 2$, and has the value $A[l][c] = 3$, being the smallest among all elements of the formation. The power of this formation is $3 \cdot (8 + 3 + 9 + 3 + 4) = 3 \cdot 27 = 81$|
|~[img3.jpg]|The formation is delimited in the blue contour, and has $l = 1$, $c = 3$, $i_1 = 1$, $i_2 = 3$, $j_1 = 1$, $j_2 = 3$. The nucleus is at position $l = 1$, $c = 3$, and has the value $A[l][c] = 4$, being the smallest among all elements of the formation. The power of this formation is $4 \cdot (9 + 8 + 4 + 4 + 5) = 4 \cdot 30 = 120$|
|~[img4.jpg]|The formation is delimited in the yellow contour, and has $l = 3$, $c = 1$, $i_1 = 1$, $i_2 = 3$, $j_1 = 1$, $j_2 = 2$. The nucleus is at position $l = 3$, $c = 1$, and has the value $A[l][c] = 1$, being the smallest among all elements of the formation. The power of this formation is $1 \cdot (9 + 3 + 1 + 9) = 1 \cdot 22 = 22$|
|~[img5.jpg]|The formation is delimited in the blue contour, and has $l = 1$, $c = 3$, $i_1 = 1$, $i_2 = 2$, $j_1 = 3$, $j_2 = 3$. The nucleus is at position $l = 1$, $c = 3$, and has the value $A[l][c] = 4$, being the smallest among all elements of the formation. The power of this formation is $4 \cdot (4 + 4) = 4 \cdot 16 = 64$|
|~[img6.jpg]|The formation is delimited in the purple contour, and has $l = 2$, $c = 3$, $i_1 = 1$, $i_2 = 2$, $j_1 = 3$, $j_2 = 3$. The nucleus is at position $l = 2$, $c = 3$, and has the value $A[l][c] = 4$, being the smallest among all elements of the formation. The power of this formation is $4 \cdot (4 + 4) = 4 \cdot 16 = 64$. **The formation has exactly the same elements as the previously exemplified formation, but has the nucleus located in a different position!**|
```
