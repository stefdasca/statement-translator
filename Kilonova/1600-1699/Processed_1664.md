Victor has many wooden cubes at his disposal, all of the same size, each colored with one of the colors $0, 1, 2, ..., 9$. He invented a game in the form of an algorithm:
* *Step 0* - The variable $X$ is initialized to zero.
* *Step 1* - A random number of cubes are chosen and a sequence is formed with them. The cubes in the sequence are glued to each other.
* *Step 2* - If all the cubes in the sequence have the same color, the value of the variable $X$ is displayed and the game stops. Otherwise, proceed to step $3$.
* *Step 3* - A color $C$ is chosen and then all the cubes of color $C$ are removed from the sequence. The places of the removed cubes remain temporarily empty.
* *Step 4* - Any cube in the sequence will be moved to its left as long as the adjacent positions are empty. $X$ is incremented by $1$ for each move by one position. The movement operations end when no more left moves can be made. Then return to step $2$.

# Task

Consider a sequence with at least two elements representing the colors of the cubes in the sequence. It is required to calculate the maximum value that $X$ can have.

# Input data

The input file `easydel.in` contains the given sequence on the first line. The digits in the sequence are written without spaces between them.

# Output data

The output file `easydel.out` will contain a single number representing the maximum value that $X$ can have.

# Constraints and clarifications

* The maximum length of the color sequence is $20\ 000$

# Example

`easydel.in`
```
12132131123221
```

`easydel.out`
```
37
```

## Explanation

All cubes of color $1$ are removed. The remaining sequence is `_2_32_3__2322_`. The number of left moves will be $1 + 2 + 2 + 3 + 5 + 5 + 5 + 5$, so $X$ will increase by $28$. The sequence becomes `23232322`.
If cubes of color $3$ are then removed, the remaining sequence will be `2_2_2_22`. The number of left moves will be $1 + 2 + 3 + 3$, so $X$ will increase by $9$. The sequence will become `22222` and the game will stop. The value of $X$ will be $37$.
If cubes of color $2$ are removed first, the sequence `1_13_1311_3__1` will be obtained. $X$ will increase by $18$. The sequence will become `113131131` and $X$ could increase by at most $10$.
If cubes of color $3$ are removed first, the sequence `121_21_112_221` will be obtained, and $X$ will increase by $17$. The sequence will become `12121112221`, and $X$ could increase by at most $18$.