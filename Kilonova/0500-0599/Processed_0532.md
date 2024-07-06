***biom*** $sn^{[1]}$ [At: $DN^3$ / Pl: ~uri / E: it **bioma**] (Blg) Ecological complex that forms in relation to a certain ambient environment.

\\
Steve Stonecutter is in a world made up of cubes, and each cube belongs to a single biome. The cubes are arranged in a line and are numbered from $1$ to $N$. It is considered that blocks $i$ and $i + 1$ are adjacent to each other for all values of $i$ from $1$ to $N - 1$.

We can represent this world as a string $S$ of length $N$ made up of lowercase English alphabet letters, numbered from $1$ to $N$, where the $i$-th character represents the biome of the $i$-th cube.

To move, Steve can perform the following actions:
- He can move with a cost of $A$ from cube $i$ to its immediate right neighbor, i.e., $i + 1$;
- He can move with a cost of $B$ from cube $i$ to its immediate left neighbor, i.e., $i - 1$;
- He can move with a cost of $C$ from cube $i$ to the smallest cube $j$ for which $j \\gt i$ and $S_i = S_j$;
- He can move with a cost of $D$ from cube $i$ to the largest cube $j$ for which $j \\lt i$ and $S_i = S_j$.

\\
These movements can be performed if and only if the position Steve wants to move to exists. For example, if Steve is on cube $1$, he cannot perform the second or fourth movement.

Starting from cube $1$, Steve wishes to reach cube $N$ with minimum cost, so he asks you to find out what this cost is.

# Task
Determine the minimum cost for Steve to get from cube $1$ to cube $N$.

# Input data
The first line contains a single number $N$ representing the number of cubes in Steve's world.

The second line contains four numbers $A$, $B$, $C$, and $D$ representing the costs of each action that Steve can perform.

The third line contains the string $S$ of length $N$ representing the map of the biomes in the world.

# Output data
On a single line, print a single number representing the minimum cost to get from cube $1$ to cube $N$.

# Constraints
- $1 \\leq N \\leq 1\\ 000\\ 000$.
- $0 \\leq A, B, C, D \\leq 1\\ 000\\ 000\\ 000$.

|# | Points | Constraints |
| - | - | ------------ |
|1|12|$N \\leq 10$|
|2|8|For any $i \\lt j \\lt k$, if $S_i = S_k$ then $S_i = S_j$|
|3|11|$B = D = 1\\ 000\\ 000\\ 000$, and $A, C \\leq 1\\ 000$|
|4|19|$A = 1$, and each of $B$, $C$, and $D$ can be $1$ or $1\\ 000\\ 000\\ 000$|
|5|10|$A \\leq 1$, and each of $B$, $C$, and $D$ can be $0$, $1$ or $1\\ 000\\ 000\\ 000$|
|6|11|$N \\leq 500$|
|7|8|$N \\leq 100\\ 000$|
|8|21|no additional constraints|

# Examples
`biom.in`
```
6
3 5 4 2
abccbc
```
`biom.out`
```
10
```
Steve can move one position to the right with a cost of $3$. From cube $2$, he can move to cube $5$ with a cost of $4$. Finally, he moves again one position to the right to reach his destination, cube $6$. The total cost will be $3 + 4 + 3 = 10$.
\\
`biom.in`
```
15
1 2 3 4
abccabcbacbabcb
```
`biom.out`
```
11
```
Steve can move from cube $1$ to cube $5$, and then to cube $9$, both moves having each a cost of $3$. Then, from cube $9$ he can move to cube $10$ with a cost of $1$. From cube $10$, he can move to cube $14$ with a cost of $3$, and finally to reach his destination, in cube $15$, with a cost of $1$. The total moving cost will be $3 + 3 + 1 + 3 + 1 = 11$.