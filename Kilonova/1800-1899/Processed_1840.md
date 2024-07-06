Noble Stegan, a prince of Dendromarcei, was saddened by his father's death. After many futile attempts to discover his father's fate by calculating the area of different trapezoids using Simpson's rule, a spirit came to his aid. The spirit gave Stegan a tree to take care of. The spirit said: _"Look closer! Can't you see? This tree is special, as it has an even number of vertices. If you find a way to pair the vertices such that their cost is as minimal as possible, you will learn how your father died. But first, you must understand the cost of a pair. The secret lies in the meaning of life."_

Stegan, being a mathematician, knows that the meaning of life can be found in the words: "To be xor not to be" (a phrase that cannot be translated into Romanian). He deduced that for a pair of vertices, the cost of the pair is the value of the $XOR$ (exclusive OR) operation on the weights of the edges located on the path between these vertices.

To Stegan's detriment, he lacks computational skills, so he asks for your help.

Formally, you are given a tree with $N$ vertices, $N$ being even. Each edge has a weight. For a pair of vertices $(u,v)$, we define the cost of the pair as the value of the $XOR$ (exclusive OR) operation on the weights of the edges located on the path between these vertices.

You need to find a way to divide the vertices into $\frac{N}{2}$ pairs such that the sum of the costs is as minimal as possible. Since it may be difficult to find the minimal sum of the costs, we only ask you to do your best, being scored accordingly.

# Input data

The first line of input contains an even integer, $N$ - the number of vertices in the tree. The following $N-1$ lines contain $3$ space-separated numbers, $u_i, v_i, w_i,$ meaning that the vertices $u_i$ and $v_i$ are connected by an edge with weight $w_i$.

# Output data

The first line should contain the sum of the costs of the pairs of vertices you have chosen. The following $\frac{N}{2}$ lines should contain the indices of the vertices that form each pair. No pair should contain common vertices.

# Scoring

For each group:

1. If it is a test where you exceed the time limit or get a Runtime Error, you will receive $0$ points for that group.
2. If it is a test where any of the $\frac{N}{2}$ displayed pairs are invalid or the sum of the costs does not match the displayed value, you will receive $0$ points for that group.
3. If none of the above applies, you will receive points according to the following formula:

$$
\displaystyle \text{group\_score} \cdot \text{min}\left\{ \left( \frac{ok\_cost_i}{out\_cost_i} \right) ^4\right\}
$$

where:

* $i$ goes through each test in the group
* $out\_cost_i$ is the displayed answer for test $i$
* $ok\_cost_i$ is the optimal answer for test $i$

# Constraints and clarifications

* $2 \leq N \leq 200$
* $N$ is even
* $0 \leq w_i \leq 2^{24}$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 3     | $N \leq 10, w_i \leq 64$|
| 2 | 6    | $N \leq 14$      |
| 3 | 19    | $N \leq 40, w_i \leq 64$|    |
| 4 | 8      | $N \leq 120, w_i \leq 16$|   |
| 5 | 41 | $N \leq 120$    |
| 6 | 23    | No additional constraints.    |

# Example 1

`stdin`
```
6
5 2 42
5 4 52
6 3 26
4 6 39
1 6 15
```

`stdout`
```
54
1 6
3 5
4 2
```

## Explanation

~[xor1.png]

# Example 2

`stdin`
```
4
1 2 4
3 4 5
2 3 1
```

`stdout`
```
1
2 3
1 4
```

## Explanation

~[xor2.png]