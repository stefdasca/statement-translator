# Task
A family of possums has a den with $N$ levels and $\frac{N \cdot (N + 1)}{2}$ rooms arranged in a triangular matrix with $N$ rows. Each room can house only one possum. The den was dug into the ground by the possums, and level $1$ (the uppermost level) is closest to the surface. Each level $I$ contains $I$ rooms. If $I < J$, then level $I$ is positioned higher than level $J$, meaning level $I$ is closer to the surface than level $J$. The possum family has exactly $\frac{N \cdot (N + 1)}{2}$ members with ages between $1$ and $\frac{N \cdot (N + 1)}{2}$, with distinct ages. The basic rule in the possum family's den is as follows: In the room located at row $I$ and column $J$, a younger possum than those in rooms $(I + 1, J)$ and $(I + 1, J + 1)$ must reside. A possum of age $X$ is considered younger than a possum of age $Y$ if $X < Y$. Each possum wants to know the highest level it can be positioned on. Unfortunately, they do not have the paws made for programming, so the possum family members ask for your help.

# Task
Given the natural number $N$, they ask you to answer two questions:
1. For each possum, find the highest level (closest to the surface) it can be located on while respecting the age rules;
2. For a given possum of age $K$, display the matrix so that the possum is placed in a room on the highest level possible while respecting the age rules.

# Input data
The first line of the input file `oposumi.in` contains the number $T$ which can have the value $1$ or $2$ such that:
- If $T$ has the value $1$, then solve request $1$, and the following will be the natural number $N$ representing the number of levels in the den;
- If $T$ has the value $2$, then solve request $2$, and the following will be the natural number $N$ representing the number of levels in the den, followed by the natural number $K$ representing the age of the possum that wishes to be positioned on the highest level possible.

# Output data
In the output file `oposumi.out`:
- For $T = 1$, print a sequence of $\frac{N \cdot (N + 1)}{2}$ numbers, where the $I$-th number represents the highest level on which the possum of age $I$ can be.
- For $T = 2$, print $N$ rows, representing the way the possums are arranged in the den according to age, so that the possum of age $K$ is positioned on the highest level possible. On row $I$, print $I$ numbers separated by a space representing the ages of the possums arranged on level $I$.

# Constraints and clarifications
- $1 \le N \le 1\ 000$;
- $1 \le K \le \frac{N \cdot (N + 1)}{2}$;
- For the task $T = 2$, the solution is not unique. Any correct solution is accepted;
- Tests are not grouped.

# Example 1
`oposumi.in`
```
1 3
```
`oposumi.out`
```
1 2 2 2 3 3
```

## Explanation
The highest level at which a possum can reside is:
- The possum of age $1$ can reside on level $1$.
- Each possum of age $2$, $3$ or $4$ can reside on level $2$.
- Possums of age $5$ or $6$ will reside on level $3$. 

# Example 2
`oposumi.in`
```
2 4 7
```
`oposumi.out`
```
1
2 3
4 5 7
6 8 10 9
```

## Explanation
The highest level where the possum of age $K = 7$ years can reside is level $3$, and one possible arrangement of the possums in the rooms is shown above.