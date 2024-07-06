It is possible that you know the game Bloxorz. If you don't, please watch stage 1 of [this video](https://www.youtube.com/watch?v=ba2BJ1jcVFw&t=25s) to understand the mechanics of this game. In this problem, there are **no** buttons, the possibility of splitting the player into two cubes, or other things that do not appear in stage 1 of the video.

The player is a rectangular parallelepiped of dimensions $2 \times 1 \times 1$. At the beginning, its height is $2$ while its length and width are $1$. To move on the map, the player will rotate in the 4 directions (North, South, East, West). During a rotation, the player's height, length, and width will swap. For example, from the initial state of the player, it can reach a height of $1$, a length of $2$, and a width of $1$.

# Task
You have a two-dimensional map that contains platforms in some positions. The player is only allowed to walk on platforms. Verify if it is possible for the player to reach from the initial platform to the final platform, ending with a height of $2$ and a length and width of $1$. If it is possible, display a correct path that the player can use.

# Input data
The first line contains the numbers $N$ and $M$, representing the dimensions of the map (the number of rows and the number of columns).

The next $N$ lines contain $M$ characters, each representing a piece of the map. The characters can be:
- `_` — This character represents a platform.
- `#` — This character represents that there is nothing there. It means the player is not allowed to walk there.
- `A` — This character represents the initial platform.
- `B` — This character represents the **final** platform.

# Output data
If there is no path, print `NU`.
If there is a path, print `DA` on the first line, and on the second line, a sequence of characters from the set $\{$`N`$,$ `S`$,$ `E`$,$ `V`$\}$ representing the directions the player will take at each step (`N` — North, `S` — South, `E` — East, `V` — West).

# Constraints and clarifications
- $1 \leq N,M \leq 2\ 000$
- **The player must be entirely on platforms. It is not allowed for half of the player to be on a platform while the other half is not.**
- The problem does not necessarily require a path with a minimum number of steps.
- There are no platforms outside the map.
- You will receive $40\%$ of the points of a subtask for correctly displaying only the first message (`DA`/`NU`).

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|10|If a path exists, it consists of only one direction|
|2|70|$N,M \leq 500$|
|3|20|No additional constraints

# Example
`stdin`
```
6 10
___#######
_A____####
_________#
#_________
#####__B__
######___#
```
`stdout`
```
DA
EESEEES
```

## Explanation
**The example is the same as the one in the video, as well as the moves made.**

Solutions like `ESSEESE` or `EESENVSEEESSNVNSVNESEVSSVENVNEESVNESVNESV` are also correct.