Here is the translated competitive programming problem statement in English:

---

Roberto has the soul of an artist. He dreams of becoming a famous painter someday, but for the moment he earns his living as a painter.

Roberto has been tasked with painting a wall of length $n$ meters and height one meter.

For this, he has $m$ days available. Each day $i$, he covers a compact portion of height one meter and length $l_i$ meters, starting at a distance $d_i$ meters from the left end of the wall.

From experience, Roberto knows that each portion of the wall must be covered with at least $K$ layers of paint for the final coat to have the desired consistency. Unfortunately, his artistic nature didn't allow him to plan his work optimally, so at the end of the $m$ days of effort, Roberto found that the wall has portions covered more than $K$ times and portions covered less than $K$ times.

To redeem himself in his own eyes and especially in the eyes of the team leader, he needs to first find out the total area of all the portions of the wall that still need to be painted.

# Task

Knowing the length of the wall $n$, the number of days $m$, and the compact portions he paints each day, determine the total area of the wall that still needs to be painted.

# Input data

The input file `paint.in` contains on the first line three natural numbers $n$, $k$, and $m$ separated by a space, where $n$ is the length of the wall, $k$ is the minimum number of layers of paint to achieve the desired consistency, and $m$ is the number of days Roberto paints.
The next $m$ lines contain two natural values separated by a space. The numbers $d_i$ and $l_i$ on the $i + 1$ line represent the distance from the left end of the wall at which he starts painting on day $i$, and the length in meters of the portion of the wall painted on day $i$.

# Output data

The output file `paint.out` contains on the first line a natural number $S$ which represents the total area of the wall that has not been covered with at least $k$ layers of paint.

# Constraints and clarifications

* $1 \leq n, m \leq 250\ 000$
* $1 \leq k \leq min(100\ 000, m)$
* $0 \leq d_i < l_i < n$

# Example

`paint.in`
```
5 2 3
0 2
1 3
2 3
```

`paint.out`
```
2
```

## Explanation

$n = 5, k = 2, m = 3$.
On the first day, Roberto paints $2$ meters of the wall between positions $0$ and $2$. On the second day, Roberto paints $3$ meters of the wall between positions $1$ and $4$. On the third day, Roberto paints $3$ meters of the wall between positions $2$ and $5$.
Thus, starting from the left end of the wall, there will be a portion of the wall of length $1$ covered with a single layer and starting from the distance of $4$ from the end, there will be another portion of wall of length $1$ covered with a single layer.

---

I have double-checked the statement for potential grammar and syntax errors and corrected them accordingly.