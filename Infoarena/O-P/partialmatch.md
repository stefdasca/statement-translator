## Task

Because Antonio and Antonia are at the seaside, we present another type of problem with a super short statement: Two strings $A$ and $B$ and a natural number $K$ are given. The task is to determine how many positions string $A$ "almost-matches" over string $B$. A string $A$ "almost-matches" over another string $B$ at a position $i$ $(0 \leq i < |B|)$, if $i + |A| \leq |B|$ and there are at most $K$ positions $j$ $(0 \leq j < |A|)$, for which $A[j] \neq B[i + j]$.

## Input data

The input file `partialmatch.in` contains on the first line the string $A$, on the second line the string $B$, and on the third line the number $K$. 

## Output data

In the output file `partialmatch.out` you will print the number of almost-matches of $A$ over $B$ and their positions, one number per line.

## Constraints and clarifications

$1 \leq |A|$, 
$|B| \leq 100\ 000$

$0 \leq K \leq 10$

Both strings contain only characters from the Latin alphabet. 

Character numbering starts at position $0$. 

## Example

`partialmatch.in`

```
abba
abbaaba
1
```

`partialmatch.out`

```
2
0
3
```

`partialmatch.in`

```
baa
ccba
1
```

`partialmatch.out`

```
0
```

## Explanation

There are two almost-matches of $A$ over $B$:

$abba$ $aba$
$abba$ $abb$
$a$ $ba$
$a$ $b$
$ba$