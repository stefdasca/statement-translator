# Grendizer

Grendizer, the robot from the animated series watched by Algorel, has a new weapon. This weapon works as follows: Grendizer sets a detonation point and an effective radius $r$; all targets at exactly the Manhattan distance $r$ from the detonation point will be hit. Algorel has cataloged the $N$ targets that Grendizer needs to destroy in one of the episodes. Now he wonders: if Grendizer were to detonate the weapon at point $(x, y)$ with an effective radius $r$, how many of the targets would be hit? I think you already know who needs to solve the problem instead of the pesky Algorel - who can't remember any algorithms due to watching cartoons.

## Task

## Input data

The input file `grendizer.in` contains on the first line two natural numbers, $N$ and $M$, representing the number of targets and the number of questions for which Algorel wants to find the answer.
The next $N$ lines each contain two integers representing the coordinates of a target. The following $M$ lines describe a question through three numbers separated by spaces: $x\ y\ r$ having the meaning described above.

## Output data

In the output file `grendizer.out` you will print on each line the answer for each of the $M$ questions.

## Constraints and clarifications

Targets can overlap

The Manhattan distance between two points $(x_1,\ y_1)$ and $(x_2,\ y_2)$ is $|x_1 - x_2| + |y_1 - y_2|$

Effective radii are natural numbers in the interval $[1,\ 10^9]$

The coordinates of the targets and launch points will be integers in the interval $[-MAX\_MOD,\ +MAX\_MOD]$

The following table specifies the values for $N$, $M$ and $MAX\_MOD$ for each test:

| Test | Values           |
|------|------------------|
| 1    | 8 4 10           |
| 2    | 500 500 100      |
| 3    | 20\ 000 20\ 000 300 |
| 4    | 30\ 000 30\ 000 300|
| 5    | 40\ 000 40\ 000 300|
| 6    | 50\ 000 50\ 000 10^5|
| 7    | 60\ 000 60\ 000 10^5|
| 8    | 70\ 000 70\ 000 10^5|
| 9    | 90\ 000 90\ 000 10^5|
| 10   | 10 5 10^8        |

## Example

`grendizer.in`

```
8 4
2 0
1 -1
0 -2
-1 -1
-2 0
-1 1
0 2
1 1
0 0 2
1 1 1
2 -1 1
0 0 1000000000
```

`grendizer.out`

```
8
4
3
0
```