## Task

You are the flower who I have chosen, and with care I have chosen you,
If it were for me to choose again,
Again I would choose you.

The sky, it does have many stars,
But I want only one of them,
There are flowers in the whole world,
But I want only my flower. (Nicolae Guta)

Nicolae sees $N$ stars in front of him. These can be modeled as 2-dimensional points, each having integer coordinates between $-10^8$ and $10^8$. Now he must decide the position and size of the central gravitational flower of the universe. This can be modeled as a 2-dimensional circle, with its center at an integer point. He wants to do this in such a way that exactly half of the stars are inside the central gravitational flower of the universe, and exactly half of the stars are outside of it.

More formally, $N$ points $(x_i, y_i)$ are given. Three integers $x, y, r$ must be found such that $-10^8 \leq x, y \leq 10^8$, $0 \leq r \leq 10^{18}$ and for exactly $N / 2$ points $(x', y')$ among the $N$ points $(x - x')^2 + (y - y')^2 \leq r$, and exactly $N / 2$ points $(x', y')$ among the $N$ points $(x - x')^2 + (y - y')^2 > r$. Note that $r$ is not the radius of the circle, but the square of the radius.

## Input data

The input file `stars.in` will contain, on the first line, the number $T$ of tests. Each test starts with a natural number $N$, with the meaning described above. Then follows $N$ lines, each containing values $x_i, y_i$. 

## Output data

The output file `stars.out` should contain, for each of the $T$ tests, the answers on separate lines. For each test, three values $x, y, r$ which satisfy the conditions in the task should be printed.

## Constraints and clarifications

$1 \leq T \leq 100000$

$1 \leq N \leq 100000$

The sum of the values of $N$ does not exceed 100000 in a file.

$N$ is even.

$-10^8 \leq x_i, y_i \leq 10^8$.

## Example

`stars.in`
```
2
2
0 -1
0 1
4
0 0
0 1
1 1
1 0
1 -3
```

`stars.out`
```
5
2
0
2
```