Sure! Here is the translated text:

---

Given a tree with $N - 2$ nodes and probabilities $p$ on the edges. The edge from node $x$ to node $y$ has probability $p_{x,y}$. There is a hungry cat in each node. On each edge, there is a delicious pie, all made of mice, whiskas, milk, etc. All pies are initially covered, practically invisible to the kittens.

The pies will be uncovered in turn, and our well-known character, *Marcel*, has the honor of setting the order in which the pies will be shown to the kittens. Then, when the pie from the edge of node $x$ to node $y$ is uncovered, one of the following happens: 
1. If none of the cats at nodes $x$ or $y$ have eaten a pie yet, either the cats will agree and eat the pie together from the edge, or they will quarrel and overturn it. The probability that both do **not** eat will be $p_{x,y}$.
2. If exactly one of the cats has already eaten, that cat will be too lazy to move from her node and will allow (generously) the other to eat peacefully. 
3. If both cats have already eaten, the food will remain untouched.

After all the pies have been uncovered, it is clear that each cat $x$ will have a probability $q_x$ of remaining hungry (respectively $1 - q_x$ of having eaten).

Help Marcel find an order of uncovering the pies in which scenario 3 (described above) **cannot happen**, and for which the value of the maximum $q$ that $q_x$ can have is minimized.

# Task
The competitor will implement a single function, `solve`, with the following signature:
```cpp
long long solve (int n, std::vector<int> t, std::vector<int> v);
```

The parameters of this function have the following meanings:
* $n$ represents the number of nodes in the tree. These are numbered from $1$ to $n$.
* $t$ contains $n-1$ elements with the meaning that there exists an edge between $i + 2$ and $t[i]$ for $i = 0, 1, ..., n-2$.
* $v$ contains also $n - 1$ elements with the meaning that $p_{i+2,t[i]} = 2^{-v[i]}$. **These numbers are integers to avoid precision errors**. It is guaranteed that $0 \le v[i] \le 10^9$.

The function will return an integer $r$, with the property that the required probability $q$ in the statement satisfies $q = 2^{-r}$. This number can be demonstrated to always be an integer.

**The competitor does NOT implement a `main` function.**

## Subtask 1 (6 points)
* $N \le 8$
## Subtask 2 (9 points)
* $N \le 25$
* It is guaranteed that for any node $i = 1, 2, ..., n$, there exist either $2$ values or no value $j$ in $\{1, 2, ..., n\}$ with the property that $t[j] = i$.
## Subtask 3 (8 points)
* $N \le 100\ 000$
* Each node has a maximum degree of 2.
## Subtask 4 (18 points)
* $N \le 50$
## Subtask 5 (19 points)
* $N \le 700$
## Subtask 6 (7 points)
* $N \le 100\ 000$
* It is guaranteed that for any node $i = 1, 2, ..., n$, there exist either $2$ values or no value $j$ in $\{1, 2, ..., n\}$ with the property that $t[j] = i$.
## Subtask 7 (16 points)
* $N \le 100\ 000$
* All probabilities corresponding to edges are equal among them.
## Subtask 8 (17 points)
* $N \le 100\ 000$

# Examples
`Input`
```
5
1 1
1 2
3 1
1 2
```
`Output`
```
3
```
`Input`
```
8
1 793356
1 1666576
2 7158429
1 2321928
4 2158429
6 1035046
1 1852042
```
`Output`
```
7951785
```

---

In the first example, the order of uncovering the pies on the edge is: $(1\ 3), (1\ 2), (3\ 4), (1\ 5)$. 

In the second example, there was an order for which the answer would have been smaller than that in the example, only this assumed that the probability that two cats refuse both pies between them was non-zero!