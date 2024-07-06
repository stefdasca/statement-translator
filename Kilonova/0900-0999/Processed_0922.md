Researchers have discovered that the activity of centipedes is stimulated by the color yellow, and therefore an ant is subjected to an experiment. On the edge of the table where the experiment is conducted, $N$ rectangular sheets of yellow color are stuck side by side, numbered in order from left to right, from $1$ to $N$. The ant is on the table, in front of the first sheet, and follows a path moving only on the free sides of the sheets (which are not stuck to other sheets or to the table), vertically or horizontally, (as indicated by the arrows in the image below), returning to the table. Knowing that in an upward movement the ant covers one centimeter in $5$ seconds, in a downward movement covers one centimeter in $2$ seconds, and if it moves horizontally covers one centimeter in $3$ seconds, help the researchers to obtain some data.

~[furnica.png|width=35em]

# Task

Write a program that solves the following tasks:

1. Determine the time (expressed in seconds) necessary for the ant to cover the entire mentioned path;
2. Determine the maximum length (expressed in centimeters) of a portion of the path in which the ant does NOT descend at all;
3. Determine the sheet number on which the ant is located after $T$ seconds.

# Input data

The input file `furnica.in` contains:

* The first line contains a natural number $C$ which represents the task number and can have the values $1$, $2$ or $3$.
* The second line contains a natural number $N$ which represents the number of yellow sheets if the task is $1$ or $2$, or two natural numbers $N$ and $T$ if the task is $3$.
* On the next $N$ lines, two natural numbers representing the sides of the sheets (expressed in centimeters), in the order of their numbering. The first number represents the horizontal side dimension, and the second number represents the vertical side dimension of the yellow sheet.
* The numbers on the same line of the file are separated by a space.

# Output data

The output file `furnica.out` will contain a single line on which a natural number representing the result determined for the task $C$ will be written.

# Constraints and clarifications

* $1 \leq N,T \leq 10\ 000$; the sides of the sheets are non-zero natural numbers with at most nine digits each;
* If the ant reaches a point at the junction of two sheets, it is considered to be on the left sheet;
* For any $T$, the ant will be on one of the sheets;
* For each task, $30$ points are awarded.

# Example 1

`furnica.in`
```
1
5
3 9
5 9
2 6
2 13
1 4
```

`furnica.out`
```
151
```

## Explanation

In the first example, the task is $1$. There are $5$ yellow sheets and the path taken by the ant is as modeled in the image above. The path has a length of $45$ centimeters and the ant will finish it in $151$ seconds.

# Example 2

`furnica.in`
```
2
5
3 9
5 9
2 6
2 13
1 4
```

`furnica.out`
```
17
```

## Explanation

In the second example, the task is $2$. The longest portion of the path in which the ant does not descend has $9+3+5=17$ cm.

# Example 3

`furnica.in`
```
3
5 100
3 9
5 9
2 6
2 13
1 4
```

`furnica.out`
```
4
```

## Explanation

In the third example, the task is $3$. After $100$ seconds, the ant will be on sheet $4$.