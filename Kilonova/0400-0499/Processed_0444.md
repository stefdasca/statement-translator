```markdown
You have just downloaded the latest version of the well-known game Plants vs. Zombies. The game is played on an infinite 2D field where multiple zombies will appear. Each zombie has a starting position $(s_x, s_y)$ where it appears, a speed of `v` units/second, and a string of exactly `15` moves that it will make. A move is encoded by a character from the set `{U, R, D, L}` ("up", "right", "down", "left").

Zombies will perform the moves sequentially, starting from the first move. Each zombie will move in the direction indicated by the current move for exactly one second, after which it will proceed to the next move. For instance, if a zombie has a speed of `3`, starts at the position `(2, 4)`, and the first move is `U`, it will make the moves `(2, 4) → (2, 5) → (2, 6) → (2, 7)` in one second, after which it will proceed to the next move. For more information, see the explanations.

If a zombie exhausts its initial string of moves, it will continue with the move string from the beginning, so they will cycle through the set of moves infinitely. In their movement, two zombies can occupy the same position at the same time without interfering with each other.

Our goal is to neutralize the zombies by placing **laser plants** (*Laser Beans*). A plant will be placed at the position $(l_x, l_y)$ and will be set in one of the four directions `{U, R, D, L}`. The plants will neutralize everything that lies in their direction. For example, a plant at position `(2, 5)` directed towards `U` will neutralize everything located at positions `(2, 5), (2, 6), (2, 7), (2, 8), (2, 9), ...`. It is noted that a zombie will be neutralized even at the moment it reaches the position of the plant.

What is the minimum number of laser plants that need to be placed so that each zombie is neutralized at some point during the game?

# Task
You will implement the function with the following header:
```cpp
std::vector<Plant> minimum_plants(std::vector<Zombie> zombies);
```
The data structures used for the interaction are described in the file `zombies.h` and have the following description:
```cpp
struct Zombie { int sx, sy, v; string moves; };
struct Plant { int lx, ly; char dir; };
```
The function minimum_plants will be called once, with the parameters having the specifications from the statement. **It is guaranteed that the move string of each zombie has a length of exactly `15`.**

For the returned solution to be valid, the number of laser plants returned must be the minimum possible and the plants must neutralize all zombies. Also, the plants must be placed in distinct positions, and the coordinates $l_x$ and $l_y$ must be integers between $−10^9$ and $10^9$ inclusive.

# Constraints and clarifications
## Subtask 1 (17 points)
* The number of zombies is between `1` and `100`
* For each zombie:
  * $−300 \leq s_x, s_y \leq 300$
  * `1 \leq v \leq 300`
## Subtask 2 (34 points)
* The number of zombies is between `1` and `2,000`
* For each zombie:
  * $−10^5 \leq s_x, s_y \leq 10^5$
  * $1 \leq v \leq 10^5$
## Subtask 3 (21 points)
* The number of zombies is between `1` and `20,000`
* For each zombie:
  * $−10^6 \leq s_x, s_y \leq 10^6$
  * $1 \leq v \leq 10^6$
## Subtask 4 (28 points)
* The number of zombies is between `1` and `50,000`
* For each zombie:
  * $−10^6 \leq s_x, s_y \leq 10^6$
  * $1 \leq v \leq 10^6$
  
# Model grader
The grader will read from the console the input data in the following format:
* line `1`: `N`, representing the number of zombies
* line `1 + i` `(1 \leq i \leq N)`: $s_x \ s_y \ v \ moves$ (separated by a space)
The grader will display on the console your answer in the following format:
* line `1`: `K`, representing the number of lasers
* line `1 + i` `(1 \leq i \leq K)`: $l_x \ l_y \ dir$ (separated by a space)

# Examples
`stdin`
```
3
0 0 3 URURURURURURURU
10 5 1 LLLLLDDDRRRRRRR
15 0 2 UUUUUUUUUUUUUUU
```
`stdout`
```
1
-2 1 R
```
`stdin`
```
2
10 10 1 UUUUUUUUUUUUUUU
-1 -1 1 DDDDDDDDDDDDDDD
```
`stdout`
```
2
-1 11 R
-1 12 D
```
Explanation
---
This is the figure for the first example:
~[Enunt_Zombies.jpg]
```