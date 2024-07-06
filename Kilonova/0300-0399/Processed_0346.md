```markdown
As you may already know, accountants keep their data in form of tables and they calculate all sorts of sums on lines and columns. Atnoc, our accountant, has organized his values in the form of a table with $N$ rows (numbered from $0$ to $N - 1$) and $M$ columns (numbered from $0$ to $M - 1$).

Elements on the last column are the sums of their row (more precisely, the element on row $i$ and column $M - 1$ is the sum of elements on row $i$ situated on the columns $0, 1, 2,... , M - 2$), and the elements on the last line are the sums of their column (more precisely, the element on column $i$ and row $N - 1$ is the sum of elements on column $i$ situated on the rows $0, 1, 2,... , N - 2$). An example of such a table is shown below.

| $2\ $ | $5\ $  |  $7\ $  | $\bold{14\ }$    |
|---|---|---|---|---|
| $11\ $ | $6\ $  |  $6\ $  | $\bold{23\ }$  |
| $\bold{13\ }$ | $\bold{11\ }$ |  $\bold{13\ }$ |  $\bold{37\ }$ | 

Unfortunately, Atnoc spilled water on his beloved table and in so doing some of the table's elements became unreadable. In order to recover the value in cell $(i, j)$ he will need to pay a cost of $B_{ij}$.

Determine the minimum cost Atnoc has to pay in order to be able to recover the table.

# Interaction

To solve this problem you will have to implement the following function:
```cpp
long long solve(int N, int M, int** A, int** B);
```

The parameters $N$ and $M$ represent the size of the table. The arrays $A$ and $B$ (whose rows are indexed from $0$ to $N-1$ and columns from $0$ to $M-1$) represent the elements of the table and the cost to recover the values respectively.

The function should return the minimum cost to recover the table.

# Constraints
$1 \leq N, M \leq 3\ 000$

$1 \leq A_{ij}$ if the element is readable or $A_{ij} = -1$ if the element is unreadable

$A_{ij} \leq 100$ for $i \neq N - 1$ or $j \neq M - 1$

$1 \leq B_{ij} \leq 10^6$ 

It is guaranteed there is no further information to be extracted from the (readable) values themselves

For tests worth $10$ points, $(1 \leq N, M \leq 4)$.

For tests worth $25$ more points, $(1 \leq N, M \leq 15)$. 

For tests worth $40$ more points, $(1 \leq N, M \leq 750)$.

Note: The test data is not the same as the one used during the original contest and the statement has been slightly modified.

# Example 

The [sample grader](_grader.cpp) reads the number `N` and `M` from the first line and on the next `N` lines `M` values representing the values of `A` and then on the final `N` lines `M` values representing the values of `B`.

`stdin`
```
3 3
-1 -1 -1
-1 2 -1
3 4 7
3 3 18
4 1 4
2 2 2
```
`stdout`
```
3
```

Explanation
---

By finding the cell $(0, 0)$, paying $3$ we will have enough information to reconstruct the entire table.
```