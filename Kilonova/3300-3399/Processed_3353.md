# Task

We have a rectangular board with $n$ rows and $m$ columns, consisting of $n \times m$ squares each with unit side. We wish to completely tile this board using the following $4$ types of tiles:

| Type     | Image | Description |
|----------|-------|-------------|
| Type 1   | ~[pavari1.png] | This type of tile is symmetric in any of its rotations and therefore has only one way in which it can be placed. |
| Type 2   | ~[pavari2.png] | This type of tile can be placed in two positions (horizontal or vertical). |
| Type 3   | ~[pavari3.png] | This type of tile can be placed in $4$ different positions. |
| Type 4   | ~[pavari4.png] | This type of tile has only one way it can be placed. |

Type $4$ tiles can be used at most once in any test. For the other $3$, it is indicated in each test which of them can be used (zero or more times). 

Two tiling solutions $A$ and $B$ are different if there exists at least one position on the given board that in solution $A$ is part of one type of tile and in solution $B$ is part of another type of tile or if that position is part of the same type of tile but in solution $A$ the tile has a different orientation than in solution $B$.

# Input data

The file `pavari.in` contains on the first line the numbers $n$ and $m$, representing the dimensions of the board to be tiled. The second line contains a number $p$, between $1$ and $3$, representing the number of types of tiles that can be used. On the next line there are $p$ distinct values, between $1$ and $3$, written in increasing order, representing the types of tiles.

# Output data

The file `pavari.out` contains on the first line an integer representing the number of distinct possible tiling solutions.

# Constraints and clarifications

- $1 \leq n, m \leq 10$;
- $1 \leq n \times m \leq 50$;
- The Type $4$ tile can be used at most once in any test.
- In any solution, the tiles must be entirely within the board and must not overlap.

# Example

`pavari.in`
```
2 6
3
1 2 3
```

`pavari.out`
```
3
```

## Explanation

~[pavari5.png|width=30%]

Colors are not important; they have been added only to differentiate the types of tiles. All types of tiles can be used. It can be observed that no tiling can be made using types $3$ and $4$.