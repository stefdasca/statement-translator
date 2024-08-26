Cats

## Task

Given a tree with $N \geq 2$ nodes and probabilities $p$ on the edges. On the edge from node $x$ to $y$ there is the probability $p_{x,y}$ with $0 < p_{x,y} \leq 1$. In each node, there is a hungry cat. On each edge, there is a delicious pie, full of mice, whiskas, milk, $\dots$. All pies are initially covered, practically invisible to the little cats. The pies will be uncovered one by one, and our well-known character, Marcel, has the honor of establishing the order in which the pies will be shown to the cats. When the pie on the edge from node $x$ to node $y$ is uncovered, one of the following happens:
- If neither of the cats at nodes $x$ or $y$ have eaten pie yet, the cats will either agree and eat the pie on the edge together, or argue and tip it over. The probability that both will not eat is $p_{x,y}$.
- If exactly one of the cats has already eaten, that cat will be too lazy to move from its node and will (generously) let the other eat in peace.
- If both cats have already eaten, the food will remain untouched.

Once all the pies are uncovered, it is clear that each cat $x$ will have a probability $q_x$ of remaining hungry (or $1 - q_x$ of having eaten). Help Marcel to find an order of uncovering the pies in which scenario 3 (from those described above) CANNOT happen, and for which the maximum value $q$ that $q_x$ can have is minimized.

## Input data

The input file `pisici.in` contains, on the first line, the number $n$. The nodes of the tree are numbered from $1$ to $n$. The second line contains $n - 1$ numbers, representing the array $t$ (let's denote $t[i]$ as the $i$-th of these numbers), meaning there is an edge between $i + 1$ and $t[i]$ for $i = 1, 2, \dots, n - 1$. The third line contains $n - 1$ numbers, representing the array $v$, meaning that $p_{i+1,t[i]} = 2^{-v[i]}$. These numbers are integers to avoid precision errors. It is guaranteed that $0 \leq v[i] \leq 10^9$ and that $1 \leq t[i] \leq i$.

## Output data

The output file `pisici.out` will contain an integer $r$, with the property that the required probability $q$ in the statement satisfies $q = 2^{-r}$. This number can always be demonstrated to be an integer.

## Constraints and clarifications

$2 \leq N \leq 50000$

### Subtask Stay Home, $6$ points:
$N \leq 8$

### Subtask Relatives Only, $9$ points:
$N \leq 25$ 
and it is guaranteed that for any node $i = 1, 2, \dots, n$, there exist either 2 values or no values $j$ in $\{1, 2, \dots, n - 1\}$ with the property that $t[j] = i$.

### Subtask At the Airport, $8$ points:
Each node has a maximum degree of $2$.

### Subtask Camp Isolation, $18$ points:
$N \leq 50$

### Subtask Trapped in School, $19$ points:
$N \leq 700$

### Subtask Family Reunion, $7$ points:
It is guaranteed that for any node $i = 1, 2, \dots, n$, there exist either 2 values or no values $j$ in $\{1, 2, \dots, n - 1\}$ with the property that $t[j] = i$.

### Subtask Corporation Party, $16$ points:
All edge probabilities are equal.

### Subtask Town Quarantine, $17$ points:
No other guarantees.

## Example

`pisici.in`
```
5
1 1 3 1
1 2 1 2
```
`pisici.out`
```
3
```

`pisici.in`
```
8
1 1 2 1 4 6 1
793356 1666576 7158429 2321928 2158429 1035046 1852042
```
`pisici.out`
```
3
```

## Explanation

In the first example, the order of uncovering the pies on the edges is: $(1, 3)$, $(1, 2)$, $(3, 4)$, $(1, 5)$. In the second example, there is an order for which the answer would have been smaller than in the example, but that would have required that it was possible for two cats to both refuse the pie between them (scenario 3, forbidden)!