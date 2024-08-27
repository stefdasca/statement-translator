## Task

The Roman Empire has expanded significantly and is now in a weakened state. At any moment, revolts can break out in any of its cities. Rome is no longer a safe capital, and Caesar wishes to relocate the capital and all imperial troops to a city from which the armies can traverse the empire quickly; in other words, to the city for which the sum of distances to all other cities is minimal. The empire has $N$ cities numbered from $1$ to $N$, and the road network has a tree structure, so that the imperial armies do not have difficulties in choosing the route between two cities. The distance between any two cities connected by a direct road is one day of travel.

## Input data

The first line of the file `capitala.in` will contain the number $N$ as described above. The next $N-1$ lines will each contain two numbers $A$ $B$ indicating that there is a road between cities $A$ and $B$.

## Output data

The first line of the file `capitala.out` will contain the city where the capital should be placed and the sum of distances to all other cities.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$

If there are multiple possibilities for placing the capital, print any one of them.

No partial points will be awarded.

## Example

`capitala.in`
```
5 
2 5 
2 1 
1 3 
4 2
```

`capitala.out`
```
2 5
```