# Christmas

Tanaka has decided to celebrate Christmas (a bit early by traditional standards, but who can resist a good kurtos kalacs?), and as a result, he needs to buy a Christmas tree. Unfortunately, the tree nursery in his village only has one rooted tree, with $N$ nodes. The root is node $1$. Tanaka doesn't want to buy the whole tree, but the owner of the nursery is offering a spectacular promotion: Tanaka is allowed to buy any connected subset of nodes of the tree. The machine that will cut the tree will use a cost proportional to the maximum number of nodes in an "upward" path (defined rigorously in the clarifications) in the subset. Moreover, from each node of the tree, a number of ornamental globes can hang. Tanaka would like to choose a set where as many ornamental globes as possible can hang, but he also cares about the cost. Help Tanaka select a set where the ratio of the sum of the number of ornamental globes that can hang in its nodes to the cost of purchasing it is maximized.

## Input data

The first line of the input file `craciun.in` will contain the value $N$. The second line contains $N$ numbers, where the $i$-th number represents the number of ornamental globes that can hang on node $i$. The third line contains $N-1$ numbers, where the $i$-th number represents the ancestor of node $i+1$.

## Output data

The output file `craciun.out` will contain the required ratio.

## Constraints and clarifications

$0 \leq$ number of ornamental globes that can hang on each node $\leq 1\ 000\ 000$

To receive points on a test, your answer must have a relative or absolute error compared to the committee's answer of at most $10^{-4}$.

Scientific notation will not be accepted in displaying the answer (for example, $1e9$ is not acceptable).

An "upward" path represents a path $a_{1} - a_{2} - \dots - a_{K}$ where $a_{i}$ is the child of $a_{i+1}$, for $i = 1, \dots, K-1$.

Subtask 1 (feedback test 2) - 10 points:
$1 \leq N \leq 500$.

Subtask 2 (feedback test 7) - 10 points:
$1 \leq N \leq 1\ 000$.

Subtask 3 (feedback tests 9 and 10)  - 10 points:
$1 \leq N \leq 3\ 000$.

Subtask 4 (feedback tests 13 and 15)  - 40 points:
$1 \leq N \leq 50\ 000$.

Subtask 5 (feedback tests 17 and 18)  - 30 points:
$1 \leq N \leq 100\ 000$.

## Example

`craciun.in` 
```
3 
100 101 102 
1 1 
```

`craciun.out` 
```
151.5 
```

## Explanation

The entire tree is selected.