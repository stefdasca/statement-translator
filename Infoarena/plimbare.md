# Walk

The tests for this problem are not well constructed enough to correctly separate inefficient or incorrect solutions. Enter here if you want to help us improve the quality of the tests for this problem! In each city where the members of the informatics team prepare before the international olympiads, there is a walk organized to visit the tourist attractions. This year the city where the olympians have arrived has the curious property that there is a street between any two objectives, but the street is one-way.

## Task

Determine a walk of maximum length that can go on the streets of the city in their normal direction of movement, so that at the end of the walk we reach the same objective from which we started, and each street or objective is visited at most once (except for the objective where we start which will be visited twice).

## Input data

In the input file `plimbare.in` the first line will contain the number $N$ of objectives. On the following $\frac{N \cdot (N-1)}{2}$ lines there will be two integers $x, y$ separated by exactly one space, with the significance that between objective $x$ and objective $y$ there is a street in the direction from $x$ to $y$.

## Output data

The output file `plimbare.out` will contain the maximum number $P$ of objectives that we can visit in such a walk on the first line. The next line will contain $P$ integers separated by space, which will give us the visited objectives and the order in which they are visited.

## Constraints

$1 \leq N \leq 100$

## Example

`plimbare.in`  
```
4
1 2
1 4
2 3
3 1
3 4
4 2
4 1
```

`plimbare.out`
```
4
1 4 2 3 1
```

## Explanation

The longest walk is one that visits all the $4$ objectives. The objectives will be visited in the order $1 \rightarrow 4 \rightarrow 2 \rightarrow 3 \rightarrow 1$.