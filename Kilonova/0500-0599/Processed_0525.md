Gigel has an undirected graph `G` with `N` nodes and `M` edges labeled with positive costs. After the mix-up Gigel caused at the National Olympiad in Informatics, Ninel, Gigel's younger brother, stole all the edges. Gigel wants to recover the edges, but Ninel puts him through tough challenges.

Let `S` be a sequence of length `L` containing on each position an undirected edge with an associated cost and a refusal cost `r`. Gigel has the following mission from Ninel: he must find the minimum cost to travel from node `u` (in graph `G`) to node `v` (in graph `G`) using a subsequence of edges from the sequence `S`. He has an interval `[a, b] (a \leq b)` which determines which edges from the sequence `S` he is allowed to use. Thus, Gigel initially starts at node `u` and traverses the edges at the corresponding positions from `[a, b]` from left to right. At each step, Gigel:
* either chooses to use the current edge if he is at node `x` thus arriving at node `y` (or if he is at node `y` thus arriving at node `x`); the cost increases by the cost associated with the edge at the current step
* or refuses the current edge and remains in the node where he was when he reached the current step; the cost increases by the refusal cost associated with the element at the current step

# Task
The number `N` of nodes, the sequence `S` of edges, and `Q`, the number of missions Gigel has received, are known. The sequence `S` contains a tuple at each position in the form:
* `<x, y, c, r>` : `c` - represents the cost of the edge with endpoints at `x` and `y`; `r` - represents the refusal cost of the current edge

The `Q` missions are in the form:
* `<u, v, a, b>` : Gigel initially starts at node `u` and wants to reach node `v`. He starts traversing the edges in the interval `[a, b]` from left to right, at each step, choosing the edge or refusing it.

The task is to find the minimum cost for each of the `Q` missions. If Gigel cannot reach from node `u` to node `v`, output `-1`.

# Input data
The file `razbunare.in` contains on the first line `N`, the number of nodes in graph `G`, followed by `L`, the length of the sequence `S`, followed by `Q` which represents the number of missions Gigel has to complete. On the next `S` lines, a tuple in the form `<x, y, c, r>` with the meanings previously explained, representing the edges in the sequence `S`. On the next `Q` lines, a tuple in the form `<u, v, a, b>` representing the missions Gigel has to complete.

# Output data
The file `razbunare.out` contains `Q` numbers representing the answers to Gigel's missions in the order in the input file.

# Constraints and clarifications
* `2 \leq N \leq 30`
* $1 \leq L \leq 3 \cdot 10^4$
* $1 \leq Q \leq 3 \cdot 10^5$
* $0 \leq c \text{ (cost of an edge) }, r \text{ (refusal cost) } \leq 10^4$
* `1 \leq x, y, u, v \leq N`
* For `10` points `N \leq 7, L \leq 200, Q \leq 200`
* For another `30` points `N \leq 7, L \leq 20\ 000, Q \leq 20\ 000`
* For another `10` points `N \leq 10, L \leq 20\ 000, Q \leq 60\ 000`
* For another `25` points `N \leq 22, L \leq 20\ 000, Q \leq 60\ 000`
* For another `15` points `N \leq 30, L \leq 25\ 000, Q \leq 150\ 000`
* For the remaining `10` points: the original constraints
* For each edge in the sequence `S` we have `x ≠ y`
* Nodes are indexed from `1` to `N`
* The sequence is indexed from `1`
* If Gigel cannot reach from node `u` to node `v`, output `-1`
* After Gigel has traversed all the edges in the interval, he must be in node `v`

# Example
`razbunare.in`
```
5 5 3
1 4 4 5
4 1 6 1
2 1 2 9
2 5 1 0
1 5 2 5
2 2 2 4
5 4 5 5
1 5 2 5
```
`razbunare.out`
```
10
-1
9
```
Explanations
---

For the first mission: Gigel is at node `2` and wants to end up at node `2`. The minimum cost of traveling from `2` to `2` is to refuse all the edges from `[2, 4]: 1 + 9 + 0` (thus staying in node `2` the entire time).  
For the second mission: Gigel cannot travel from `5` to `4`.  
For the third mission: Gigel initially starts at node `1` and uses the edges from `[2, 5]`. He refuses the second edge `(4, 1)`, chooses the third edge and reaches `2`; chooses the fourth edge and reaches `5` and refuses the fifth edge: `1 + 2 + 1 + 5`.

`razbunare.in`
```
4 8 6
2 4 5 8
2 4 4 8
2 3 6 4
1 4 5 0
2 4 10 10
1 3 5 2
3 2 2 9
3 4 1 1
3 2 1 5
3 1 2 2
1 1 1 7
2 3 2 4
3 3 1 7
1 2 2 5
```
`razbunare.out`
```
32
-1
41
14
36
27
```
