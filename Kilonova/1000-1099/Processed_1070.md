Here is the translated problem statement in English:

---

Mihai and Maria, while heading to kindergarten, noticed that they often meet in the morning. The children do not attend the same kindergarten and do not live nearby to leave together. After meeting again this morning, they decided to establish, for each of them, a path from home to kindergarten, such that the paths intersect and the scenery they can admire on their way is as beautiful as possible. Additionally, neither of them accepts any detours. The village where the two children live can be represented using an array with $L$ rows (numbered from $1$ to $L$) and $C$ columns (numbered from $1$ to $C$). Thus, each position in the village is given by $2$ coordinates $(i, j)$, representing, in order, the row and column of the respective position.

Mihai's house is at the coordinates $(1, 1)$, and his kindergarten is at the coordinates $(L, C)$. Maria's house is at the coordinates $(L, 1)$, and her kindergarten is at the coordinates $(1, C)$. Each child can take a step from the current position to any of the $4$ neighboring positions by row or by column (without leaving the village). Each position in the array is associated with a natural value representing the "beauty coefficient of the scenery visible from that position." To determine the beauty coefficient of a path, the values from all the positions through which the path passes are summed.

# Task

Determine the "maximum beauty coefficient" that can be obtained for two paths that meet the following conditions:

* They intersect exactly once, meaning they have at least one common position in the array (after intersecting, the paths may continue on common positions, but once they separate, they should not intersect again);
* Each child's path must have the minimum number of steps between their house and their kindergarten;
* The number of positions through which the path passes from each house to the meeting point can be different (the first of the children to reach the meeting point will wait for the other, the value from this position being counted only once);
* The sum of the positions’ values in the array for the two paths must be maximum (the values of the common positions for the two paths are added twice).

Also, determine the position where the two meet.

# Input data

The input file `poteci.in` contains on the first line the two natural numbers $L$ and $C$, separated by a single space. Each of the following $L$ lines contains $C$ natural numbers separated by a space, representing the beauty coefficient of the scenery that can be admired from the respective position.

# Output data

The output file `poteci.out` will contain on the first line a natural number representing the "maximum beauty coefficient." The second line will contain two natural numbers $x$ and $y$, separated by a single space, representing the row and column of the position where their paths intersect. If there are multiple such positions, the position with the minimum row value is chosen. If there is still a tie, the position with the minimum column value is chosen.

# Constraints and clarifications

* $1 \leq L, C \leq 1 \ 000$
* The values in the array are natural numbers less than or equal to $10 \ 000$
* A child's path cannot pass through the house or kindergarten of the other.
* $30\%$ of the score is awarded for correctly determining the first task.

# Example

`poteci.in`
```
3 4
1 0 0 0
1 1 1 1
1 2 2 1
```

`poteci.out`
```
15
3 2
```

## Explanation

Mihai's path can pass through the positions, in this order: $(1, 1)$, $(2, 1)$, $(2, 2)$, $(3, 2)$, $(3, 3)$, $(3, 4)$. 

Maria's path can pass through the positions: $(3, 1)$, $(3, 2)$, $(3, 3)$, $(2, 3)$, $(2, 4)$, $(1, 4)$.