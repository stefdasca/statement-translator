Once upon a time, there was a man so poor that his only possession was a flock of sheep situated at natural nonzero coordinates less than $5\ 000$. Unfortunately, our man forgot how many sheep he had and where they were located. The only thing he remembered was the sum of the Manhattan distances from all his sheep to any point with natural coordinates less than or equal to $5\ 000$. Since the set of points where he needs to search for his sheep is enormous, he asks you to help him find the lost sheep.

# Interaction Protocol

Your program must include a function

```cpp
void findPoints()
```

This function must call a limited number of times the function:

```cpp
long long getDistance(int x, int y)
```

which will return the sum of the Manhattan distances from the point at coordinates $(x, y)$ to all the sought sheep and must call a function

```cpp
void newPoint(int x, int y)
```

to announce that a sheep has been found at coordinates $(x, y)$.

The two functions are provided by the committee to the competitors.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000\ 000$
* $1 \leq x, y \leq 4\ 999$ for any of the sought sheep
* There may be multiple sheep at the same coordinates
* $0 \leq x, y \leq 5\ 000$ for any call to the `getDistance` function
* The Manhattan distance between the points $(x_1, y_1)$ and $(x_2, y_2)$ is $|x_1-x_2|+|y_1-y_2|$
* For $70\%$ of the score, the number of calls to the `getDistance` function must be at most $20\ 000$.
* For $100\%$ of the score, the number of calls to the `getDistance` function must be at most $9\ 999$.
* The `manhattan.h` header must be included in the program

# Example

`grader`: `findPoints()`
`contestant`: `getDistance(1, 1)`
`grader`: `return 0`
`contestant`: `getDistance(1, 2)`
`grader`: `return 2`
`contestant`: `newPoint(1, 1)`
`contestant`: `newPoint(1, 1)`

## Explanation

The two calls are sufficient to deduce that there are exactly two sheep, both at coordinates $(1, 1)$.