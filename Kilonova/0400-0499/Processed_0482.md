The main character from the novella "At the Gypsies", Omeskoku, is trapped in a monstrous cave (there really are monsters in the cave!). He has access to a satellite that can give him a map of the cave. The cave is in the form of a labyrinth. The cave is monstrous, so in some areas of the cave there are monsters.

The monsters are quite friendly, though, so Omeskok plays a game with them. At each step, Omeskok and the monsters can choose whether to move or stay put, and all movements are made simultaneously. The monsters, like Omeskok, if they choose to move, can move one unit in any of the 4 cardinal directions (North, East, South, West). The game has a twist: If the monsters manage to catch Omeskok, they will feast well :).

If Omeskok manages to save himself and escape from the labyrinth, he gains the right to live while the monsters will starve. Omeskok, however, notices the immense number of monsters in the cave, so it is very unlikely that he can escape. His very advanced satellite can also launch lasers that can neutralize the monsters, but he wants to neutralize as few as possible so that they don't catch on (if they catch on, they no longer want to play and can eat Omeskok very easily).

# Task

What is the minimum number of monsters that need to be neutralized?

# Input data

You will read the values $n$ and $m$ representing the size of the cave. The cave is read in the form of a matrix of $n$ rows and $m$ columns.
The components of the cave will be represented by the following symbols:
- `#` represents an obstacle that neither the monsters nor Omeskok can pass;
- `.` represents an accessible parcel for both the monsters and Omeskok;
- `M` represents a monster.

# Output data

You will print a single number representing the minimum number of monsters that need to be eliminated so that Omeskok can reach the exit.

# Constraints and clarifications

- $1 \le n,m \le 1000$
- Omeskok will always start from the top-left corner of the matrix and the exit of the cave will always be in the bottom-right corner of the cave;
- The given portion of the cave is surrounded by obstacles (you cannot exit the given terrain);
- If Omeskok cannot escape from the cave, but neither can the monsters catch him without letting him escape, then this is considered a victory for the monsters, because Omeskok's goal is not merely to avoid being eaten but to escape without being eaten!
- Omeskok will always have at least one route through which he can escape;
- There can be multiple monsters on the same parcel, but initially, there will be just one;
- Omeskok is eaten if he reaches the same parcel as a monster;
- If Omeskok reaches the exit at the same time as a monster, he will still be eaten because it takes time to climb the ladder;
- The monsters play optimally;
- The matrix can contain other characters, but they will be considered free decorative portions.

# Example 1

`stdin`

```
5 5
...M.
.###.
M..#.
.....
...#.
```

`stdout`

```
2
```

# Example 2

`stdin`

```
6 6
......
.##.#.
....#.
M#M.#.
.####.
.#....
```

`stdout`

```
0
