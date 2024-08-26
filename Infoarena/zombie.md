## Zombie

On a street consisting of $D$ squares, zombies appear at different times from the right end. There are $N$ zombies, and for each one, you know the time they enter square $D$. All zombies, once they enter the street, move at a speed of $1$ square per second towards the left end. The good wizard is positioned just to the left of the left end (square $0$) and must kill all zombies before they reach him. He has $2$ spells:
1. "Rasengan" instantly kills the first zombie in front of him at the cost of $1$ chakra.
2. "Rasen Shuriken" instantly kills all zombies on the street at the cost of $K$ chakra.

## Input data

The input file `zombie.in` contains on the first line $3$ natural numbers $D$, $N$, $K$ as described above, and on the second line, there will be $N$ natural numbers representing the times at which the $N$ zombies enter the street.

## Output data

The output file `zombie.out` will contain a single natural number representing the minimum chakra the wizard needs to use to kill all the zombies.

## Constraints and clarifications

$1 \leq D \leq 1\ 000\ 000\ 000$

$1 \leq N \leq 1\ 000\ 000$

$1 \leq K \leq 1\ 000\ 000$

the times when zombies appear are each distinct and are within the range $[1, 1\ 000\ 000\ 000]$

the times when the zombies appear are given in ascending order

## Example

`zombie.in`
```
5 5 2 1 10 11 12 13
```

`zombie.out`
```
3
```

## Explanation

He can kill the first zombie with "Rasengan" consuming $1$ chakra, and the remaining four can be killed all at once with "Rasen Shuriken" consuming $2$ chakra.