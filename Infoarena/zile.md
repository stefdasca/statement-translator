## Task

In a room, there are $N$ people. Each person is born on one of the $Z$ days of a year. Determine the birth days of each person so that there are exactly $K$ pairs of people in the room who were born on the same day.

## Input data

The file `zile.in` contains the integer numbers $N$, $Z$, and $K$, separated by spaces.

## Output data

The file `zile.out` must contain a single line that contains $N$ integers ranging from $1$ to $Z$, representing the birth days of the $N$ people, so that there are exactly $K$ pairs of people born on the same day in the room. If there are multiple solutions, you may print any of them. It is guaranteed that there will be at least one solution.

## Constraints and clarifications

$1 \leq N \leq 50$ 

$1 \leq Z \leq 365$ 

$0 \leq K \leq \frac{N*(N-1)}{2}$ 

## Example

`zile.in`

```
5 365 4
```

`zile.out`

```
1 1 1 365 365
```