# Concert

A group of $N$ artists have received invitations to perform at a concert. Each artist was sent an invitation with a specified time interval between hours $A$ and $B$. However, the event organizers made a mistake, leading to overlapping performance times for some artists. The artists, being renowned, refuse to perform unless they can do so alone. Additionally, they demand compensation if required to start performing after the hour $A+1$ or finish before the hour $B$. An artist can only perform between the hours $A$ and $B$ on their invitation. Some invitations can be canceled, so some artists might not perform at all.

## Task

Knowing the intervals within which each artist can perform, the profit each artist brings per unit of time, and the compensations demanded in the aforementioned cases, you need to determine the maximum sum achievable at the concert and how it can be achieved.

## Input data
The first line of the file `concert.in` will contain $N$. The next $N$ lines of the file will contain 5 numbers each, separated by a space. They represent $A$, $B$, the profit per unit of time, and the compensations if the artist does not start performing at $A+1$ and if they do not finish performing at $B$.

## Output data
The first line of the file `concert.out` will contain the maximum sum that can be obtained from the concert.

## Constraints
$1 \leq N \leq 1\,000$

$1 \leq A_i < B_i \leq 2\,000\,000\,000$

The profit brought by each artist or the compensations demanded by each of them will not exceed the value 500.

Compensations are paid once, not per unit of time.

If the artist $i$ has in their contract the interval $(A_i, B_i)$, they can perform between hours $A_i + 1$ and $B_i$ inclusive.

Any two artists have different intervals.

The solution will not exceed the value $2^{31} - 1$

No two artists $x$ and $y$ have intervals such that the interval in which $x$ can perform is completely within $y's$ interval.

## Examples
`concert.in`
```
5
0 5 10 10 15
3 8 8 8 20
4 10 12 4 10
8 16 7 4 7
12 20 10 5 50
```

`concert.out`
```
189
```

## Explanation

Artist 1 performs between hours $1$ and $5$, bringing a profit of $(5 - 1 + 1) \times 10 = 50$ and does not demand compensations because they performed within the hours specified in the invitation.

Artist 2 does not perform at all.

Artist 3 performs between hours $6$ and $10$, bringing a profit of $(10 - 6 + 1) \times 12 = 60$, but they receive a compensation of $4$ because they did not start at the hour specified in the invitation, hour $A + 1 = 4$. Thus artist 3 brings a profit of $60 - 4 = 56$.

Artist 4 performs between hours $11$ and $12$, bringing a profit of $2 \times 7 = 14$, but demands both compensations, thus bringing a profit of $14 - 7 - 4 = 3$.

Artist 5 brings a profit of $8 \times 10 = 80$ and does not demand compensations because they performed within the specified hours. Thus, the total adds up to: $50 + 56 + 3 + 80 = 189$.