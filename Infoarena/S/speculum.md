## Task

Consider the following infinite grid, with rows and columns numbered starting from 1:

$1 \ \ 2 \ \ 3 \ \ 4 \ \ \dots$

---------

$1 \ | \ \ 1 \ \ 1 \ \ 1 \ \ 1 \ \ \dots$

$2 \ | \ \ 2 \ \ 1 \ \ 1 \ \ 2$

$3 \ | \ \ 1 \ \ 2 \ \ 1 \ \ 2 \ \ \dots$

$4 \ | \ \ 2 \ \ 2 \ \ 1 \ \ 1 \ \ \dots$

Constructed as follows:

It starts with the square of side length $1$ that contains the value $1$ at position $(1, 1)$.

At each step, the size of the square is doubled as follows:

1. A square of the same size is added to the right of the current square. This new square has the columns with the same values as the initial square but mirrored relative to the vertical line between these squares. More precisely, if the first square has columns $C_1, C_2, \dots, C_{n-1}, C_n$, the square to its right will have columns $C_n, C_{n-1}, \dots C_2, C_1$.
2. A new square of the same size is added below the initial square, with values obtained by mirroring the rows of the initial square horizontally and swapping the values $1$ with $2$ and vice versa. Specifically, the initial rows $L_1, L_2, \dots, L_{n-1}, L_n$ are written in the order $L_n, L_{n-1}, \dots L_2, L_1$, assigning $2$ in place of each occurrence of $1$ and $1$ in place of $2$.
3. A new square of the same size is added to the bottom-right of the initial square. This new square is obtained by mirroring both the rows (horizontally) and columns (vertically) of the initial square. The values remain unchanged.

For example, in the second step, we have the square

$1 \ \ 1$

$2 \ \ 1$

and according to $1.$ we add to its right the square

$1 \ \ 1$

$1 \ \ 2$

(this is the initial square 'mirrored', with the same columns but in reverse order), and below it, according to $2.$:

$1 \ \ 2$

$2 \ \ 2$

(the initial square mirrored horizontally, and with values $1$ and $2$ swapped), and in the bottom-right, according to $3.$:

$1 \ \ 2$

$1 \ \ 1$

(the initial square mirrored twice, or the square from step $2.$ mirrored a second time horizontally).

To solve the problem, you need to respond to several queries of the form $(x1, y1, x2, y2)$, with the meaning: what is the sum of the numbers in the grid located in the rectangle with top-left corner $(x1, y1)$ and bottom-right corner $(x2, y2)$? The $x$ coordinate numbers the rows, while $y$ numbers the columns.

## Input data

The input file `speculum.in` contains on the first line the number of queries $T$. The following $T$ lines contain $4$ integers each: $x1 \ y1 \ x2 \ y2$.

## Output data

In the output file `speculum.out`, print on each line a single number, the answer to the queries in the order they appear in the input file.

## Constraints

$1 \leq T \leq 20$

$1 \leq x1 \leq x2 \leq 10^9$

$1 \leq y1 \leq y2 \leq 10^9$

## Example

`speculum.in`

```
6
1 1 1 2
1 1 2 1
2 2 4 4
5 6 6 8
12 2 16 4
11512 62723 44722 85311
```

`speculum.out`

```
2
3
13
9
24
1125326168
```

## Explanation

Test 4 asks for the sum of the square defined by the corners $(5, 6)$ and $(6, 8)$. It has the following values:
$1 \ \ 2 \ \ 2$

$1 \ \ 2 \ \ 1$

with a sum of $9$.