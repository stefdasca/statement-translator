## Task

Some of you might know the game Sokoban. The game is played on a matrix with $N$ rows and $M$ columns. Some cells are free (denoted by '.'), while others are blocked (denoted by '#'). Exactly one cell (denoted by 'S') is occupied by the player. Exactly one cell (denoted by 'X') is occupied by a box. Exactly one cell (denoted by 'E') is designated as the destination cell. The player's goal is to push the box to the destination cell. The player can push the box in a certain direction if they are in an adjacent cell to the box (in the 4 directions $NSWE$) and their position relative to the box is opposite to the direction they wish to push the box. For example, if the player is directly to the left of the box, they can push it to the right. In order for the movement to be possible, the cell into which the box is pushed must be free. Additionally, the player can only access free cells. The box is solid, and the player cannot pass through a cell if it is occupied by the box. The player can pass over the starting or destination cells. Given an instance of the game, you must decide if it has a solution, i.e., if it is possible for the player to push the box from its starting position to the destination cell.

## Input data

The input file `sokoban.in` will contain on its first line the number of tests, $T$. Each test follows the structure below:
the first line contains the values $N$ and $M$, representing the number of rows and columns of the matrix, respectively. The next $N$ rows contain $M$ characters each, which can be '.', '#', 'X', 'S', or 'E'.

## Output data

The output file `sokoban.out` will contain $T$ lines, each containing the word $YES$ or $NO$.

## Constraints and clarifications

The sum of $max(N, M)$ for each test is less than or equal to $2000$.

## Example

`sokoban.in`
```
1
10 12
.##########.
.#........#.
.#..X..S..##
.#.#..####.#
.###..E....#
##.#....#.##
#..##.###.##
#.........##
#..#..##...#
############
```

`sokoban.out`
```
YES
```