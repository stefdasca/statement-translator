Here is the translated text:

---
Costel is passionate about the oriental art of crafting paper objects, origami, but he is just beginning and needs to become familiar with the correct folding operations of the paper. He has a square sheet of paper torn from a math notebook, having the size of exactly \(N \cdot N\) squares. The folds must be made exactly on a horizontal or vertical line.

Two types of folds are allowed:

* Type $1$ fold, vertical fold executed at $X$ squares from the left edge of the sheet: the left part of the sheet folds towards the right along the vertical line located at a distance of $X$ squares from the left edge.
* Type $2$ fold, horizontal fold executed at $X$ squares from the top edge of the sheet: the top part of the sheet folds down along the line located at a distance of $X$ squares from the top edge of the paper.

After performing a succession of folds, the initial sheet of paper will become an object, which will have a rectangular shape, with a height $H$, width $M$, and a thickness equal to the maximum number of overlapping sheets in the obtained object.

# Task

Given a succession of folds applied to a sheet of size \(N \cdot N\), write a program that determines the height, width, and thickness of the resulting object.

# Input data

The input file `origami.in` has the following structure:

* The first line of the file contains a natural number $N$, representing the initial size of the paper.
* The second line contains a natural number $K$, representing the number of folds.
* The next $K$ lines contain pairs of non-zero natural numbers, $A B$, separated by a space, representing the type of fold ($A$ is $1$ for a vertical fold, or $A$ is $2$ for a horizontal fold), and at what distance the fold is made.

# Output data

The output file `origami.out` will contain, on a single line, three non-zero natural numbers $H, L, G$, separated by a space, representing the height, width, and respective thickness of the resulting object.

# Constraints and clarifications

* $2 \leq N \leq 170$
* $1 \leq K \leq 2N - 2$
* $A = 1$ or $A = 2$
* $1 \leq B <$ the height or width of the paper at that moment (depending on the type of fold)

# Example

`origami.in`
```
4
3
1 3
2 3
1 1
```

`origami.out`
```
3 2 6
```

# Explanation

The paper has $4$ units of height and $4$ units of width. The first fold is made from left to right, along the third vertical line from the left edge of the sheet. A sheet with a height of $4$, width of $3$, and thickness of $2$ is obtained. The second fold is made by folding the upper part of the sheet down, along the third horizontal line from the top edge of the sheet. An object with a height of $3$, width of $3$, and thickness of $4$ is obtained. After the third fold, the final object is obtained, having a height of $3$, width of $2$, and thickness of $6$.