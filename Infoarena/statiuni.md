## Task

The road map of an island has the shape of a tree. The nodes represent resorts, and the edges represent direct roads connecting two resorts. The beach resorts are those connected to only one other resort. Determine the number of resorts on the island with the property that there are roads consisting of at most $k$ edges to at least two beach resorts.

## Input data

The first line of the file `statiuni.in` contains $N$ - the number of resorts on the island and $k$ - the number of edges allowed to a beach resort. The next $N-1$ lines contain two numbers each, ranging between $1$ and $N$, representing a direct road between two resorts. The numbers are separated by space.

## Output data

The first line of the file `statiuni.out` will contain the required number.

## Constraints and clarifications

$1 \leq N \leq 100000$

If a resort is on the beach, one of the resorts at a distance of at most $k$ from it is considered to be itself (at a distance of $0$).

## Example

`statiuni.in`
```
6 2
1 2
2 3
3 4
4 5
4 6
```

`statiuni.out`
```
4
```

## Explanation

The resorts with the required property are $3$, $4$, $5$, and $6$.