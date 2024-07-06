```markdown
# Task

We are given the geography of a place in the form of a $N$ x $N$ matrix. The matrix contains lowercase English letters $a...z$ representing the height of the terrain at a position, $a$ being the valley and $z$ being the mountain.
<br>
We are with a car in an off-road session and want to get from the coordinate $(i_M,j_M)$ to a target at coordinates $(i_T,j_T)$.
<br>
The car can move from one cell to any other cell that shares a common side, but we must consider that we can change the height at which we are at most once, otherwise the car breaks down from drops (or climbs).
<br>
In how many ways can we choose the values of $i_M,j_M,i_T,j_T$ such that we can reach the target (to have a successful session)?

# Input data

The first line contains $N$ and subsequently, the terrain will be given.

# Output data

The number of ways we can have a successful session.

# Constraints and clarifications

* $1 \leq N \leq 1000$
* The starting position must be different from the target position
* For 20p $1 \leq N \leq 50$

# Example 1

`stdin`
```
3
aab
abc
ccc
```

`stdout`
```
70
```

## Explanation

If we place the car at position $(1,1)$ we can place the target anywhere and we will be able to reach it by changing the height at most once.
If we place the car at position $(1,3)$ however, we will only be able to place the target in $7$ positions.

# Example 2

`stdin`
```
5
aabcb
abbcb
aabbb
ccccc
abbcd
```

`stdout`
```
430
```
```