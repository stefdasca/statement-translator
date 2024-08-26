## Task

Because Mihăiţă stayed too long at the No Stress contest award ceremony, he arrived late and missed the beginning of the ball. Being generous by nature, he wants to treat his girlfriend with the money won at the contest. Arriving at the club, Mihăiţă notices a few strange things. We can imagine Barletto as a square matrix of size $N \times N$, with the entry at position $(1, 1)$. On every column $i$, $2 \leq i \leq N-1$, there is a partygoer dancing meneaito. Mihăiţă knows for each partygoer on column $i$, their initial position $(A[i], i)$, and that they only dance on their column, between positions $(A[i], i)$ and $(B[i], i)$ as follows: every second they move one cell in the same direction until they encounter one of the ends of the space in which they can dance, at which point they change direction. Because there is too much smoke in the club and Mihăiţă doesn't know that his girlfriend is having fun at the artists' table, located at position $(N, N)$, he does not enter the club until he manages to see her. Mihăiţă can see her at a moment in time $t$, if no partygoer is at that moment on any of the positions $(i, i)$, $2 \leq i \leq N-1$. Since Mihăiţă is not very patient, he will go home if he doesn't manage to see his girlfriend in $200000$ seconds. The minimum moment in time when Mihăiţă finds his girlfriend should be displayed, or $-1$ if Mihăiţă gets bored and goes home.

## Input data

The input file `meneaito.in` contains a natural number $N$, the size of the Barletto club. The next two lines contain $N-2$ numbers, representing the positions described by $A$ and $B$, respectively.

## Output data

The output file `meneaito.out` will contain a single integer, the required minimum time or $-1$.

## Constraints and clarifications

$1 \leq N \leq 200000$

$1 \leq A[i] \leq B[i] \leq 200000$

Mihăiţă enters the club at the time $0$

## Example

`meneaito.in`
```
5
2 2
2 3
5 5
```

`meneaito.out`
```
3
```

