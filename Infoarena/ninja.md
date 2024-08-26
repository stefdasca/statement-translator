## Task

Ninja A and Ninja B want to commit a respectable theft. Respectable in the sense that the other members of the ninja community would be somewhat impressed, because until now Ninja A and Ninja B have committed crimes with a turnover of around $3$ oranges and a RATB fine. This time, the two want to rob the gold reserves of the National Bank. These reserves are located in a rectangular room with dimensions $M \times N$. Each row of this room contains exactly one pile of gold. The piles contain gold bars. A gold bar of length $L$ spans $L$ columns of the matrix. A pile of gold of dimension $X$, where $X$ is an odd number, located in the range of columns $[LEFT, RIGHT]$, consists of a gold bar of length $X$ on top of which there is a pile of dimension $X - 2$, located in the range of columns $[LEFT + 1, RIGHT - 1]$. If the size of the pile is equal to $1$, then it has no other bar on top of it. Each column of the room is equipped with a surveillance camera. The camera located on column $C$ supervises all the gold bars that overlap with column $C$. Ninja A and Ninja B wonder how many gold bars would remain unsupervised if they turned off all the surveillance cameras in the range of columns $[R, C]$. They ask you for the answer to several such questions.

## Input data

The input file `ninja.in` will contain three natural numbers $N, M, K$ representing the number of columns, the number of rows of the room, and the number of questions you need to answer. The next $M$ lines will contain two numbers $X, Y$ each, representing the fact that on that line there is a pile of gold located in the range of columns $[X, Y]$. The next $K$ lines will also contain two numbers $A, B$ each, representing a question of the type "How many gold bars remain unsupervised if all the cameras in the range of columns $[A, B]$ are turned off?".

## Output data

The output file `ninja.out` will contain $K$ lines, each containing a natural number which represents the answer to the corresponding question.

## Constraints and clarifications

$1 \leq N, M, K \leq 10^5$

Attention: $M$ represents the number of rows in the matrix.

## Example

`ninja.in`
```
5 5 5
2 4
1 3
1 5
3 3
4 4
1 5
1 3
1 4
3 5
5 5
```

`ninja.out`
```
9
5
8
4
0
```