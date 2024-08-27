# Robot4

On a circle there are $N$ positions, consecutively placed and marked with $1, 2, 3, \dots, N$. The distances between any two neighboring positions are equal to one step. A robot is initially positioned at $1$. At one of the positions, there is a depot with the amount $X$ of energy, from which the robot can recharge. The robot can move on the circle only in the clockwise direction. The robot can store a maximum of $W$ energy units, and initially, it is fully charged. For each step, the robot consumes one energy unit.

## Task

1) Given the number of positions $N$, the initial energy of the robot $W$, the position $P$ of the depot, and the amount $X$ of energy initially in the depot, determine the number of steps the robot can take.

2) Given the number of positions $N$, the initial energy of the robot $W$, and the amount $X$ of energy initially in the depot, determine and print the maximum number of steps the robot can take and the smallest position, conveniently chosen, where the depot can be placed to achieve the maximum number of steps.

## Input data

The first line of the text file `robot4.in` contains the natural number $C$ representing the task. If $C=1$, then the second line contains the natural numbers $N$, $W$, $X$, and $P$ separated by spaces. If $C=2$, then the second line contains the natural numbers $N$, $W$, and $X$ separated by spaces.

## Output data

If $C=1$, then the output file `robot4.out` will contain a natural number representing the number of steps the robot can take. If $C=2$, then the output file `robot4.out` will contain two natural numbers separated by a space representing the maximum number of steps the robot can take and the smallest position of the depot, conveniently chosen to achieve the maximum number of steps.

## Constraints and clarifications

When the robot reaches the depot, it recharges with the maximum possible energy, and the amount of energy in the depot decreases accordingly

$2 \leq N \leq 10000$

$1 \leq W \leq 1000000000$

$1 \leq X \leq 1000000000$

$1 \leq P \leq N$

## Example

`robot4.in`
```
1 
6 
3 
3 
3
```

`robot4.out`
```
5
```

## Explanation

We have task 1, determining how many steps the robot can take. It initially has $3$ energy units and is at position $1$, so it can reach position $3$ in $2$ steps using $2$ energy units. When it reaches position $3$, it has $1$ energy unit left and recharges from the depot with $2$ units, restoring the maximum possible $3$ energy units. It can take $3$ more steps, thus reaching position $6$ with $0$ energy units left, and it stops. In total, it has taken $5$ steps.

`robot4.in`
```
2 
6 
3 
3
```

`robot4.out`
```
6 
4
```

## Explanation

The depot will be placed at position $4$, and the robot will be able to take $6$ steps, which is the maximum.