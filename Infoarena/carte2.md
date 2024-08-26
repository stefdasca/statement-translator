## Task

Andrei has a book with dimensions $A \times B$ cm. The thickness of the book is strictly less than 1 cm because a book that is too thick is not suitable for Andrei. After finishing browsing the book, Andrei wants to place it in a cuboid box with dimensions $C \times D \times E$ cm. To achieve this, Andrei can rotate the box as he wishes: any of the box's faces can become the base, meaning the face that will be placed on the floor or the bottom of the box. Obviously, he can also rotate the book. However, the final position of the book is correct only if it is inside, on the bottom of the box, in a horizontal position with the edges parallel to the edges of the box. To insert the book, its dimensions must be strictly smaller. For example, it is sufficient if $A < D$ and $B < C$, if the chosen base is the face with dimensions $C \times D$.

## Input data

The input file `carte2.in` contains on the first line the number $T$, the number of tests. The next $T$ lines contain five natural numbers separated by space, in the order: $A$ $B$ $C$ $D$ $E$.

## Output data

In the output file `carte2.out` print for each test in order "posibil" or "imposibil" on a separate line, if it is possible to correctly insert the book into the box or not.

## Constraints

$T \leq 200$

$1 \leq A, B, C, D, E \leq 1000$

## Example

`carte2.in`
```
2
2 5 6 2 3
2 5 5 2 3
```

`carte2.out`
```
posibil
imposibil
```