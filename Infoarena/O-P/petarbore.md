## Task

Minister Brantz is set to arrive tomorrow in Berlint to negotiate with the representatives of Westalis. However, Westalian terrorists have other plans: to start a war. Berlint has the shape of a tree with $N$ nodes (a connected acyclic graph), where each node represents an intersection, and the value on an edge represents the number of minutes it takes to traverse that edge. Terrorists can hide in any intersection. Agent Twilight is trying to prevent a war between Westania and Ostania and wants to know how much time he has to stop them. The terrorists operate as follows: they hide in multiple intersections, not necessarily adjacent. Each terrorist in an intersection will send a signal to possible terrorists in adjacent intersections (connected by an edge starting from the current intersection). If there is a terrorist who receives a signal, they will detonate a bomb. Twilight wants to prevent any bomb detonation, so in the case that multiple terrorists receive signals, he is interested in the first terrorist who receives it. Twilight will analyze all combinations of intersections where the terrorists can hide and will determine for each the minimum time in which a terrorist receives a signal from a neighbor. Finally, he wants to calculate the expected time until a bomb explodes. Since mathematics is one of the many skills he possesses, Twilight deduced that this expected value $E$ is in the form... He manages to calculate $2^n$, but does not have much time to calculate $S$, so he is asking you to find it. Moreover, he requires this value modulo $998244353$. In other words, $S$ is the sum of the minimum times in which a bomb explodes for all combinations of intersections.

## Input Data

The input file `petarbore.in` will contain on the first line $N$, representing the number of nodes of the tree. On the next $N-1$ lines, the edges of the tree will be listed in the form $x \ y \ z$ representing the edge and the time required for a signal from $x$ to reach $y$ and vice versa.

## Output Data

The output file `petarbore.out` will contain a single number, representing the value of $S$ modulo $998244353$.

## Constraints

The duration of the edges will be at most $10^9$.

### Subtask

Scoring:

## Constraints

1. $20$ points $1 \leq N \leq 15$
2. $20$ points $1 \leq N \leq 200$
3. $20$ points $1 \leq N \leq 5000$ and the edges will have durations of $1$ or $2$
4. $20$ points $1 \leq N \leq 5000$ and the edges will have different durations
5. $20$ points $1 \leq N \leq 5000$

## Example

`petarbore.in`
```
4
1 2 1
1 3 1
3 4 2
```

`petarbore.out`
```
10
```

## Explanation

$f(\{1, 2\}) = 1$, $f(\{1, 3\}) = 1$, $f(\{1, 2, 3\}) = 1$, $f(\{3, 4\}) = 2$, $f(\{1, 2, 4\}) = 1$, $f(\{1, 3, 4\}) = 1$, $f(\{2, 3, 4\}) = 2$, $f(\{1, 2, 3, 4\}) = 1$

The rest of the subsets $X$, apart from the ones listed above, have $f(X) = 0$. The value $S$ will be: $1 + 1 + 1 + 2 + 1 + 1 + 2 + 1 = 10$. The expected time until a bomb explodes will be ..., but fortunately, we only need $S$.