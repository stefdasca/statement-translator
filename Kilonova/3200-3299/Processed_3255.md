
~[cat.jpg|align=right]

# Task

To save his wife Maki, Sushi Cat has arrived in an abstract non-Euclidean vector space. In this space, he discovers a peculiar structure - a tree. This tree has $N$ nodes numbered from $1$ to $N$, is rooted at node $1$, and each edge has an associated weight. Sushi Cat "falls" from the root towards the leaves. When he reaches a node with more than one child, he can fall into any child with a probability proportional to the value of the edge to that child. For example, if a node has two children and the edge to the first child has cost $1$, while to the other child it is $3$, then there is a probability of $\frac{1}{1+3}$ that he continues to the first child, and $\frac{3}{1+3}$ to the second child.

Eventually, Sushi Cat arrives at one of the leaves. But he does not stop there! The tree is rerooted at the leaf where he just arrived, and the game repeats for another $K$ times. In the end, he is too dizzy to know where he stopped. So he asks you to determine for each leaf of the tree (including the root, if it has only one neighbor), the probability that he stopped there at the end of the adventure.

# Input data

The first line contains the integers $N$ and $K$. The next $N - 1$ lines contain triplets of the form $(u, v, w)$, indicating that there is a bidirectional edge from node $u$ to node $v$ with weight $w$.

# Output data

For each leaf of the tree in increasing order (including the root, if it has only one neighbor), you need to print the probability that Sushi Cat stopped at that leaf. If the required probability is a real number of the form $\frac{p}{q}$, you need to print $p \cdot q^{-1} \mod 10^9 + 7$, where $q^{-1}$ denotes the [modular inverse](https://edu.roalgo.ro/mediu/modular-inverse/#ce-este-inversul-modular) of $q$ modulo $10^9 + 7$.

# Constraints and clarifications

* $2 \leq N \leq 100$;
* $0 \leq K \leq 10^{18}$;
* $1 \leq w \leq 10$;
* For tests worth $22$ points, $K=0$;
* For other tests worth $6$ points, $K=1$;
* For other tests worth $12$ points, the tree is a chain;
* For other tests worth $29$ points, $K \leq 3 \cdot 10^4$;
* For other tests worth $31$ points, there are no additional restrictions.

# Example 1

`stdin`
```
5 0
1 2 1
2 3 2
3 4 1
3 5 2
```

`stdout`
```
0 
333333336 
666666672
```

## Explanation

~[graph.png|width=15%]

This is the representative tree for the example. Sushi Cat will fall from node $1$ and will reach node $3$ with probability $1$. From there, he has a probability of $\frac{1}{3}$ to continue to $4$ and $\frac{2}{3}$ to continue to $5$. Therefore, the result is as follows:
* For leaf $1$, probability $0$;
* For leaf $4$, probability $\frac{1}{3}$, so we will display $1 \cdot 3^{-1} \mod 10^9 + 7 = 333333336$
* For leaf $5$, probability $\frac{2}{3}$, so we will display $2 \cdot 3^{-1} \mod 10^9 + 7 = 666666672$

# Example 2

`stdin`
```
5 1234576
1 2 1
2 3 2
3 4 1
3 5 2
```

`stdout`
```
701387956
456084865
842527194
```
