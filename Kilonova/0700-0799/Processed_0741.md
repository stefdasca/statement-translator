An image will be represented as a rectangular array of real numbers, with each number representing a grayscale value of the image. The values range between $0$ (representing a completely white region) and $1$ (completely black region), with two decimal places.
The center of gravity of the image is an element of the array. Suppose it is on row $i$ and column $j$. Then the absolute difference between the sum of elements above row $i$ and the sum of elements below row $i$ is minimal. Similarly, for this minimum difference, the absolute difference between the sum of elements to the left of column $j$ and the sum of elements to the right of column $j$ should also be minimal.
Let us consider the following array as an example, which may result from scanning the lowercase letter 'o'. The center of gravity is on row $3$ and column $3$ because the difference in the sums of elements from each zone formed by ignoring the third row is $0.1$ (sums are $5.55$ and $5.65$) and similarly, the difference in the sums of elements from each zone formed by ignoring the third column is $0.1$ (sums are $5.60$ and $5.70$).

~[ocr.png|width=30em]

# Task

Write a program that determines the center of gravity of a scanned image.

# Input data

The input text file `ocr.in` contains the representation of an image. The first line of the input file contains two natural numbers $n$ and $m$ separated by a space, representing the number of rows and the number of columns of the array, respectively. The next $n$ lines contain $m$ real numbers each, within the interval [$0, 1$] separated by spaces, representing the scanned image.

# Output data

The output text file `ocr.out` will contain a single line with two natural numbers $l$ and $c$, separated by a space, representing the coordinates (row, column) of the center of gravity. If multiple centers of gravity are determined, the coordinates of the one with the maximum row index will be printed; if there are multiple centers of gravity on the same row, the one with the maximum column index will be printed.

# Constraints and clarifications

* $1 \leq n, m \leq 50$;
* Real values are expressed with up to two decimal places.
* Rows are numbered from $1$ to $n$ (top to bottom), and columns from $1$ to $m$ (left to right).

# Example 1

`ocr.in`
```
5 5
0.1 0.2 0.1 0.2 0.1
0.1 0.2 0.3 0.1 0.1
0.2 0.3 0.1 0.1 0.3
0.4 0.1 0.1 0.1 0.2
0.2 0.2 0.3 0.3 0.1
```

`ocr.out`
```
3 3
```

# Example 2

`ocr.in`
```
5 10
0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1
0.2 0.2 0.2 0.2 0.2 0.2 0.2 0.2 0.2 0.2
0.3 0.3 0.3 0.3 0.3 0.3 0.3 0.3 0.3 0.3
0.4 0.4 0.4 0.4 0.4 0.4 0.4 0.4 0.4 0.4
0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.6
```

`ocr.out`
```
4 6
```

