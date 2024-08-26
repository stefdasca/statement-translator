Beads

Frightened by recent events at the salon she used to visit, Miruna thought it would be better to protect herself against bad luck. Searching through the attic, she found some old spell books that once belonged to her grandmother Boonikutzei. On page $666$ of the $13$th book she opened, Miruna found the desired spell: To avoid accidental weapon discharges, it is recommended to wear a necklace made of $N$ beads painted in red and blue, so that for any subarray of $K$ beads, there are at least $A$ and at most $B$ red beads. By complete coincidence, Miruna inherited a necklace with $N$ beads from Boonikutzei, and now she wonders in how many ways she can paint the beads to be protected.

## Task

## Input data

The input file `margele.in` contains on the first line $4$ integers $N$, $K$, $A$, and $B$ having the meaning from the statement.

## Output data

In the output file `margele.out` you will print a single integer representing the total number of ways to paint the beads modulo $666013$.

## Constraints

$1 \leq N \leq 50$

$1 \leq K \leq \min(10, N)$

$0 \leq A \leq B \leq K$

## Example

`margele.in`

```
5 5 1 4
```

`margele.out`

```
30
```

`margele.in`

```
20 10 3 8
```

`margele.out`

```
19672
```

## Explanation

For the first example, all $2^5$ colorings are valid except for the $2$ in which we use a single color.