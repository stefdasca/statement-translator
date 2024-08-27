Barbarian

Paftenie the Barbarian is a famous adventurer. He has led wars, discovered treasures, conquered fortresses, and the hearts of maidens. However, this time he was captured by his most feared enemies and thrown into a dungeon. The dungeon is actually a grid of size $R \times C$. Some cells have dragons, some are occupied by walls, and others are free. Paftenie needs to escape the dungeon by moving only through free cells (a cell has a maximum of 4 neighbors), and he must stay as far away as possible from the fierce dragons whose flames can damage his attire (so that the minimum distance to the nearest dragon from each of the cells on his path is maximized).

## Task

Help Paftenie the Barbarian to escape the dungeon by determining a path such that the minimum distance to the nearest dragon from each of the cells on his path is maximized!

## Input data

The input file `barbar.in` contains on the first line two integers $R$ and $C$, representing the number of rows and columns of the dungeon, respectively. The next $R$ lines contain $C$ characters each, not separated by spaces, with the following meanings:
- . free cell
- * wall
- $D$ dragon
- $I$ Paftenie's starting point
- $O$ exit from the dungeon

## Output data

The output file `barbar.out` will contain on the first line a single number, representing the maximum value of the minimum distance to the nearest dragon from each of the cells on the path. If there is no solution, print $-1$.

## Constraints and clarifications

$1 \leq R, C \leq 1\ 000$

It is guaranteed that there is at least one dragon in the dungeon.

## Example

### barbar.in
```
10 10
..........
.I....D...
..........
..D...D...
.*........
D*........
*...D.....
..****....
...O......
..........
```
### barbar.out
```
2
```

## Explanation

One possible solution:
```
..........
.I ooo .D...
.... o .....
..D. o .D...
.*.. oo ....
D*... ooooo
* ...D.... o
..****... o
...O oooooo
.......... 
```