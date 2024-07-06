```markdown
Vasilică has $N$ towers with heights $h_1, h_2, \dots, h_N$ at the kindergarten. When he arranges at least two towers in a line so that their heights are in increasing order, Vasilică says that he has built a hill. The height of the hill is equal to the height of the tallest tower used. For example, arranging the towers with heights $2 \\ 4 \\ 4 \\ 7 \\ 9$ forms a hill with a height of $9$.

Vasilică would like to arrange the $N$ towers in a line, forming a sequence of hills so that the sum of the heights of the hills formed is maximized.

# Task

Write a program that, knowing the heights of the $N$ towers, will determine the maximum possible sum of the heights of the hills that can be formed by arranging the $N$ towers in line.

# Input data

The input file `deal.in` contains:
 * The first line contains the natural number $N$.
 * The second line contains $N$ natural numbers separated by spaces, representing the heights of the $N$ towers.

# Output data

The output file `deal.out` will contain a single line which will print a natural number representing the task.

# Constraints and clarifications

* $2 \leq N \leq 100 \ 000$;
* $1 \leq $ Heights of the towers $ \leq 100 \ 000$;
* If after arranging the towers $h_i \leq h_{i+1}$ then the towers $i$ and $i + 1$ are part of the same hill.

# Example

`deal.in`
```
7
10 2 2 2 7 5 2
```

`deal.out`
```
22
```

## Explanation

A possible solution with the sum of heights $22$ would be: $2 \\ 10 \\ 2 \\ 5 \\ 2 \\ 2 \\ 7$. Three hills are formed: $2 \\ 10$ (with height $10$), $2 \\ 5$ (with height $5$), and $2 \\ 2 \\ 7$ with height $7$.
```