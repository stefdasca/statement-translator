```markdown
Let a natural number `N` and a room of length `2 * N + 2` be seen as a closed interval `[-N - 1, N + 1]`. In the center `C` of the room `(C = 0)`, there is initially a ballerina named Costelina Salopeta. She is going to perform `T` dance steps of length `1`, making the first step to the right. In the `2 * N` distinct points of integer coordinates inside the room, `K` obstacles can be placed. When the ballerina reaches a point with an obstacle, she stumbles and makes a pirouette. Thus, she changes her direction of movement, and the obstacle from that point disappears.

~[image.png]

Obstacles cannot be placed at the points of coordinates `-N - 1`, `0`, and `N + 1`. The walls of the room at coordinates `-N - 1` and `N + 1` are considered permanent obstacles that will not disappear upon contact, and the point of coordinate `C = 0` represents Costelina's initial position.

# Task
Given the values of `T, N`, and `K`, calculate in how many ways the `K` obstacles can be placed such that after a complete performance of `T` steps, Costelina returns to the starting point `C`.

# Input data
The file `piruete.in` contains on the first line the natural numbers `T, N`, and `K` separated by a space, with the significance as described above.

# Output data
The file `piruete.out` will contain on the first line a single natural number representing the answer modulo $10^9 + 7$.

# Constraints and clarifications
* `0 \leq T \leq 200`, `T` is an even number;
* `1 \leq N \leq 100`;
* `0 \leq K \leq 2 * N`;
* Attention! The answer must be given modulo $10^9 + 7$;
* For `10%` of the tests we have `N \leq 10`;
* For `30%` of the tests we have `N \leq 30`;
* For `70%` of the tests we have `T \leq 2 * N + 2`;

# Example:
`piruete.in`
```
6 3 4
```
`piruete.out`
```
7
```

Explanation
---
The ballerina will perform `T = 6` steps in a room of length `2 * N + 2 = 2 * 3 + 2 = 8`, `K = 4` obstacles are placed.

There are `7` ways to place the obstacles:
1. `[.x.Cxxx]`
2. `[.xxC.xx]`
3. `[x.xC.xx]`
4. `[xx.Cx.x]`
5. `[xx.Cxx.]`
6. `[xxxC.x.]`
7. `[xxxC..x]`

The position of a free space is denoted by `.`, and the position of an obstacle by `x`.
```