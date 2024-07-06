A rectangular billboard contains bulbs, side by side, aligned in $n$ rows and $m$ columns.

Each bulb has an associated switch. By operating the switch of a bulb, the state of all bulbs on its row and column changes, except for its own state. Changing the state means transitioning from the current state to the opposite state (off $\\rightarrow$ on, on $\\rightarrow$ off).

# Task

Create a program that determines the minimum number of switch operations so that all bulbs on the billboard are off, if this is possible.

# Input data

The input file `becuri.in` contains on the first line two natural numbers separated by space $n$ and $m$ representing the number of rows and the number of columns of the billboard.
The next $n$ lines will contain $m$ integers separated by space, each integer representing the initial state of a bulb, $1$ if the bulb is on, and $0$ if it is off.

# Output data

The output file `becuri.out` will contain a single line which will print an integer representing the minimum number of switch operations to turn off all bulbs, or `-1` if there is no solution for the given initial configuration.

# Constraints and clarifications

* $1 \leq n, m \leq 500$

# Example

`becuri.in`
```
3 3
0 0 1
0 0 1
1 1 0
```

`becuri.out`
```
1
```

## Explanation

We operate the switch in position $(3, 3)$.