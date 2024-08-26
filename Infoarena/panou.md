## Task

Buru has at home two panels with brand-new bulbs received as a gift from Santa Claus. Each panel contains $N \times N$ bulbs arranged in a grid with $N$ rows and $N$ columns, some bulbs being lit, others turned off. Thus, each bulb can be associated with a position $(i, j)$ representing the row and column it is positioned in the panel. Let us consider the first panel as panel $A$ and the second panel as panel $B$. Underneath each bulb in panel $A$, there is a switch. If we activate a switch under a bulb located at row $i$ and column $j$, the state of all bulbs in positions $(x, y)$ with $x = i$, $y \leq j$ and all bulbs in positions $(x, y)$ with $x < i$, $y = j$ change (specifically, the state of all bulbs on the same row and smaller columns, the state of bulbs in the same column and smaller rows, and the state of the corresponding bulb on the activated switch). By changing the state of a bulb, we mean it switches from lit to off or from off to lit. Buru wants panel $A$ to look identical to panel $B$ after some switches. Moreover, he wants to achieve this with the minimum number of switches. Help Buru!

## Input data

The input file `panou.in` contains on the first line a natural number $N$ with the significance from the statement. On the following $N$ lines, there are $N$ characters $0$ or $1$ separated by a single space, representing the state of a bulb on the first panel (panel $A$). Next, $N$ lines follow, containing $N$ characters $0$ or $1$ separated by a space, representing the configuration of panel $B$. ($0$ means the bulb is off, whereas $1$ means the bulb is lit.)

## Output data

The output file `panou.out` contains on the first line a natural number $Min$ representing the minimum number of switches Buru needs to perform to make the two panels identical.

## Constraints and clarifications

$1 \leq N \leq 500$

The two panels are identical if any bulb located on row $i$ and column $j$ is in the same state on both panels.

## Example

`panou.in`
```
3
0 1 0
1 1 0
0 0 0
0 0 0
0 0 0
```

`panou.out`
```
1
```

## Explanation

By activating the switch located at position $(2, 2)$, the two panels become identical.