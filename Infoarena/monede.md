# Coins

The vault of the Romanian bank consists of $N$ rows with $M$ drawers of equal sizes arranged side by side. In the morning, when the bank opens, all drawers are closed. During the day, the bank will receive money (coins), and bank employees will place the coins in random drawers. At the end of the day, a robot must rearrange the coins so that all the open drawers contain the same number of coins. He will not consider the closed drawers. The robot moves only horizontally or vertically. The effort made by the robot to move $P$ coins is equal to $P*nr$, where $nr$ is the number of drawers the robot passes through.

## Task

Write a program to find the minimum effort made by the robot to rearrange the coins. The existence of a solution is guaranteed.

## Input data

The first line of the input file `monede.in` contains the natural numbers $N$ $M$ separated by a single space. The next $N$ lines contain $M$ numbers separated by spaces representing the number of coins in the drawers. If the number of coins is $0$ it means that the drawer is closed and will not be considered by the robot.

## Output data

The first line of the output file `monede.out` will contain the required minimum effort.

## Constraints and clarifications

$2 \leq N, M \leq 127$

$2 \leq$ number of open drawers $\leq 127$

$1 \leq$ number of coins in a drawer $\leq 1023$

## Example

`monede.in`
```
5 4
2 4 0 1
0 0 0 0
4 0 0 0
0 0 0 0
0 1 0 6
```

`monede.out`
```
17
```