## Crybabies

## Task

On June $1^{st}$, Mrs. Eraotacude thought of organizing a surprise for the $K$ kindergarten children. She bought $N$ cakes, with the $i^{th}$ cake having $A_i$ slices. She arranged the children in a line, numbered them from $1$ to $K$ (it is guaranteed that she can count up to $K$), and after careful consideration, she decided how to distribute the sweets. Thus, at each moment in time, the first child in the line will approach the table with the cakes and state which cake they would like to eat from. If there is at least one slice of that cake on the table, Mrs. Eraotacude will give the child a slice from that cake, and the child will happily go to the end of the line. Otherwise, if there are no more slices of that cake on the table, the child will start to cry, hence being named CrybabyNr$1$. Of course, in a split second, their colleagues will follow, thus triggering the Choir of Crybabies. At that moment, Mrs. Eraotacude will stop serving the sweets permanently and will try to stop the Choir of Crybabies. To do this, she has to put CrybabyNr$1$ in the corner. For purely statistical reasons, Mrs. Eraotacude wants to know, for each child, for how many sequences of choices that child will end up being CrybabyNr$1$. A sequence $s_1, s_2, s_3, \dots, s_p$ is called a sequence of choices if $s_t$ represents the cake from which a slice was taken at moment $t$ ($1 \leq t \leq p-1$), and $s_p$ represents the cake from which CrybabyNr$1$ wanted to eat. Obviously, for a sequence of choices to be valid, it is necessary that at moment $t$ ($1 \leq t \leq p-1$) there is at least one slice left from cake $s_t$, and at moment $p$ there are no more slices left from cake $s_p$.

## Input data

The input file `plangaciosi.in` will contain the first line $N$ and $K$. The second line will contain the $N$ values $A_i$.

## Output data

The output file `plangaciosi.out` will contain a single line with $K$ values. The $i^{th}$ value will represent the number of sequences of choices in which child $i$ is CrybabyNr$1$ (modulo $1.000.000.007$).

## Constraints and clarifications

$1 \leq N, K \leq 2000$

$1 \leq A_i \leq 2000$

$A_1 + A_2 + A_3 + \dots + A_N \leq 2000$

For $10$ points, it is guaranteed that in total there are at most $2 \times 10^6$ sequences of choices.

For another $10$ points, it is guaranteed that $A_i = 1$ for any $i$.

For another $30$ points, it is guaranteed that $N \leq 40$ and $A_1 + A_2 + A_3 + \dots + A_N \leq 400$

For another $25$ points, it is guaranteed that $A_1 + A_2 + A_3 + \dots + A_N \leq 800$

## Example

`plangaciosi.in`

```
2 6
1 2 0 1
3 6
0 0
```

## Explanation

The $10$ sequences of choices are:
$1 \dots 1 2$

$1 \dots 2 2$

$1 \dots 2 2$

$2 \dots 2 2$

$1 \dots 1 2$

$1 \dots 2 2$

$2 \dots 2 1$

$2 \dots 1 1$

$2 \dots 1 2$

$2 \dots 1 2$

CrybabyNr$1$ is child $2$ in the first sequence, child $3$ in sequences $2, 5$, and $10$, and child $4$ in the other $6$ sequences.