There once was a man so poor that his only possession was a board with $N$ rows (numbered from $1$ to $N$) and $N$ columns (numbered from $1$ to $N$), and in each position of this board, there was a bulb and a switch. Initially, all the bulbs are off. For any operation of a switch, the states of the bulbs in that position and up to four neighboring positions change simultaneously, meaning that the bulbs that were off turn on, and those that were on turn off.

# Task

Help the poor man find a way to operate the switches so that all the bulbs turn on.

# Input data

The input file `switch5.in` contains a single natural number $N$ on the first line.

# Output data

The output file `switch5.out` contains a matrix given by $N$ rows, with each row containing exactly $N$ digits $0$ or $1$, without spaces. This matrix will have the value $0$ at position $(i, j)$ if the switch at that position was not operated, or it will have the value $1$ if the switch at that position was operated.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$
* The output file will not contain any space characters

# Example

`switch5.in`
```
4
```

`switch5.out`
```
0100
0001
1000
0010
```

## Explanation

The switches were operated at positions $(1, 2)$, $(2, 4)$, $(3, 1)$, and $(4, 3)$.

Another correct result would have been:

```
1111
1001
1111
0000
```