## Task

We all know that dedications at a party are very expensive. The great artist Sorin Pastrama has proposed a deal: if you help him solve the following problem, he will make as many dedications as you want at the next party, FOR FREE. The problem is as follows: We are given a tree with $N$ nodes. It is guaranteed that no matter which node you choose to remove from the tree, there is at least one resulting subtree that has the size. Let $val_i$ be equal to the value of edge $i$. Initially, $val_i = 0$ $(1 \leq i \leq N-1)$. We will take each pair of nodes $1 \leq x < y \leq N$ and increment the value of each edge on the path from $x$ to $y$ by 1. We will sort the edges in descending order according to their values (and in case of equality, in ascending order according to the edge index) and normalize them. That is, the first edge in the sort will have a value equal to 0, the second edge will have a value equal to 1, $\dots$, the last edge in the sort will have a value equal to $N-2$. Now, the final value of edge $i$ will be equal to $(val_i * alfa[val_i]) \% 100003$, where $alfa$ is an array of length $N-1$ given in the input. The task is to display a permutation $p(1), p(2), \ldots, p(N)$ of the numbers from 1 to $N$ that satisfies the following properties: it is maximum, where $dist(i, j) = length\ of\ the\ elementary\ path\ between\ nodes\ i\ and\ j$. The sequence of pairs $\{(p(1) \rightarrow 1, p(1)), (p(2) \rightarrow 2, p(2)), \ldots, (p(N) \rightarrow N, p(N))\}$ is lexicographically minimal, where $p(i) \rightarrow i$ represents the sequence of the final values of the edges on the path from node $p(i)$ to node $i$, in the order in which they appear on the path.

## Input data

The file `dedicatie.in` contains on the first line the natural number $N$ as described above. The next $N-1$ lines contain two natural numbers $x$ and $y$ with the meaning that there is an edge between these two nodes. The last line of the input file contains the $N-1$ elements of the array $alfa$ separated by a space (the array is indexed from 0).

## Output data

The file `dedicatie.out` will contain $N$ lines. The $i$-th line will contain the value of $p(i)$.

## Constraints and clarifications

$1 \leq N \leq 10^5$  
$1 \leq alfa[i] < 100003$  
$0 \leq i \leq N-2$  

A pair $(a, b)$ is smaller than a pair $(x, y)$ if $a < x$ or if $a = x$ and $b < y$.  
A sequence $\{a_1, a_2, \ldots, a_k\}$ is lexicographically smaller than the sequence $\{b_1, b_2, \ldots, b_s\}$ if there exists a position $1 \leq i \leq min(k, s)$ such that $a_1 = b_1, a_2 = b_2, \ldots, a_{i-1} = b_{i-1}$ and $a_i < b_i$ or if $a_1 = b_1, a_2 = b_2, \ldots, a_k = b_k$ and $k < s$. Sorin Pastrama's favorite phrase is: "You picked the wrong pocket, my boy!"

## Example

`dedicatie.in`  
`dedicatie.out`  
6  
5 4  
4 2  
3 1  
4 6  
1 5  
7574 2 1 66670 25002  

4  
5  
2  
1  
6  
3  

## Explanation

After we traverse each path and increment the edges by 1, their values are:  
edge 1 (5 $\rightarrow$ 4): 9  
edge 2 (4 $\rightarrow$ 2): 5  
edge 3 (3 $\rightarrow$ 1): 5  
edge 4 (4 $\rightarrow$ 6): 5  
edge 5 (1 $\rightarrow$ 5): 8  

After normalization, the edges have the following values:  
edge 1 (5 $\rightarrow$ 4): 0  
edge 2 (4 $\rightarrow$ 2): 2  
edge 3 (3 $\rightarrow$ 1): 3  
edge 4 (4 $\rightarrow$ 6): 4  
edge 5 (1 $\rightarrow$ 5): 1  

After multiplying with $alfa$, the edges have the final values:  
edge 1 (5 $\rightarrow$ 4): $(0 * 7574) \% 100003 = 0$  
edge 2 (4 $\rightarrow$ 2): $(2 * 1) \% 100003 = 2$  
edge 3 (3 $\rightarrow$ 1): $(3 * 66670) \% 100003 = 4$  
edge 4 (4 $\rightarrow$ 6): $(4 * 25002) \% 100003 = 5$  
edge 5 (1 $\rightarrow$ 5): $(1 * 2) \% 100003 = 2$  

The optimal permutation is:  
4  
5  
2  
1  
6  
3  

and it is maximum. The sequence of pairs is:  
$\{(\{0, 2\}, 4), (\{0, 2\}, 5), (\{2, 0, 2, 4\}, 2), (\{2, 0\}, 1), (\{5, 0\}, 6), (\{4, 2, 0, 5\}, 3)\}$  
and it is lexicographically minimal.