# Playground for the two Pokémon, **Fire and Water**, can be represented as a two-dimensional map with marked coordinate points $(x, y)$, where $0 \leq x \leq N$ and $0 \leq y \leq M$. Among these $(N + 1) \times (M + 1)$ points marked on the map, $P$ points are special points where the Pokémon can hide (hidden-points).

Initially, the Pokémon **Fire** is at the coordinate point $(0, 0)$ and wants to reach the coordinate point $(N, M)$. It can move at any moment from the coordinate point $(x, y)$ to one of the neighboring points $(x, y + 1)$ or $(x + 1, y)$. The Pokémon **Water** is initially at the coordinate point $(N, M)$ and wants to reach the coordinate point $(0, 0)$. It can move at any moment from the coordinate point $(x, y)$ to one of the neighboring points $(x, y - 1)$ or $(x - 1, y)$.

As in any game, the Pokémon have established rules, as follows:
1. The Pokémon **Fire** starts the game and chooses the first path to follow.
2. The Pokémon **Water** chooses the path to follow after **Fire** follows its path.
3. Each Pokémon follows a path that visits **the maximum number of special points available**.
4. If there are multiple paths with the maximum number of special points, the **lexicographically smallest path** will be chosen.
5. Once a special point is visited, it will lose its property of being a special point.

# Task

Given $N$, $M$, and the list of special points, write a program that determines the number of special points left on the map at the end of the game.

# Input data

The input file `pokemoni.in` contains on the first line the natural numbers $N$, $M$, and $P$ with the meaning from the statement. The following $P$ lines contain the special points, one point per line; a special point is specified by its coordinates $x \, y$. The numbers on the same line of the input file are separated by a space.

# Output data

The output file `pokemoni.out` will contain a single line that will have a natural number representing the number of special points left on the map at the end of the game.

# Constraints and clarifications

* $2 < N, M \leq 10 \, 000$
* $1 < P \leq 100 \, 000$
* $0 \leq x \leq N$, $0 \leq y \leq M$
* Assume that a point $(x_1, y_1)$ is smaller than a point $(x_2, y_2)$ if $x_1 < x_2$ or $x_1 = x_2$ and $y_1 < y_2$.
* A path $(t_1, t_2, \ldots, t_{\text{lg}})$ is lexicographically smaller than another path $(s_1, s_2, \ldots, s_{\text{lg}})$ if there exists $i \geq 0$, such that $t_j = s_j$ for any $0 \leq j < i$ and $t_i < s_i$.

|#|Points|Constraints|
|-|-|-|
|1|30|$2 < N, M \leq 100, 1 < P \leq 1 \, 000$|
|2|20|$100 < N, M \leq 1 \, 500, 1 \, 000 < P \leq 10 \, 000$|
|3|20|$N = 1 \, 000, M = 1 \, 000, 10 \, 000 < P \leq 100 \, 000$|
|4|15|$1 \, 000 < N, M \leq 1 \, 500, P = 100 \, 000$|
|5|15|$N= 10 \, 000, M = 10 \, 000, P = 100 \, 000$|

# Example

`pokemoni.in`
```
6 8 12
5 5
1 4
3 6
4 4
6 7
4 7
0 7
1 2
5 1
6 6
2 1
3 2
```

`pokemoni.out`
```
2
```

## Explanation

~[img1.jpg|align=right]

The two possible paths chosen by the Pokémon are marked in the adjacent image.

The maximum number of special points that can be visited by the Pokémon **Fire** is $6$. 
There are several paths to visit these $6$ special points:
1. $(1, 2) - (1, 4) - (4, 4) - (5, 5) - (6, 6) - (6, 7)$
2. $(1, 2) - (3, 2) - (4, 4) - (5, 5) - (6, 6) - (6, 7)$

Among these paths, the first path was chosen as it is the lexicographically smallest.

The $6$ special points visited by the Pokémon Fire lose their special point quality.

From the remaining special points, the Pokémon **Water** can visit a maximum of $4$.

There are $2$ special points left on the map at the end.