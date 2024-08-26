## Task

Help the organizers answer the $T$ questions.

## Input Data

The first line of the input file `galerie.in` will contain three natural numbers $N,M$, and $T$ as described in the statement. The next $M$ lines will contain three natural numbers $P,Q,C$ each, describing that $C$ moles start from room $P$ to room $Q$. Each of the following $T$ lines will contain three numbers $X,Y,K$ describing a question from the organizers.

## Output Data

The output file `galerie.out` will contain $T$ lines, each line containing a number $D_i$, representing the answer to the $i$-th question asked by the organizers.

## Constraints

$1 \leq T \leq 250\,000$

$1 \leq N, M \leq 100\,000$

$1 \leq P, Q, X, Y, K \leq N$

$P \ne Q$

$X \ne Y$

$0 \leq C \leq 50$

For $20\%$ of the tests, it is guaranteed that $T,M \leq 1\,000$

No more moles will leave a room than were accommodated

The moles will travel through the rooms in strictly increasing or strictly decreasing order

From a room $P$ from which no tunnel starts, moles can only move to room $P-1$ or $P+1$

The moles are not obliged to use the tunnels

## Example

`galerie.in`
```
4 1 1
1 4 2
1 3 1
```

`galerie.out`
```
2
```

## Explanation

If no tunnel is built, the moles follow the path $1-2,2-3,3-4$, taking a total time of $2*3=6$.

In the case of the first question, the chosen path will be $1-3,3-4$, traveled in a time of $4$. The final time is reduced by $2$.