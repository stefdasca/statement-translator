## Task

The mage Roxanne, after numerous hours of researching ancient mysteries, decided to go to a café to relax. When she arrived at the old café, she saw on the wall a strange structure called a tree. Formally, a tree is a collection of $N$ vertices numbered with consecutive natural numbers, where vertex $0$ is the root, and all other vertices have a unique parent (vertex $v$ has parent $p_v$). Because the café is run by magicians and programmers, the tree is drawn with the root at the top. Intrigued by this structure, the mage decides to pour magic coffee into one of the vertices. If the coffee is poured into vertex $u$, then it overflows into the subtree with root at vertex $u$. Because it is magic coffee, it does not flow randomly; it occupies the longest chain it can occupy in the subtree rooted at vertex $u$, when passing through node $u$. The amount of coffee lost when it flows is proportional to the length of the chain that the coffee occupies. Roxanne notes this amount as $r_u$. Note that the edges of the tree can have different lengths. Roxanne is interested in the amount of coffee she might lose if she pours it into all the vertices of the tree; this is the sum of the values $r_u$ from all vertices $u$ of the tree. Initially, this is not hard to calculate, but the programmers decide to challenge her and increase the length of certain edges $Q$ times. Can you help Roxanne find the total length of all the chains occupied by the coffee, if it is poured into all the vertices, initially and after each of the $Q$ modifications? Note! She needs the answers modulo $10^9 + 7$.

## Input data

In the input file `arboras.in`, the first line contains a single integer $N$, the number of vertices. The second line contains $N−1$ integers: $p_1, p_2, \dots, p_{N−1}$, where $p_v$ is the parent of node $v$, while node $0$ is the root. The third line contains $N−1$ integers: $d_1, d_2, \dots, d_{N−1}$, where $d_v$ is the length of the edge between vertex $v$ and $p_v$. The fourth line contains $Q$, the number of increases. Each of the next $Q$ lines contains two integers $v_i$ and $add_i$, representing modification $i$, where the length of the edge between vertex $v_i$ and $p_{v_i}$ increases by $add_i$.

## Output data

In the output file `arboras.out`, print $Q+1$ lines: on the $i+1 \text{st}$ line print the answer after the $i \text{th}$ modification. On the first line, print the answer before any modification. All answers must be printed modulo $10^9 + 7$.

## Constraints

$1 \leq N \leq 100\,000$

$1 \leq Q \leq 100\,000$

$1 \leq d_i \leq 100\,000$ for any $1 \leq i \leq N-1$

$1 \leq d_i < i$ for any $1 \leq i \leq N-1$

$1 \leq add_i \leq 10^9$ for any $1 \leq i \leq Q$

For 11 points: $1 \leq N \leq 1\,000$, $1 \leq Q \leq 1\,000$

For other 13 points: The tree height is at most 50

For other 31 points $d_i = 100\,000$ for any $1 \leq i \leq N-1$, $add_i = 10^9$ for any $1 \leq i \leq Q$

## Example

`arboras.in`

```
5
0 0 1 1
0 0 0 0
10
1 2
2 2
3 2
4 2
4 1
3 1
2 1
1 1
4 1000
2 1000
```

`arboras.out`

```
0
2
4
8
10
12
13
14
15
2015
3015
```