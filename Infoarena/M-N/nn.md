## Task

The great engineer $NN$, an expert in dam construction, has received a more complicated task this time. He has to build $M$ dams across multiple rivers in a delta and plans the construction of each dam on graph paper. All the rivers over which he has to build dams are branches of the same river, and all start from the same point along the river’s length. To explain his sketch, $NN$ marks the separation point of all branches of the river with a point $O$, called the origin. Then, starting from the origin, $N$ half-lines extend, each representing a portion of land, so the empty space between two consecutive half-lines will be considered a branch of the river. After drawing his project sketch, $NN$ wonders how many rivers each dam completely covers. A dam completely covers a river if it intersects each of its banks. Your task is to help him by providing precise information so he can implement his plan as efficiently as possible while maintaining his reputation.

## Input data

The first line of the file `nn.in` contains $N$ and $M$, representing the number of half-lines and the number of dams, respectively. Each of the next $N$ lines contains information about the $N$ half-lines as follows: on line $i$ $(1 \leq i \leq N)$ there is a pair of natural numbers $x$ and $y$, representing the coordinates of a point on half-line $i$ (we already know that all half-lines start from $O(0, 0)$). Each of the next $M$ lines contains $4$ numbers $x_1$, $y_1$, $x_2$, $y_2$ representing that there is a dam with extremities at the points with coordinates $(x_1, y_1)$ and $(x_2, y_2)$.

## Output data

The output file `nn.out` will contain $M$ numbers, each on a separate line, representing the number of rivers blocked by each of the $M$ dams. The thickness of the dam will be considered negligible in solving the problem.

## Constraints and clarifications

All numbers in the input file are natural numbers $\leq 10^5$

No point in the file coincides with the origin

For $10\%$ of the tests $N = 2$, $M = 1$

For the next $20\%$ of the tests, the endpoints of the segments (dams) will lie on the half-lines from the input data

For the first $50\%$ of the tests $N, M \leq 1000$

The use of `long double` type is recommended for working with rational numbers.

## Example

`nn.in`
```
5 3
5 1
2 1
2 5
5 5
0 4
3 0 4 2
1 4 3 1
5 3 7 6
```
`nn.out`
```
1 
2 
0 
```