## Task

Hercules has received a new task (if he solves it, he gets some reward). He needs to go to the Olympic basement to kill the Hydra. Initially, the Hydra has only one head (with index $1$). Every time Hercules cuts a head with index $i$, the Hydra grows the next $i \dots$ heads. Specifically, if the Hydra has heads from $1$ to $x$ and Hercules cuts head $y$, the Hydra grows heads from $x + 1$ to $x + y$. Once Hercules has cut a head, that head will not regenerate again, meaning a head with index $i$ cannot be cut multiple times. To become an Olympic-level fighter, Hercules has decided to reach the point where the Hydra has obtained head $K$ but no other head with a higher index. Since Hercules only knows the famous backtracking method, you have to help him determine the minimum number of operations to achieve his goal (as well as what the operations are).

## Input data

The input file `hercule.in` will contain on the first line a natural number $T$, the number of tests. The next $T$ lines will each contain a natural number $K$.

## Output data

The output file `hercule.out` will contain the answer for these $T$ tests. For a test, the first line will contain $sol$ - the minimum number of moves performed by Hercules. The second line will contain $sol$ numbers representing the moves (the indices of the heads that Hercules will cut in the correct order). If there is no solution, print $-1$.

## Constraints and clarifications

$1 \leq T \leq 10000$

$1 \leq K \leq 1000000000$

Any correct solution will be accepted

## Example

`hercule.in`
```
3
7
11
10
```

`hercule.out`
```
3
1 2 3
4
1 2 3 4
-1
```

