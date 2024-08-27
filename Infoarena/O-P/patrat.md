**Square**

Gigel and Alina are playing a riddle game. Gigel is thinking of two natural numbers $x$ and $y$. Alina promises Gigel that she will find those numbers between $x$ and $y$ that can be written as the sum of two perfect squares in at least two different ways. For example, the number $N$ has the mentioned property if it can be written in two different ways as the sum of perfect squares: $N = p_1 + p_2$ and $N = p_3 + p_4$. The four squares ($p_1$, $p_2$, $p_3$, $p_4$) must be non-zero and pairwise distinct.

## Task

Help Alina guess all the numbers between $x$ and $y$ that can be written as the sum of two squares in two different ways.

## Input data

The first line of the input file `patrat.in` contains two natural numbers $x$ and $y$ representing the limits between which Alina must find numbers having the mentioned property.

## Output data

If there are $k$ numbers having the mentioned property between $x$ and $y$, the output file `patrat.out` will contain $k$ lines, each containing a natural number which can be written as the sum of two squares in two different ways. The numbers will be written in ascending order. If there is no number having the required property between $x$ and $y$, the file will contain only the number $0$.

## Constraints and clarifications

$1 \leq x$
$y \leq 20\,000$

## Example

### patrat.in

`40 100`

### patrat.out

`65 85`

### patrat.in

`10 60`

### patrat.out

`0`

## Explanation

In the interval $[40, 100]$ there are two numbers having the required property: $65 = 1 + 64 = 1^2 + 8^2$ and $65 = 16 + 49 = 4^2 + 7^2$
$85 = 4 + 81 = 2^2 + 9^2$ and $85 = 36 + 49 = 6^2 + 7^2$
In the interval $[10, 60]$ there is no number having the required property.