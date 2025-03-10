
# Task

You are given $n$ pairs of coordinates that represent the initial positions of $n$ airplanes. Each airplane $i$ also has a flight direction $d_i$. This can be 'U' (up), 'D' (down), 'L' (left), or 'R' (right). At second $0$, the airplanes will start flying in the given direction with a constant speed of one unit per second.

When two airplanes are at the same coordinates, they do not collide but continue flying, as they are at different altitudes. Determine the number of pairs $(i, j)$ ($1 \le i < j \le n$) for which the airplanes $i$ and $j$ will have the same coordinates at some moment in time.

~[Avioane.png|align=center|width=30%]

# Input data

The first line contains the value $n$ (the number of airplanes). On the $i$-th of the next $n$ lines, there will be the values $x_i$ and $y_i$ (the starting coordinates of airplane $i$), as well as the character $d_i$ (representing the starting direction).

# Output data

The first line should contain a single number, representing the number of pairs of airplanes $(i, j)$ that will ever be at the same coordinates. **It is recommended to use the long long data type.**

# Constraints and clarifications

For all test cases, it holds that $1 \le n \le 5\cdot10^5$ and $1 \le x_i, y_i \le 10^6$ for any $1 \le i \le n$. Also, any two airplanes are at **distinct positions**.

|#| Points | Constraints                                                  |
|-|-------|-------------------------------------------------------------|
|1|    6  | $n=2$                                                       |
|2|   17  | $n \le 1000$                                                 |
|3|   24  | $x_i=1$ for any $1 \le i \le n$                              |
|4|   34  | $x_i, y_i \le 1000$ for any $1 \le i \le n$                  |
|5|   19  | No additional constraints                                    |

# Example 1

`stdin`
```
4
1 2 D
2 1 R
2 4 L
3 4 L
```

`stdout`
```
3
```

## Explanation

The example is illustrated in the above image. The dotted lines represent the paths of the airplanes, and the places where pairs of airplanes meet are circled.

# Example 2

`stdin`
```
2
1 3 D
2 1 R
```

`stdout`
```
0
```

## Explanation

It is not enough for the paths of two airplanes to intersect. They must be at the intersection point at the same time.

# Example 3

`stdin`
```
3
1 2 D
2 1 R 
3 2 U
```

`stdout`
```
3
```

## Explanation

Any two airplanes will meet at the same coordinates $(2, 2)$. Even if the meeting coordinates are the same for the $3$ pairs, they are counted separately.
