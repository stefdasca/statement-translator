```markdown
It is considered $N$ closed intervals, having natural number boundaries between $1$ and $L$. Each natural number $i$ in the interval $[1, L]$ has an associated weight $c_i$.

We call a *cover* a set of natural numbers between $1$ and $L$ with the property that each interval contains at least one element of the set. The cost of a cover is equal to the sum of the weights of the numbers in the cover.

# Task

For a given set of intervals, determine the minimum cost of a cover.

# Input data 

The input file `cover.in` contains on the first line the two natural numbers $N \ L$ separated by a space. On the next line, there are $L$ natural numbers separated by a space $c_1 \ c_2 \dots c_L$, representing the weights of the natural numbers in the interval $[1, L]$. The next $N$ lines each contain two natural numbers $a$, $b \ (1 \leq a \leq b \leq L)$ representing the boundaries of the intervals.

# Output data

The output file `cover.out` will contain a single line that will print a natural number representing the minimum cost of a cover.

# Constraints and clarifications

* $1 \leq N \leq 60\ 000$
* $1 \leq L \leq 1\ 000\ 000$
* $0 \leq c_i \leq 1\ 024$, for any $1 \leq i \leq L$
* For $40\%$ of the tests, $N \leq 1\ 000$ and $L \leq 10\ 000$.

# Example 1

`cover.in`
```
2 5
100 5 9 6 90
1 3
3 5
```

`cover.out`
```
9
```

## Explanation

The cover $\\{3\\}$ is built, which has a cost of $9$. Element $3$ belongs to both intervals given in the input file.
There are other possible covers, for example $\\{2, 4\\}$ but its cost is $11$ which is not minimal.

# Example 2

`cover.in`
```
4 10
1 3 6 4 5 1 0 1 3 2
1 3
3 5
6 9
4 4
```

`cover.out`
```
5
```

## Explanation

The cover $\\{1, 4, 7\\}$ is built, which has a cost of 5.
```
```