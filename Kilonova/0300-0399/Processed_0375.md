# Task

Given an installation of $N * M$ lights. Each light is defined by its color, in RGB format. Thus, an element from the matrix can be considered a triplet $(x_R, x_G, x_B)$. Each value ranges from $0$ to $255$.

The dispersion of a color is defined as the number:

$$\left( \left[ \frac{x_G}{x_R}\right]^2 + \left[ \frac{x_B}{x_G}\right]^2 + \left[ \frac{x_R}{x_B}\right]^2 \right) * 1000.$$

(First, the integer part is calculated, followed by the other operations in known order). If the denominator of a fraction is $0$, the fraction is null. For example, for $(64, 128, 0)$, the dispersion is $(2^2 + 0^2 + 0^2) * 1000 = 4 * 1000 = 4000$.

It is known that one can move from one light to another if they are adjacent (in one of the four directions) and the absolute difference between the dispersions of the two elements in the matrix is less than or equal to an integer $P$.

It is known that the RGB format is additive, and the color black is $(0, 0, 0)$. For each light, there can be another light in the matrix such that their sum results in the color black. It is known that if these lights are connected (i.e., one can reach directly or indirectly from one to the other), the entire installation blocks.

For example, if we sum $(0, 128, 64)$ with $(128, 128, 128)$, we get the result: $(128, 0, 196)$ - each index is added with each, and if the result is greater than $255$, $256$ is subtracted.

# Task

1. How many pairs exist in the matrix, for which their connection would determine the color black?
2. For such a given installation, what is the maximum number $P$, for which the installation does not block?

# Input data

The first line of the file `lumini.in` contains three natural numbers $N, M, C$. The last number represents the index of the task to be solved.
The next $N$ lines of the file contain $3 * M$ numbers each, separated by a space, which define each light in the matrix. Thus, from a triplet, the first number is the intensity $R$, the second $G$, and the third $B$.

# Output data

The output file `lumini.out` will contain on the first line, the number of pairs formed, if the first task must be solved.
If the second task must be solved, the found $P$ will be printed.

# Constraints and clarifications

* $N, M \leq 1000$
* $1 \leq C \leq 2$
* The first task is worth $30$ points, and the second task $70$ points.
* For the second task, for $20$ out of the $70$ points, $N, M \leq 50$
* For reading, it is recommended to use the `<cstdio>` library in C++.

# Example 1

`lumini.in`
```
3 2 1
0 64 64 64 64 0
128 128 128 192 192 192
0 192 192 192 192 0
```

`lumini.out`
```
2
```

## Explanation

Only the first task will be solved:

The first $2$ bulbs are $(0, 64, 64), (64, 64, 0)$. They have an intensity of $1000$.
$(128, 128, 128)$ and $(192, 192, 192)$ have an intensity of 3000. $(0, 192, 192)$ and $(192, 192, 0)$ have an intensity of $1000$.

# Example 2

`lumini.in`
```
3 2 2
0 64 64 64 64 0
128 128 128 192 192 192
0 192 192 192 192 0
```

`lumini.out`
```
1999
```

## Explanation

Only the second task will be solved:

- $(0, 64, 64) + (0, 192, 192) = (0, 0, 0);$
- $(64, 64, 0) + (192, 192, 0) = (0, 0, 0).$

Thus, in total, $2$ pairs form black.
For $P = 2000$, either of the two pairs can be formed.