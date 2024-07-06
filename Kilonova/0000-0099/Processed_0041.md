Those who have seen the movie Highlander know that the phrase with which the immortals begin the fight is "There can be only one." Let us try to simulate the story of the immortals.

In a rectangular area composed of $n$ rows (numbered from $1$ to $n$) and $m$ columns (numbered from $1$ to $m$), there are at most $n \times m-1$ immortals. Two neighboring immortals "fight" each other and the one who loses the fight is eliminated. The "fight" consists of one immortal jumping over the other, if such a jump can be made. The jump can be horizontal or vertical and the immortal over which the jump is made disappears. A neighbor of the immortal in position $(i, j)$ is understood to be an immortal in one of the positions $(i-1,j), (i+1,j), (i,j-1), (i,j+1)$. Therefore, after the fight, the immortal from the field $(i,j)$ will be found in one of the positions: $(i-2,j), (i+2,j), (i,j-2)$ or $(i,j+2)$, if this position is free and is within the area.

# Task
Determine a sequence of battles that can be fought, so that in the end only one immortal remains.

# Input data
The input file `immortal.in` contains the first line with three natural values $n m I$, separated by a space, representing the number of rows, the number of columns of the described area, and respectively the number of initially existing immortals. The next $I$ lines each contain two natural numbers $x\ y$ separated by a space, representing the positions where the $I$ immortals are initially found (row and column).

# Output data
The output file `immortal.out` will contain $I-1$ lines, each line describing a "battle." The battles will be written in the order they happened. A line will contain $4$ natural numbers indicating: the first two are the position from which an immortal goes to "fight", and the last two are the position where this immortal reaches after the "fight". For the "fight" to be correct, in the position over which the immortal "jumps", there must be an immortal who will "die". A position will be specified by the row index followed by the column index. The values written on the same line will be separated by spaces.

# Constraints and clarifications
* $1 < n, m \leq 20$
* $1 < I \leq \min{15, n \times m-1}$
* For the test data, there is always a solution.

# Example

`immortal.in`
```
3 4 4
1 2
2 1
3 2
3 3
```

`immortal.out`
```
3 3 3 1
3 1 1 1
1 1 1 3
```

Explanations
---

```  
   1   2   3   4
 =================   
1|   | * |   |   |    
 |---------------|   
2| * |   |   |   |
 |---------------|
3|   | * | * |   |
 =================
 ```  
 $(3, 3) \rightarrow (3,1)$  $(3, 2)$ disappears
 $(3, 1) \rightarrow (1,1)$  $(2, 1)$ disappears
 $(1, 1) \rightarrow (1,3)$  $(1, 2)$ disappears