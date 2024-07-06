Gigi has a palace with `T` floors, which is quite monotonous in design. Each floor contains a network of `N x M` square rooms, with `M` rooms on each of the `N` lines (numbered from `1`). Each room contains a light bulb that can initially be on or off. On the occasion of Easter holidays, Gigi wants to light up all the bulbs in his palace using an app where he can change the state of the bulbs for each room (from off to on and vice versa). On the screen, he can view all the rooms on a single floor. Unfortunately, when Gigi makes a move and wants to press in the right of a room, he will also press in the right of the adjacent rooms (top and bottom, as well as left and right, if the rooms exist, but not diagonally).

Not knowing how he can proceed, he will ask for your help and promises to reward you with dairy products. Gigi appreciates different ways of solving the problem, but does not appreciate redundancy. A sequence of moves `X` that lights up all the bulbs is considered *valid* if and only if there is no other sequence `Y` that also lights up the bulbs, with `Y \subset X`.

Since Gigi suspects that he will find himself in this situation again, find out the number of possible ways to light up each floor in the palace and display a *valid* way to illuminate each floor (if possible).

# Input data
The first line contains the numbers `N`, `M`, `T`. Then, for each floor, the initial state of the bulbs is read on the next `N` lines, `M` on each line (`1` - on, `0` - off).

# Output data
The first line will display the total number of ways. If there is no valid way, it will only display `0`. Otherwise, the next lines will display a valid way to light up all the bulbs, on the second line showing the number of moves. Then, on each line, the moves `a b` will be displayed, meaning that a press is made on line `a` and column `b`.

# Constraints and clarifications
* `1 \leq T \leq 10`
* `1 \leq N, M \leq 500 000`
* `30%` of the points are for the number of ways. **Attention**, this number must be printed no matter what, even if it is wrong.
* The remaining `70%` of the points are for a solution that respects the task (if it exists).
## Subtask 1 (40 points)
* `N \cdot M \leq 350`
## Subtask 2 (30 points)
* `N \cdot M \leq 1 000`
## Subtask 3 (10 points)
* `N \cdot M \leq 1 500`
## Subtask 4 (20 points)
* `N \cdot M \leq 500 000`
* **Attention** `N, M \geq 1`

# Example

`stdin`
```
3 5 1
10110
01101
10010
```

`stdout`
```
8
5
2 2
1 4
2 3
1 5
2 5
```

`stdin`
```
4 4 2
1000
0000
0000
0000
0000
0000
0000
0000
```

`stdout`
```
0
16
10
2 1
2 2
2 3
2 4
3 1
3 4
4 1
4 2
4 3
4 4
```

Explanations
---

For the second example: it can be demonstrated that there is no way to illuminate the floor with the bulbs in the configuration
```
1000
0000
0000
0000
```
However, there are `16` ways to light up all the bulbs if none are initially on.