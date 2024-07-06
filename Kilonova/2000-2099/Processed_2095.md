# Task

The Great Romanian Wall is composed of $n$ rows of bricks, numbered **from bottom to top** from $1$ to $n$, and each row contains $m$ bricks, numbered from left to right from $1$ to $m$.

We consider the brick $(x,y)$ to be the $x$-th brick on the $y$-th row.

On this wall, a weed grows as follows:

1. Initially, only the brick $(1,1)$ is covered by the weed.
2. Each day, the weed will choose a covered brick $(x,y)$ and will try to spread to an uncovered brick among the bricks $(x-1,y)$, $(x+1,y)$, and $(x,y+1)$. 
3. If the weed spreads from one brick $(x_1,y_1)$ to another brick $(x_2,y_2)$, a branch will form between these two bricks.

An example of weed growth for $n=m=4$:
~[buruiana2.png|width=20%]

In how many ways can the weed grow such that it covers the entire wall? Two growth modes are considered different if there is a branch in the first mode that does not exist in the second, or vice-versa.

Since the answer can be very large, display the remainder when divided by $10^9+7$.

# Input data

The input file `buruiana.in` will contain on the first line two numbers $n$ and $m$ - the dimensions of the wall.

# Output data

The output file `buruiana.out` will contain the number of ways (modulo $10^9+7$) in which the weed can grow such that it covers the entire wall.

# Constraints and clarifications

- $2 \le n,m \le 10^{18}$;
- For $9$ points, $n,m \le 4$;
- For another $16$ points, $n=2$ and $m \le 20$;
- For another $18$ points, $n=2$ and $m \le 5\ 000$;
- For another $12$ points, $n=2$ and $m \le 10^6$;
- For another $10$ points, $m \le 10^6$;
- For another $20$ points, $m \le 10^9$;
- For the remaining $15$ points, no additional constraints are imposed.

# Example 1

`buruiana.in`
```
2 3
```

`buruiana.out`
```
8
```

## Explanation

The weed can grow in the following $8$ ways:
~[exemplu-better-2.png|width=30%]

# Example 2

`buruiana.in`
```
6 9
```

`buruiana.out`
```
714900741
```

## Explanation

The answer must be displayed modulo $10^9+7$.