## Task

The $N$ members of a special anti-terrorism team have been sent on a mission. The first phase involves moving them to specific positions. Thus, each member has an initial position and must reach a final position, possibly passing through intermediate positions. The main difficulty lies in the fact that in the area there are $P$ soldiers of a terrorist group. These do not move, but can threaten certain positions; a special team soldier cannot pass through a threatened position or a position where a terrorist (alive) is located. The solution could involve eliminating some of the terrorists. If possible, devise a plan to complete the mission.

## Input data

The input file `antitero.in` contains:
- the first line contains $3$ numbers $X$ $N$ $P$, where $X$ represents the number of positions in the area, and $N$ and $P$ have the meanings described above
- on the following $X$ lines, an $X \times X$ matrix, specifying the positions connected to each other (the roads are two-way)
- on the next $N$ lines, for each soldier in the special team, the starting point and destination are specified
- on the next line, the positions of the $P$ enemy soldiers are given
- on the following lines until the end of the file, pairs $i$ $j$ are given with the meaning that a soldier located at point $i$ can shoot an enemy located at point $j$. The pairs $i$ $j$ and $j$ $i$ will not exist simultaneously in the input file.

## Output data

The output file `antitero.out` will contain the mission plan. Its lines have the following format:
- "Success" - the first line
- $M$ $i$ $j$ - the soldier $i$ of the anti-terrorism team moves to position $j$ (without specifying the intermediate positions)
- $E$ $i$ $j$ - the soldier $i$ eliminates the terrorist $j$. The action must be presented chronologically.

If the mission cannot be completed, only the message "Mission aborted" will be displayed.

## Constraints and clarifications

$1 \leq X \leq 100$  
$1 \leq N \leq 10$  
$1 \leq P \leq 20$

In the initial points, there are no terrorists, and they are not threatened by them. Several soldiers may be in the same position simultaneously. The statement also applies to terrorists. A test for which there is a solution is failed if:
- at least one of the lines in the output file does not follow the above format
- an $M$ line sends a soldier to a point that is not accessible to him, or
- an $E$ line 'eliminates' a terrorist who is not located at a point where the respective soldier can shoot, or who was previously eliminated, or
- after completing the specified moves, at least one soldier is not in his final position.

## Example

`antitero.in`
```
8 2 2 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 1 0 0 0 0 0 1 
0 0 0 1 0 0 0 0 
1 0 0 0 1 0 0 0 
1 0 0 0 0 0 0 1 
1 0 0 0 0 1 0 0 
0 1 0 0 0 0 0 1 
5 2 
6 7 
8 7 
3 4 
7
```

`antitero.out`
```
Success 
M 2 4 
E 2 1 
M 1 5 
M 2 6 
```

## Explanation

The terrorists are located at $7$ and $8$, one of the soldiers must reach from $1$ to $5$ and the other from $2$ to $6$. From point $7$ an enemy located at $3$ can be eliminated, and from $4$ an enemy located at $7$. Soldier $2$ moves to position $4$. Soldier $2$ eliminates terrorist $1$. Soldier $1$ reaches $5$. Soldier $2$ reaches $6$.