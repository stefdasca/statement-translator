Ionică has a box full of cubes. Each cube has a digit written on it. At some point, Ionică stacks $n$ cubes one on top of the other forming a tower. Seeing the tower, Ionică's father tells him a digit $k$ and a method for removing cubes from the tower. Specifically, Ionică needs to remove cubes to get a tower with the minimum height according to the following rules:
* at any time a group of at least $k$ adjacent cubes that have the same digit written on them can be removed;
* the groups are removed starting from the base of the tower, each time beginning with the first group that meets the previous condition.

# Task

Write a program that determines the final tower, after removing all groups of cubes according to the method specified by Ionică's father.

# Input data

The input file `turn.in` contains on the first line the natural numbers $n$ and $k$ separated by a space, and on the next line, the digits written on the cubes in order from the base of the tower to the top, separated by spaces.

# Output data

The output file `turn.out` will contain on the first line the number of cubes in the final tower, and the second line the digits on the cubes in the tower (in order from the base of the tower to its top) with a space between each.

# Constraints and clarifications

* $2 \leq n \leq 49\ 000$
* $2 \leq k \leq 9$
* for all test cases the resulting tower has at least one cube

# Example 1

`turn.in`
```
20 3
1 0 2 2 2 0 0 0 7 7 5 5 5 5 5 7 7 7 3 9
```

`turn.out`
```
3
1 3 9
```

## Explanation

The evolution of the tower is as follows:
After removing the group of cubes with digits $2\ 2\ 2$ the result is: $1\ 0\ 0\ 0\ 0\ 7\ 7\ 5\ 5\ 5\ 5\ 5\ 7\ 7\ 7\ 3\ 9$
After removing the group of cubes with digits $0\ 0\ 0\ 0$ the result is: $1\ 7\ 7\ 5\ 5\ 5\ 5\ 5\ 7\ 7\ 7\ 3\ 9$
After removing the group of cubes with digits $5\ 5\ 5\ 5\ 5$ the result is: $1\ 7\ 7\ 7\ 7\ 7\ 3\ 9$
After removing the group of cubes with digits $7\ 7\ 7\ 7\ 7$ the result is: $1\ 3\ 9$

# Example 2

`turn.in`
```
21 4
1 2 2 2 2 1 1 3 3 3 3 3 1 1 4 4 4 4 4 1 1
```

`turn.out`
```
2
1 1
```

## Explanation

The evolution of the tower is as follows:
After removing the group of cubes with digits $2\ 2\ 2\ 2$ the result is: $1\ 1\ 1\ 3\ 3\ 3\ 3\ 3\ 1\ 1\ 4\ 4\ 4\ 4\ 4\ 1\ 1$
After removing the group of cubes with digits $3\ 3\ 3\ 3\ 3$ the result is: $1\ 1\ 1\ 1\ 1\ 4\ 4\ 4\ 4\ 4\ 1\ 1$
After removing the group of cubes with digits $1\ 1\ 1\ 1\ 1$ the result is: $4\ 4\ 4\ 4\ 4\ 1\ 1$
After removing the group of cubes with digits $4\ 4\ 4\ 4\ 4$ the result is: $1\ 1$