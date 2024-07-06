```markdown
After discovering the ruins of a medieval fortress, archaeologists decided to restore it, starting with the main wall. This wall is made up of $N$ pillars, each with a width of $1$ meter, placed one next to the other (adjacent). The height of each pillar in meters is known, but unfortunately, not all of them are now at the same level. For the restoration of the wall, the archaeologists have bricks that have a width of $1$ meter and variable lengths, expressed in meters. An unlimited number of bricks of any length are available. We assume that all available bricks and all pillars that make up the wall have the same thickness of $1$ meter.

The restoration consists of two stages:
- In the first stage, all pillars with a height equal to or greater than $H$ are cut down to the height $H$, the others, which are shorter, maintain their initial height;
- In the second stage, all pillars are brought to the same height, filling the gaps between them with bricks, such that the wall becomes compact; for unknown reasons, the archaeologists will place the bricks "lying down", each occupying, possibly, the space above multiple pillars.

The archaeologists analyzed the situation, **independently**, for $Q$ possible values of $H$.

# Task
For each of the $Q$ values chosen for the height $H$, determine the minimum number of bricks required to restore the wall, independently, starting from the initial heights of the pillars.

# Input data
The file `restaurare.in` contains:
- The first line contains the number $N$ of pillars;
- The second line contains $N$ natural numbers, separated by spaces, representing the initial heights of the pillars, in order, from left to right;
- The third line contains the natural number $Q$, representing the number of possible values for the height $H$;
- The fourth line contains $Q$ natural numbers, separated by spaces, representing the possible values of $H$.

# Output data
The file `restaurare.out` contains $Q$ numbers, one on each line, representing the minimum number of bricks required to restore the wall for each of the heights $H$, in the order they appear in the input file.

# Constraints and clarifications
- $1 \le N, Q \le 100\ 000$;
- The height of each pillar is a natural number in the range $[1, 100\ 000]$;
- $1 \le H \le \text{maximum value among the initial heights of the pillars}$;
- For $35\%$ of the test cases $N \le 1\ 000$, and for another $40\%$ of the test cases $Q=1$.

# Example
`restaurare.in`
```
5
4 3 2 4 2
3
1 4 3
```
`restaurare.out`
```
0
4
2
```

## Explanation
The initial shape of the wall:
~[restaurare1.png]

For $H=1$ all pillars have the same height, so no brick is needed. For $H=4$, $4$ bricks are needed, with the wall having the following structure after restoration:
~[restaurare2.png]

For $H=3$, $2$ bricks are needed, with the wall having the following structure after restoration:
~[restaurare3.png]
```