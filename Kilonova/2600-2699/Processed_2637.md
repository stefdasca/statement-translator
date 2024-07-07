
Robin Hood and Little John decided to determine who is the best archer. To this end, they built $n$ targets arranged in a straight line and numbered from $1$ to $n$. They then established the shooting distance. The two move in front of the targets in a straight line at the agreed distance.

~[rh.png]

They try to hit all $n$ targets with their arrows as follows: Robin starts from target $1$ and moves up to target $n$, then returns to target $1$, and so on. John starts from target $n$ and moves up to target $1$, then returns to target $n$, and so on. Each of the two competitors covers the space between two consecutive targets in one second. Robin shoots once every $p$ seconds, and John shoots once every $q$ seconds, each aiming at the target in front of them. The two can shoot simultaneously at the same target or at a target already hit. The competition ends when each target has been hit at least once.

# Task

1. Determine the time in which the contest ends.
2. Find the targets hit exactly once during the contest.
3. Find the targets hit the most times during the contest.

# Input data

The input file `robinhood.in` contains on the first line a natural number $C$, representing the task. The second line of the input file contains a natural number $n$, representing the number of targets, and the third line contains two natural numbers $p \\ q$, separated by a space, representing the shooting interval of the two archers.

# Output data

If the task is $1$, the output file `robinhood.out` contains on the first line a natural number $t$, representing the time in which the two archers hit all the targets.

If the task is $2$, the first line of the output file will print in ascending order, separated by spaces, the sequence numbers of the targets hit exactly once. If no target was hit exactly once, the value $0$ will be printed.

If the task is $3$, the first line of the output file will contain a natural number representing the maximum number of arrows that hit a target, and on the next line, the sequence numbers of those targets will be printed in ascending order, separated by spaces.

# Constraints and clarifications

* $1 \leq C \leq 3$
* $3 \leq n \leq 10\ 000$
* $1 \leq p, q \leq 500$
* A solution exists for all tests

|#|Score|Constraints|
|-|-|----------|
|1|53|$C = 1$|
|2|21|$C = 2$|
|3|26|$C = 3$|

# Example 1

`robinhood.in`
```
1
5
2 3
```

`robinhood.out`
```
9
```

## Explanation

|time|1|2|3|4|5|target|
|-|-|-|-|-|-|-|
|second 1||r||j||
|second 2|||$\underline{R} \ j$||target 3|
|second 3||$\underline{J}$||r||target 2|
|second 4|j||||$\underline{R}$|target 5|
|second 5||j||r||
|second 6|||$\underline{R} \ \underline{J}$||target 3|
|second 7||r||j||
|second 8|$\underline{R}$||||j|target 1|
|second 9||r||$\underline{J}$||target 4|

Note: uppercase letters indicate the seconds when Robin and John shoot at the target.

# Example 2

`robinhood.in`
```
2
5
2 3
```

`robinhood.out`
```
1 2 4 5
```

## Explanation

The targets that were hit with a single arrow are targets $1\ 2\ 4$ and $5$.

# Example 3

`robinhood.in`
```
3
5
2 3
```

`robinhood.out`
```
3
3
```

## Explanation

Target $3$ was hit $3$ times: twice by Robin and once by John.
