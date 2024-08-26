# Tarnacop

Due to excessive digging, the mining galleries of the city of Targu Mures have been flooded by an underground river. The mining galleries can be considered as a graph with $N$ nodes ($N$ rooms) and $M$ edges ($M$ corridors between rooms). The room where the accident happened (where the underground river entered the galleries) is known, and we'll denote it as $S$. Giugudel came to help the miners with his magic pickaxe. He managed to dig a drainage hole for the water from the galleries, the drainage hole being located in room $D$. Now, Giugudel knows for each corridor the capacity (the number of cubic meters of water that can pass through that corridor per second) and the amount of water passing through that corridor. Evidently, this amount will be less than the capacity. Giigudel knows the number of cubic meters of water draining through room $D$ per second, and he is curious to find out for each corridor, if its capacity were decreased by one unit, whether the capacity of water flowing per second through room $D$ would also decrease.

## Input data

The input file `tarnacop.in` will contain on the first line the numbers $N, M, S, D$ with the meaning from the statement. Each of the next $M$ lines will contain a quadruplet of the form $X, Y, C, I$, meaning that there is a corridor between rooms $X$ and $Y$, with a capacity $C$ through which $I \text{ m}^3$ of water passes per second.

## Output data

The output file `tarnacop.out` will contain on the first line a natural number $K$, representing the number of edges with the property specified in the statement. Each of the next $K$ lines will contain a pair of natural numbers $X, Y$, indicating that the edge from $X$ to $Y$ has the property from the statement. The edges must be displayed in ascending order of $X$, and in case of equality, in ascending order of $Y$.

## Constraints and clarifications

$1 \leq S, D \leq N \leq 100\ 000$

$1 \leq M \leq 300\ 000$

$S \neq D$

$0 \leq I \leq C \leq 5\ 000\ 000$

Edges with capacity 0 cannot be reduced

For any room different from $S$ and $D$, the sum of water quantities entering the room is equal to the sum of water quantities leaving the room

Water can flow through a corridor only in the direction specified in the input (for an edge $X, Y$ water will always flow from $X$ to $Y$)

The amount of water draining through $D$ is maximally possible

There will be no multiple edges between two nodes

There will be no self-loops

## Example

`tarnacop.in`

```
4 4 1 4
1 2 1 1
2 3 1 1
3 4 1 1
2 4 2 0
```

`tarnacop.out`

```
1
2 4
```