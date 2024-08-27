## Task

Vitezomanul Mirel has just bought a new AI-mobile (a state-of-the-art car) and wants to drive it through Targu Mures. The city is made up of $M$ bidirectional streets and $N$ intersections, each street connecting 2 different intersections. Having a lot of time available, he wants for each pair of intersections $(i, j)$ to get to intersection $j$ from intersection $i$ as quickly as possible using only the streets in the city. Unfortunately for him (and for you), he insists that on any street he travels on, he must reach a higher speed than the speed he reached on the previous street. In each intersection, he must brake to change the street, and the longer the street, the higher the speed he can reach on it. Unfortunately, Mirel is only good at driving, so he asks you to find out for him the shortest path between any two intersections $(i, j)$ while respecting his requirements.

## Input data

The input file `viteza2.in` contains on the first line $N$ and $M$ representing the number of intersections and streets in the city. The next $M$ lines each contain 3 numbers $A$, $B$, and $D$ signifying that between intersections $A$ and $B$ there is a street of length $D$ that connects them.

## Output data

The output file `viteza2.out` should contain $N$ lines each with $N$ numbers. The $j$-th number on the $i$-th line should represent the minimum length of a path that starts from intersection $i$, ends at intersection $j$, and respects Mirel's requirements. If there is no path that meets these requirements, Mirel asks you to print $-1$.

## Constraints

1 $\leq$ $N$ $\leq$ 1\,000

1 $\leq$ $M$ $\leq$ 5\,000

1 $\leq$ $A, B$ $\leq$ $N$

1 $\leq$ $D$ $\leq$ 1\,000\,000

For any two intersections $A$, $B$ there is at most one street connecting them.

Street lengths are all different from each other.

For 20% of the tests: 1 $\leq$ $N$ $\leq$ 15 and 1 $\leq$ $M$ $\leq$ 50

For another 20% of the tests: 1 $\leq$ $N$ $\leq$ 100 and 1 $\leq$ $M$ $\leq$ 1\,000

## Example

`viteza2.in`
```
4 4
1 4 1
1 2 3
2 3 7
3 4 8
```
`viteza2.out`
```
0 3 9 1
3 0 7 15
9 7 0 8
1 15 8 0
```

## Explanation

From intersection 2 to intersection 4, there is a path of length 4 $(2 \rightarrow 1 \rightarrow 4)$ but it does not meet Mirel's requirements (specifically, the length of the edge from $1 \rightarrow 4$ is smaller than that of the edge $2 \rightarrow 1$).