# Streets

Bursuc no longer writes poetry, no longer plays the guitar, nor does he solve computer science problems. Therefore, he asks you to help him with the following problem. A friend of his from the village of Fribsd asked for his help to streamline the traffic in the village. In the village, there are $N$ houses numbered from $1$ to $N$ and $M$ paths that are one-way only. A path that connects house $A$ to house $B$ allows people to go from house $A$ to house $B$ (the direction is one-way, so traveling on this path does not allow reaching house $A$ from house $B$). Bursuc also knows that it is not possible to start from any house $A$ and, by traveling only on the current paths, reach house $A$ again. Sometimes, guests come to the village and would like to visit all the houses exactly one time by walking only on the paths. In other words, they would like a sequence of houses $X_1$, $X_2$, $X_3$ $\dots$ $X_N$ such that there is a path between houses $X_i$ and $X_{i+1}$ for every $i \leq N-1$. Currently, this is not possible, so a minimum number of paths need to be constructed so that such a route exists.

## Input data

The input file `strazi.in` contains the following data:

- The first line contains two numbers $N$ and $M$ having the significance described above.
- The next $M$ lines contain two numbers $A$ and $B$ with the significance that there is a path from house $A$ to house $B$.

## Output data

The output file `strazi.out` contains the following data:

- The first line contains the number $MIN$ which represents the minimum number of paths that need to be constructed.
- The next $MIN$ lines, each containing two numbers $X$ and $Y$ with the significance that a path has been constructed from house $X$ to house $Y$.
- The last line contains $N$ distinct natural numbers with values between $1$ and $N$, representing a route that the guests could follow.

## Constraints and clarifications

$1 \leq N \leq 255$

$1 \leq M \leq 7000$

If multiple solutions are possible, any of them can be displayed.

For at least $20\%$ of the tests, $N \leq 10$

## Example

`strazi.in`
```
3 2
1 2
1 3
```

`strazi.out`
```
1
2 3
1 2 3
```

## Explanation

If the path from $2$ to $3$ is constructed, the houses $1$, $2$, and $3$ can be visited in order, with a path existing between every two consecutive houses.
