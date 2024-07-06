```markdown
A matrix with $N$ rows and $N$ columns containing natural numbers from $1$ to $N^2$ is considered, arranged consecutively, first in rows and then in columns, starting with $1$ in the top left corner, as shown in the adjacent example $(N = 4)$.

~[image.png|align=left]

If the elements of the matrix are unrolled, similar to a skein, by rotating the matrix around the center (intersection of the diagonals), pulling from one of its corners horizontally or vertically, towards the outside, a sequence with numbers from $1$ to $N^2$ is obtained in a certain order.
Examples: if $N = 4$ and pulling from:

* the top left corner – horizontally, the sequence: $1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10$ is obtained
* the bottom right corner – vertically, the sequence: $16, 12, 8, 4, 3, 2, 1, 5, 9, 13, 14, 15, 11, 7, 6, 10$ is obtained

# Task

Write a program that reads:

* a natural number $N$, representing the number of rows and columns of a matrix containing natural numbers from $1$ to $N^2$;
* two natural numbers $X$ and $Y$, representing the coordinates of the corner from which the unrolling is done:
$\{ (1,1)$ – top left; $(1,N)$ – top right; $(N,N)$ – bottom right; $(N,1)$ – bottom left;$\}$
* an uppercase character $D$, representing the direction of pulling (`H` – horizontal and `V` – vertical).

and displays the sequence of numbers resulting from the unrolling of the matrix, starting from the corner from which the pulling is done and in the direction of pulling.

# Input data

The input file `ghem.in` contains on the first line the natural number $N$, the second line contains two natural numbers $X$ and $Y$ separated by a space, and on the third line the character $D$, having the meaning described above.

# Output data

The output file `ghem.out` will contain on the first line the sequence of numbers obtained by unrolling the matrix. There will be a single space between any two successive numbers.

# Constraints and clarifications

* $2 \leq N \leq 500$
* $(X,Y) \in \{(1,1), (1,N), (N,N), (N,1)\}$
* $D$ belongs to the set \{`H`,`V`\} – uppercase

# Example 1

`ghem.in`
```
4
1 1
H
```

`ghem.out`
```
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
```

## Explanation

The adjacent matrix is unrolled by "pulling" from the top left corner in a horizontal direction, resulting in the sequence: $1, 2, 3, 4, 8, 12, 16$, $15, 14, 13, 9, 5, 6, 7, 11, 10$

~[image2.png|align=left]

# Example 2

`ghem.in`
```
4
4 4
V
```

`ghem.out`
```
16 12 8 4 3 2 1 5 9 13 14 15 11 7 6 10
```

## Explanation

The adjacent matrix is unrolled by "pulling" from the bottom right corner in a vertical direction, resulting in the sequence: $16, 12, 8, 4, 3, 2$, $1, 5, 9, 13, 14, 15, 11, 7, 6, 10$

~[image3.png|align=left]

# Example 3

`ghem.in`
```
3
1 3
V
```

`ghem.out`
```
3 6 9 8 7 4 1 2 5
```

## Explanation

The adjacent matrix is unrolled by "pulling" from the top right corner in a vertical direction, resulting in the sequence: $3, 6, 9, 8, 7, 4, 1, 2, 5$

~[image4.png|align=left]

# Example 4

`ghem.in`
```
3
3 1
H
```

`ghem.out`
```
7 8 9 6 3 2 1 4 5
```

## Explanation

The adjacent matrix is unrolled by "pulling" from the bottom left corner in a horizontal direction, resulting in the sequence: $7, 8, 9, 6, 3, 2, 1, 4, 5$

~[image5.png|align=left]
```