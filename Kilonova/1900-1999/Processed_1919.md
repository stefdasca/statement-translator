Here is the translated problem statement following the specified instructions:

---

Points are added, one by one, to the plane, with $N$ points in total. Each point has integer coordinates.
For each point added, you need to find the minimum Manhattan distance from that point to any of the points added before it.

# Input data

The first line of the input file `mindist.in` will contain $N$, the number of points.
Next, there are $N$ lines, on the $i$-th line, the integer coordinates $x_i \\ y_i$ of the $i$-th inserted point will be contained.

# Output data

The output file `mindist.out` will contain $N$ lines.
On the $i$-th line, a single integer $d_i$ will be contained, representing the minimum Manhattan distance from point $i$ to any of the points added before it.

# Constraints and clarifications

* The answer for the first point, $d_1$, is considered to be $0$
* The Manhattan distance between points $(x_1, y_1)$ and $(x_2, y_2)$ is defined as $|x_1 - x_2| + |y_1 - y_2|$
* For $20\\%$ of the tests, $N \\leq 150$
* For the remaining $80\\%$ of the tests, $N \\leq 50 \ 000$
* $1 \\leq x_i, y_i \\leq 50 \ 000$

# Example

`mindist.in`
```
4
4 1
3 4
2 2
1 3
```

`mindist.out`
```
0
4
3
2
```

---