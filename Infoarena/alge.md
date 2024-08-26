## Algae

A cubic-shaped aquarium with side length $n$ is first sectioned with $N-1$ horizontal and equally spaced planes, resulting in $N$ levels of thickness $1$, numbered from $1$ to $N$ ($1$ for the top one). Then it is sectioned with $N-1$ vertical planes, equally spaced and parallel to the left-right side faces, resulting in $N$ slices of thickness $1$, numbered from $1$ to $N$ ($1$ for the left one). Finally, it is sectioned with $N-1$ vertical planes, equally spaced and parallel to the front-back side faces, resulting in $N$ slices of thickness $1$, numbered from $1$ to $N$ ($1$ for the front one). The coordinates of a $1$-side cube in the section are in order: the first coordinate for the level, the second for the left-right slice, and the third for the front-back slice. The aquarium contains $M$ groups of algae. The groups have a cubic shape, positioned in $1$-side cubes from the section, and are arranged so that they do not touch each other, not even at a single point.

## Task

To determine a path in the aquarium for a small fish, which must leave from the sectioned cube located at the top-left-front corner, with coordinates $(1, 1, 1)$, and reach the sectioned cube in the bottom-right-back corner, with coordinates $(N, N, N)$, without passing through any group of algae, and the path to be of minimal length. The fish can move from one cube to an adjacent one (the two cubes sharing a common square).

## Input data

The file `alge.in` contains on the first line two natural numbers $N$ and $M$, separated by a space. On each of the next $M$ lines, three natural numbers separated by a space are written, representing the $3$ coordinates of the $1$-side cube from the section in which a group of algae is located.

## Output data

In the file `alge.out`, write: on the first line a natural number $k$ representing the length of the minimal path. On each of the next $k$ lines, three natural numbers, separated by a space, representing the coordinates of the $1$-side cubes from the section through which the minimal-length path passes. Each triplet represents the coordinates of a position in the fish's path (the first position will be $(1, 1, 1)$ and the last $(N, N, N)$).

## Constraints and clarifications

$2 \leq N \leq 35$  
$0 \leq M \leq 30$  
The $1$-side cubes from the section located in the top-left-front and bottom-right-back corners are not occupied by algae.  
The length of the path is equal to the number of $1$-side cubes from the section through which the fish passes.  
There may be multiple minimal-length paths. Only one solution is required.

## Example

`alge.in`  
```
3 1  
3 1 1
```

`alge.out`
```
7  
1 1 1  
1 1 2  
1 1 3  
1 2 3  
1 3 3  
2 3 3  
3 3 3
```

## Explanation

The aquarium has a side length of $3$ and there is a single group of algae located in the $1$-side cube from the section with coordinates $(3, 1, 1)$, meaning it is attached to the bottom-left-front corner of the aquarium. The minimal-length path of the fish passes through $k=7$ $1$-side cubes from the section, specifically: from the cube with coordinates $(1, 1, 1)$, in a straight line to the back of the aquarium, to the cube with coordinates $(1, 1, 3)$, then to the right to the cube with coordinates $(1, 3, 3)$, and then down to the cube with coordinates $(3, 3, 3)$.