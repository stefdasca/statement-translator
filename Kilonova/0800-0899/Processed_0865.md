Alex got a summer job as a bartender. Because he likes to turn working at the bar into a show, sometimes he arranges multiple identical glasses in terms of shape and size, but with different capacities, in the form of a stack.

~[0.png|align=right|width=30em]
A glass from the stack, except for those at the base, rests on exactly two glasses from the row below. The glasses are numbered as in the adjacent image. The levels in the stack are also numbered, starting with $1$ from the top, meaning glass $1$ is on level $1$, glasses $2$ and $3$ are on level $2$, glasses $4$, $5$, and $6$ are on level $3$, and so on.

Alex pours one milliliter of water (a drop) into glass number $1$ every second. The glasses have a peculiar property when they are full: the first milliliter that arrives in a full glass will instantly drain into the glass immediately to its left on the row below, the next milliliter will drain instantly into the glass immediately to its right on the row below, and so on, alternatively one drop into each of the two glasses.

For example, when glass $2$ is full, the first milliliter to arrive will drain into glass $4$, the next milliliter will drain into glass $5$, the third milliliter will drain again into glass $4$, and so on.

When a new milliliter of water arrives in a full glass at the base of the stack, it will instantly drain onto the table.

# Task
Knowing the number of glasses in the row at the base of the stack and the fact that the stack is complete (all rows contain the maximum number of glasses that can be arranged according to the above rule, and on the topmost row there is only one glass), write a program that determines:
1. What is the minimum level (the highest) that has the maximum sum of the capacities of all the glasses on the level?
2. What is the minimum number of seconds needed to fill all the glasses using the described process and how many milliliters of water are wasted (drain onto the table) in this case?

# Input data
The first line of the input file `pic.in` contains a natural number $V$ which can only have the value $1$ or $2$.

The second line of the input file contains a single natural number $N$ representing the number of glasses in the row at the base of the stack.

The third line of the input file contains $M = \\frac{N \\cdot (N+1)}{2}$ natural numbers $C_1, C_2, \\dots, C_M$ separated by a space, $C_i$ representing the capacity (in milliliters) of the glass numbered $i$ in the stack.

# Output data
If the value of $V$ is $1$ then the output file `pic.out` will contain on the first line a single natural number representing the order number of the minimum level (the highest) that has the maximum sum of the capacities of all the glasses on the level.
If the value of $V$ is $2$ then the output file will contain on the first line two natural numbers separated by a single space representing the minimum number of seconds elapsed until all the glasses in the stack are full and respectively the number of milliliters of water wasted (that drained onto the table) at that moment.

# Constraints and clarifications
- $2 \\leq N \\leq 50$
- $20\\%$ of the tests will have the value $V = 1$, and $80\\%$ of the tests will have the value $V = 2$.
- $35\\%$ of the tests will have $N \\leq 17$, and $65\\%$ of the tests will have $N > 17$.
- $1 \\leq C_i \\leq 25$, for any $1 \\leq i \\leq M$.

# Example 1
`pic.in`
```
1
3
2 4 2 1 2 3
```
`pic.out`
```
2
```
## Explanation
$V = 1$, so ONLY the first task is solved.

On level $1$ there is one glass with a capacity of $2$. On level $2$ there are two glasses with capacities $4$ and $2$. On level $3$ there are three glasses with capacities $1$, $2$, and $3$.

The sum of the capacities of the glasses is: $2$ on level $1$, $6$ on level $2$, and $6$ on level $3$, so the highest level with the maximum sum ($6$) is level $2$.

# Example 2
`pic.in`
```
2
3
2 4 2 1 2 3
```
`pic.out`
```
18 4
```
## Explanation
$V = 2$, so ONLY the second task is solved.

After $10$ seconds the configuration of the glasses is as follows:
|Glass|Number of drops|Comments
-|-|-
|1| 2| Full
|2| 4| Full
|3| 2| Full
|4| 0|
|5| 1|
|6| 1|

The eleventh drop drains from glass $1$ to glass $2$ and further to glass $4$. The next drop drains from glass $1$ to glass $3$ and further to glass $5$ which becomes full, and so on.

After $18$ seconds all glasses are full, and from glass $1$ one drop was wasted, from glass $2$ three drops were wasted, and from glass $3$ no drops were wasted, so a total of $4$ drops were wasted.