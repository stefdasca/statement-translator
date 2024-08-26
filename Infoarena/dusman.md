## Enemy

In a room, there are $N$ people among whom there are $M$ enemy relationships. We want to arrange the people in a sequence such that no one has an enemy as their neighbor.

## Task

Calculate the $K$-th arrangement in lexicographical order.

## Input data

The input file `dusman.in` contains on the first line three integers $N$, $K$, and $M$. The following $M$ lines contain two numbers $A$ and $B$ each, indicating that there is an enemy relationship between persons $A$ and $B$.

## Output data

The output file `dusman.out` will contain a single line with $N$ numbers that represent the $K$-th arrangement.

## Constraints and clarifications

$1 \leq N \leq 1\ 000$

No person will have more than 3 enemies

$1 \leq K \leq 10\ 000$

There will always be a solution

## Example

`dusman.in`
```
4 3 1
3 4
2 3
1 4
```
`dusman.out`
```
2 3 1 4
```

## Explanation

$1\ 3\ 2\ 4$

$1\ 4\ 2\ 3$

$2\ 3\ 1\ 4$

$2\ 4\ 1\ 3$

$\dots$