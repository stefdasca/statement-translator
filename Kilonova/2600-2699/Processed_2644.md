The text has been translated as per your instructions:

---

Robot Vasile dreams of becoming a visual artist. He creates 3D paintings on a medium that he prints out. A 3D painting has a rectangular shape and can be divided into "3D pixels," arranged in $n$ rows and $m$ columns, each 3D pixel having a certain height. Initially, the painting is white.

A 3D pixel is considered a "peak" if it has a height strictly greater than the heights of all its neighbors. Two 3D pixels are considered neighbors if they are on the same row, in consecutive columns, or if they are in the same column, in consecutive rows.

Robot Vasile paints algorithmically, as follows: he traverses the pixels in the order of rows and, within each row, in the order of columns, and if the current pixel is a peak, he "pours" a new color over it (a color different from white and from all colors used so far). We will call pure colors the colors that robot Vasile pours over the peak pixels. The pure color will "drip" and paint all neighboring 3D pixels that have a height strictly smaller than the painted peak, then will continue to drip to the neighbors' neighbors with strictly smaller heights, and so on, until the dripping is no longer possible. When the pure color reaches a white pixel, it will be colored in that color. However, if the pure color reaches a pixel that has been previously colored, the colors will mix, creating a new color. The colors formed by mixing will be different from all the pure colors robot Vasile pours over the peak pixels.

Although he dreams of being an artist, robot Vasile lacks aesthetic sense, so he has established three criteria for evaluating the artistic quality of a painting: the maximum number of pure colors that mix on a single 3D pixel, the number of distinct colors that appear in the painting (either pure or obtained through mixing), and the maximum size of an area painted in the same color, different from white. An area is formed from 3D pixels with the property that, for any two pixels $p_1$ and $p_2$ in that area, there is a sequence of 3D pixels starting with $p_1$, ending with $p_2$, and any two consecutive pixels are neighbors. The size of an area is equal to the number of 3D pixels in that area.

# Task

Write a program that, given $n$ and $m$ (the dimensions of the painting), and the heights of the 3D pixels, solves the following three requirements:
1. Determines the maximum number of pure colors that mix on a single 3D pixel;
2. Determines the number of distinct colors that appear in the painting created according to robot Vasile's algorithm;
3. Determines the maximum size of an area formed from 3D pixels of the same color, different from white.

# Input data

The input file `pictura.in` contains on the first line three natural numbers $C$ $n$ $m$, representing the requirement that needs to be solved ($1$, $2$ or $3$), the number of rows, and the number of columns of the painting. Each of the following $n$ lines contains $m$ natural numbers representing the heights of the 3D pixels that make up the surface on which robot Vasile paints (following the order of rows and columns). The values written on the same line are separated by a space.

# Output data

The output file `pictura.out` will contain a single line with the answer to requirement $C$ from the input file.

# Constraints and clarifications

* $3 \leq n,m \leq 300$
* The heights of the 3D pixels are natural numbers $\leq 30\ 000$.
* For all test data, it is guaranteed that the number of pure colors that mix on the same 3D pixel is $< 200$.

|#|Points|Constraints|
|-|-|--------|
|1|30|$C = 1$|
|2|50|$C = 2$|
|3|20|$C = 3$|

# Example 1

`pictura.in`
```
1 5 3
8 7 8
8 20 18
11 5 30
19 4 50
2 3 40
```

`pictura.out`
```
3
```

# Example 2

`pictura.in`
```
2 5 3
8 7 8
8 20 18
11 5 30
19 4 50
2 3 40
```

`pictura.out`
```
7
```

# Example 3

`pictura.in`
```
3 5 3
8 7 8
8 20 18
11 5 30
19 4 50
2 3 40
```

`pictura.out`
```
4
```

## Explanations

The heights of the 3D pixels are illustrated in figure $1$, with the peaks being marked in bold (their heights are $20, 19, 50$). All pixels are initially white, marked with $0$.

We will successively color the $3$ peaks. Coloring the peak with height $20$ in color $1$ yields the image in figure $2$. Coloring the peak with height $19$ in color $2$ yields the image in figure $3$, where we noted with $(1, 2)$ the combination of colors $1$ and $2$. Coloring the peak with height $50$ in color $3$ yields the image in figure $3$, where we noted with $(1, 3)$ the combination of colors $1$ and $3$, and with $(1, 2, 3)$ the combination of colors $1, 2$, and $3$.

~[pictura.png]

There are $7$ distinct colors visible: $0, 1, 2, 3, (1, 2), (1, 3)$, and $(1, 2, 3)$. The maximum number of pure colors that mix on a single 3D pixel is $3$. The maximum size of an area formed from pixels of the same color is $4$ - the area colored in $(1, 2, 3)$.

