# The Wind

The wind, it beats me in the face, And I have no feeling for life, Oh, soul ... what a larcenous world. My friends, with whom I have drunk, Where are they? Oh, soul ... friends like two coins I’m finished, and I’m changing my page with all, And the vagabond’s mothers, They are evil and twisted, My friends, they are. (Nicolae Guta) Given a convex polygon with $N$ vertices. For a given $K$, select a random subset $S$ containing $K$ vertices of the polygon. Consider the convex polygon that is formed if we take the coordinates of $S$ in a counterclockwise order. What is the expected value of the area of the formed polygon?

## Input data

The input file `vantu.in` will begin with the numbers $N$ and $K$. The next $N$ lines will contain the coordinates of the given polygon's points.

## Output data

In the output file `vantu.out`, if the required average is the ratio between $p$ and $q$, print $p * q^{-1} \mod 998244353$, where $q^{-1}$ is the modular inverse of $q$ modulo $998244353$.

## Constraints

$3 \leq N \leq 70000$

$3 \leq K \leq N$

$-10^9 \leq$ the coordinates of the points $\leq 10^9$

## Example

`vantu.in`
```
4 4
0 0
1 0
1 1
0 1
```

`vantu.out`
```
1
```

`vantu.in`
```
4 3
0 0
1 0
1 1
0 1
```

`vantu.out`
```
499122177
```