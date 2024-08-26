## Task

Two friends are playing a game on an infinite square grid divided into unit squares. The game proceeds as follows: the first player is placed on an arbitrary square, and the other player gives a non-zero natural number $N$. The player on the board must return to the initial position by first making a step vertically (up or down), then two steps horizontally (left or right), three steps vertically (up or down), $\dots$, until reaching $N$ steps in a single round. Unfortunately, not all games can be completed, and the player on the board does not want to make futile attempts. Since the player is not very good at finding the path, he asks you to help him find a good path or to tell the other player if this is impossible.

## Input data

The input file cardinal.in contains on the first line a non-zero natural number $Q$, representing the number of games played. Each of the following $Q$ lines contains a number $N$ as described in the statement.

## Output data

The output file cardinal.out must contain the answers for the $Q$ games, each on a separate line. If the $i$-th game can be completed, then line $i$ will contain a sequence of letters from the set $\{U, D, L, R\}$, each letter indicating a move of the player up, down, left, or right, respectively. Otherwise, line $i$ will contain the word `IMPOSIBIL`.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 100000.  
1 $\leq$ $Q$ $\leq$ 10.  

For test values worth 10 points $N$ $\leq$ 10.  
The problem will be evaluated on tests worth 90 points.

## Example

cardinal.in  

```
2  
8  
3  
```

cardinal.out  

```
URDLDLUR  
IMPOSIBIL  
```

## Explanation

In the first game, the following sequence of moves brings the player to the cell from which they started:

- 1 step up  
- 2 steps to the right  
- 3 steps down  
- 4 steps to the left  
- 5 steps down  
- 6 steps to the left  
- 7 steps up  
- 8 steps to the right  

In the second game, it is impossible for the player to return to the initial cell after 3 moves.