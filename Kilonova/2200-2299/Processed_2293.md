Sure, here's the translated text:

---
Andrei is ready for a new day of high school. Before entering the classes, he realizes that there has been a rearrangement of the classrooms. The new structure of the school, viewed from above, has the shape of a square matrix with $N$ rows and $N$ columns, each small square representing a class. Because the students disagreed with the new classroom arrangement (for well-known reasons), ants will now learn there. Due to the school's imposed regulations, Andrei receives a sheet from the school administration in the form of a matrix in which, for each coordinate $(i, j)$, where $i$ is the row, and $j$ is the column, $M_{ij}$ is written, the number of ants that will learn in the class at the same coordinates.

Since the ants want to learn as much as possible about their new school, and Andrei is forbidden to communicate the allocation in its current form, you will need to help the ants in the new school year!

# Task

The problem consists of $4$ tasks:
1. The ants are impressed by spirals, so they want you to display the number of ants in each class, considering that their traversal will be done **in a spiral**, starting from coordinate $(1, 1)$ with the first direction being to the right. (see example $1$)
2. The ants become obsessed with spirals, so they want you to display the number of ants in each class, with the guarantee that $N=2^k$, where $k$ is a natural number and considering the following traversal: At each step, the matrix will be divided into 4 quadrants. First, the **top-left** quadrant is traversed, then the **top-right**, followed by the **bottom-right**, and finally the **bottom-left**. The traversal of each quadrant will be done similarly to the traversal of the entire matrix, splitting it again into $4$ quadrants, traversed in the same order. The splitting stops when we are left with only one class in the quadrant. (see example $2$)
3. The ants are impressed by prime numbers, so they want you to display the number of classes that have a prime number of ants and their coordinates. (see example $3$)
4. The ants become obsessed with prime numbers, so they want to ask $Q$ questions in the form of: how many classes with prime numbers of ants exist in the **submatrix** that has the **top-left** corner at position $(L_1, C_1)$ and the **bottom-right** corner at position $(L_2, C_2)$. Answer these questions. (see example $4$)

# Input data

The first line of the input file `matrix.in` contains the task number $C \in \{1, 2, 3, 4\}$.
The second line contains the natural number $N$, the size of the matrix.
On the next $N$ lines, there are $N$ natural numbers, representing the number of ants in the classes on the respective row.
Only if $C=4$, the next line contains $Q$, the number of questions, followed by another $Q$ lines each containing $4$ natural numbers, in order: $L_1$, $C_1$, $L_2$, $C_2$.

# Output data

* The output will be written to the file `matrix.out`.
* If $C=1$, then the number of ants in each class will be displayed, in the order of traversal from task 1, with spaces between them.
* If $C=2$, then the number of ants in each class will be displayed, in the order of traversal from task 2, with spaces between them.
* If $C=3$, then the first line will display the number of classes that have a prime number of ants, and on each of the following lines, $2$ numbers will be displayed: the coordinate of the **row** of the class and the coordinate of the **column** of the class, separated by a space, for each class that meets the condition of having a prime number of ants. The classes will be ordered by row, and if there are multiple classes that meet the above condition, by column.
* If $C=4$, then $Q$ lines will be displayed, where on line $q$, $1 \le q \le Q$, the answer to the $q$-th question will be displayed.

# Constraints and clarifications

* $C \in \{1, 2, 3, 4\}$;
* $1 \le N \le 1 \ 000$;
* For $C=2$, $N=2^k$, $k$ natural number;
* $1 \le Q \le 1 \ 000 \ 000$;
* $1 \le i, j \le N$;
* $0 \le M_{ij} \le 1 \ 000 \ 000$;
* $1 \le L_1 \le L_2 \le N$;
* $1 \le C_1 \le C_2 \le N$.

| # | Points | Constraints |
|----|----|----|
| 1 | 25 | $C=1$ |
| 2 | 25 | $C=2$ |
| 3 | 5 | $C=3$, $M_{ij} \le 10$ |
| 4 | 20 | $C=3$ |
| 5 | 15 | $C=4$, $N, Q \le 100$ |
| 6 | 10 | $C=4$ |

# Example 1

`matrix.in`
```
1
4
7 10 98 52
2 36 80 13
61 79 9 0
21 1 43 45
```

`matrix.out`
```
7 10 98 52 13 0 45 43 1 21 61 2 36 80 9 79
```

## Explanation

~[img1.png|align=left|width=25%]

The numbers in the matrix will be displayed in a spiral, in the order of the arrows in the figure above.

# Example 2

`matrix.in`
```
2
4
7 10 98 52
2 36 80 13
61 79 9 0
21 1 43 45
```

`matrix.out`
```
7 10 36 2 98 52 13 80 9 0 45 43 61 79 1 21
```

## Explanation

The initial matrix is divided into $4$ quadrants: $\\begin{pmatrix}
7 & 10\\\\
2 & 36
\\end{pmatrix},
\\begin{pmatrix}
98 & 52\\\\
80 & 13
\\end{pmatrix},
\\begin{pmatrix}
9 & 0\\\\
43 & 45
\\end{pmatrix},
\\begin{pmatrix}
61 & 79\\\\
21 & 1
\\end{pmatrix}
$, which are then divided again into $4$ quadrants, in the order of traversal from task 2, resulting in the given response.

# Example 3

`matrix.in`
```
3
4
7 10 98 52
2 36 80 13
61 79 9 0
21 1 43 45
```

`matrix.out`
```
6
1 1
2 1
2 4
3 1
3 2
4 3
```

## Explanation

In the matrix there are $6$ prime numbers: $7, 2, 13, 61, 79, 43$, ordered by row and then by column.

# Example 4

`matrix.in`
```
4
4
7 10 98 52
2 36 80 13
61 79 9 0
21 1 43 45
5
1 1 2 3
3 2 3 2
1 4 4 4
1 2 2 3
3 1 4 3
```

`matrix.out`
```
2
1
1
0
3
```

## Explanation

* For the first question, the analyzed submatrix is $\\begin{pmatrix}7 & 10 & 98\\\\2 & 36 & 80\\end{pmatrix}$, which has $2$ prime numbers: $7, 2$.
* For the second question, the analyzed submatrix is a single element, specifically $79$, which is prime.
* For the third question, the analyzed submatrix is $\\begin{pmatrix}52\\\\13\\\\0\\\\45\\end{pmatrix}$, which has one prime number: $13$.
* For the fourth question, the analyzed submatrix is $\\begin{pmatrix}10 & 98\\\\36 & 80\\end{pmatrix}$, which has no prime numbers.
* For the fifth question, the analyzed submatrix is $\\begin{pmatrix}61 & 79 & 9\\\\21 & 1 & 43\\end{pmatrix}$, which has $3$ prime numbers: $61, 79, 43$.

---