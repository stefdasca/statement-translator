
Between the city $X$ and the city $Y$ there is a very complex railway system. The city $X$ is to the west of the city $Y$. Both the station in the city $X$ and the station in the city $Y$ have $N$ platforms, with platform $1$ being the northernmost and platform $N$ being the southernmost.

There are $M$ tracks installed between the two cities. Track $i \\ (1 \\leq i \\leq M)$ connects via a straight line the platform $a_i$ in the city $X$ with the platform $b_i$ in the city $Y$.

The infrastructure is starting to age, so you decided to renovate the tracks, but before that, you need to find out how many level crossings (intersections) exist between them. In other words, you want to find out how many pairs of tracks intersect (excluding those that intersect only in one of the two stations).

# Task

How many such intersections exist?

# Input data

The first line contains the numbers $N$ and $M$ from the statement. The next $M$ lines contain the description of the tracks. On line $i \\ (1 \\leq i \\leq M)$ there are the numbers $a_i$ and $b_i$, with the meanings from the statement.

# Output data

Print a single number, namely the number of intersections between the train tracks.

# Constraints and clarifications

* $1 \\leq N, M \\leq 3 \\cdot 10^5$
* $1 \\leq a_i, b_i \\leq N$ for each $1 \\leq i \\leq M$
* $1 \\leq M \\leq N^2$
* There will not be two tracks connected between the same pair of platforms.
* There can be platforms without associated tracks, both in city $X$ and in city $Y$.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 18      | $1 \\leq N, M \\leq 50$ |
| 2 | 16      | $1 \\leq N, M \\leq 2 \ 000$     |
| 3 | 55      | $1 \\leq N \\leq 2 \ 000$     |
| 4 | 11     | No additional constraints.      |

# Example

`stdin`
```
10 6
1 10
1 5
2 6
2 10
6 1
5 5
```

`stdout`
```
9
```

## Explanation

The $9$ intersections expressed in the form $(i, j)$, meaning track $i$ intersects track $j$, are: $(1, 3), (1, 5), (1, 6), (2, 5), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)$.
