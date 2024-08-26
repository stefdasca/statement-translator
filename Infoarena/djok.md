## Task

Tanaka has started playing a new game. In this game, there are $N$ little monsters (such as the fantastic beetle, the fierce mouse, the tall condor). Each monster is characterized by a bravery score, and each monster is found in an arena (such as the info arena, or the arena of arenas); the arenas are connected by paths. These form a tree if the paths are considered to be edges and the arenas nodes. The game proceeds as follows: Tanaka chooses an initial arena and controls the monster in that arena. Tanaka can now move through the paths, having battles with the monsters in the arenas he reaches. He can defeat only monsters whose bravery is at most $K$ units higher than his. After any victorious battle, his bravery either remains the same if the defeated monster is not stronger than the controlled monster, or it increases to the bravery of the defeated monster. For each initial monster, state the maximum number of monsters Tanaka can defeat.

## Input data

The input file `djok.in` will contain, on the first line, the numbers $N$ and $K$. On the second line, there will be $N$ numbers, the braveries of the monsters, in order. On the following $N-1$ lines, pairs $a$ $b$ of indices will follow, representing a path between arenas $a$ and $b$.

## Output data

The output file `djok.out` will contain $N$ numbers, the results for the $N$ nodes. 

## Constraints and clarifications

$$1 \leq N \leq 150\ 000$$ 
$$1 \leq K, \text{any bravery} \leq 1\ 000\ 000\ 000$$ 
For 10 points, $N \leq 100$ 
For another 20 points, $N \leq 1\ 000$ 
For another 45 points, $N \leq 70\ 000$ 
The monster controlled by Tanaka is also considered defeated 
Tanaka must have a battle with the monster in an arena the first time he passes through that arena. He cannot pass through an arena if he cannot defeat the corresponding monster. 

## Example

`djok.in` 
```
5 1 
1 2 4 5 6 
1 2 
2 3 
3 4 
4 5 
```

`djok.out`
```
2 2 5 5 5 
3 13 7 20 14 
14 4 3 5 2 4 5 2 1 4 1 5 4 4 
```