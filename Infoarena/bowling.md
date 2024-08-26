## Bowling

Nargy and Fumeanu are playing bowling. Since both are experts, they have decided to increase the difficulty of the game and play with $N$ pins arranged in a row. Because both are experts, with any throw of the ball, either of them can knock down one pin or two adjacent pins in the row. The game is considered won by the player who knocks down the last pins. Given several states of the row of pins, and assuming that from that moment both players play optimally, determine for each state who wins.

## Input data

The input file `bowling.in` contains on the first line the number $T$ of states. The next $T$ lines will contain, at the beginning, the number $N$ of pins, followed by $N$ numbers describing the row of pins: 0 for an empty spot and 1 for an existing pin.

## Output data

The output file `bowling.out` will contain $T$ lines which will print the name of the player who wins (Nargy or Fumeanu).

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 50000$

For each configuration, it is considered that Nargy will make the first move.

For 50% of the tests $N \leq 500$

## Example

`bowling.in`

```
2
4 1 0 0 1
13 1 0 1 1 1 1 1 1 1 1 1 1 1
```

`bowling.out`

```
Fumeanu
Nargy
```