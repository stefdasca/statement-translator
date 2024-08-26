## Task

Tanaka is in trouble again! As the $Nespus$ festival is approaching, he needs to find accommodation for his $K-1$ friends (including himself, that's $K$ ) in the city of $Julc$. The city of $Julc$ is organized as a tree with $N$ nodes (the nodes are intersections, and the edges are streets). Each intersection has a hotel, but due to the festival crowd, each hotel can host only one person. On each street, a band will play 24 hours a day; each band has a fun index. Tanaka's group will only visit the minimal subtree that contains all their hotels (since they are very tired from dancing, they don't want to walk too much). Tanaka doesn't want his friends to argue because of the fun index differences of various bands in the visited area, and he doesn't care much about the fun index of the bands themselves. Can you help $Tanaka$ find what would be the minimum possible difference between the maximum and minimum fun index of all the bands in the visited area, for any way of choosing $K$ hotels?

## Input data

The input file `nespus.in` will contain, in the first line, $N$ and $K$. On the next $N-1$ lines, the streets of $Julc$ will be described, one per line. Each street will be represented by a triplet $x$ $y$ $z$, which indicates that there is a street between intersections with indices $x$ and $y$, where a band with a fun index equal to $z$ is playing.

## Output data

The output file `nespus.out` will contain the required difference.

## Constraints and clarifications

$2 \leq K \leq N$ (Tanaka doesn't want to go to the festival alone ☺).  
$1 \leq$ fun index of any band $\leq 1000\ 000\ 000$  

Subtask $1$ (feedback test $1$) - $10$ points:  
$2 \leq N \leq 100$

Subtask $2$ (feedback test $3$) - $20$ points:  
$2 \leq N \leq 1000$

Subtask $3$ (feedback tests $7$, $8$, and $12$) - $30$ points:  
$2 \leq N \leq 50\ 000$

Subtask $4$ (feedback tests $13$, $14$, and $20$) - $40$ points:  
$2 \leq N \leq 100\ 000$

To ease the implementation, the streets are given in ascending order of the fun index of the band playing on them.

## Example

`nespus.in`
```
4 3
2 3 1
3 4 2
1 2 100
```

`nespus.out`
```
1
```

## Explanation

The hotels are chosen from intersections $2$, $3$, $4$

`nespus.in`
```
6 3
2 1 3
5 3 4
6 1 6
3 2 9
4 2 12
```

`nespus.out`
```
3
```

The hotels are chosen from intersections $1$, $2$, $6$