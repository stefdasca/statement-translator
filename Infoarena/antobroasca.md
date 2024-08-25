## Task

Since Antonia's birthday is on July 31, Antonio thought of buying her a frog, as it is her favorite pet. To make this gift complete, Antonio asks his girlfriend the following question: "Look, I've placed the frog on the coordinate axis $xOy$ at the point $(0, 0)$. Then, I named the frog Antobroasca; I believe the name suits it. I taught Antobroasca to move a distance of exactly $X$ horizontally, or a distance of exactly $Y$ vertically. To make the game a bit more complex, I also taught Antobroasca to move diagonally along a direction parallel to the first bisector, for a distance of exactly $Z * \sqrt{2}$. I want you to tell me if the frog can ever stop at the coordinates $(A, B)$."

## Input data

The input file `antobroasca.in` contains on the first line a natural number $T$, representing the number of tests. For each test, the first line will contain three natural numbers: $X$ $Y$ $Z$, with the significance described above, and on the second line will contain two natural numbers: $A$ $B$, representing the coordinates in Antonio's question.

## Output data

The output file `antobroasca.out` will contain $T$ lines, with each line $i$ containing the answer to question $i$. If the frog can stop at the coordinates $(A, B)$ in question $i$, print "DA". Otherwise, print "NU".

## Constraints

$1 \leq T \leq 100$  
$1 \leq X, Y, Z \leq 1\ 000\ 000\ 000$  
$-1\ 000\ 000\ 000 \leq A, B \leq 1\ 000\ 000\ 000$

## Example

`antobroasca.in`  
```
5
1 2 3
-3 8
1 3 3
3 8
1 3 4
3 1
1 3 4
0 0
2 1 1
-1 -1
```

`antobroasca.out`  
```
DA
NU
DA
DA
DA
```

## Explanation

For the first test, the frog can make the moves: $(0, 0) \rightarrow (-1, 0) \rightarrow (-2, 0) \rightarrow (-3, 0) \rightarrow (-3, 2) \rightarrow (-3, 4) \rightarrow (-3, 6) \rightarrow (-3, 8)$  
For the third test, the frog can make the moves: $(0, 0) \rightarrow (4, 4) \rightarrow (3, 4) \rightarrow (3, 1)$  
For the fourth test, the frog stays still.  
For the fifth test, the frog can make the moves: $(0, 0) \rightarrow (-1, -1)$