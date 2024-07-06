Inspired by Jules Verne's novel "Five Weeks in a Balloon", Ștefan decides to embark on an adventure himself with a hot air balloon over Africa. Unfortunately, he is caught in a sandstorm that causes him to crash in the great Sahara Desert. Until help arrives, Ștefan is forced to spend the night alone in the desert. Afraid of scorpions, he decides to recycle the planks left from the basket of the balloon to build a shelter.

Ștefan wants to build a tree-shaped shelter that has plenty of space and is far from the ground. To decide how good such a shelter is, Ștefan decides to allocate a score equal to the sum of the distances of the leaves from the root.

# Task

You are given the numbers $N$ and $C$ representing the number of planks (nodes) that Ștefan has at his disposal, respectively the number of tasks that must be solved, as well as $N - 1$ pairs of numbers representing the nails (edges) between the planks (nodes) of the tree.
**Since the plank numbered 1 has the largest width, it will always be used as the root of the tree.**

If $C = 1$, Ștefan wants to know what the current score of the tree formed by the planks left from the balloon basket is.
The score is calculated by summing for each leaf its distance from the root (node number 1).
If $C = 2$, Ștefan wants to know what is the maximum score that a tree constructed from $N$ planks could have if they were arranged optimally.
If $C = 3$, Ștefan wonders in how many ways a tree with the maximum score can be obtained. Two trees are considered different if there is at least one node whose father differs between the two trees.

# Input data

The first line of the input file `scorpion.in` contains two integers, $N$ and $C$, representing the number of planks and the number of tasks that must be solved.
The next $N - 1$ lines in the input file contain $N - 1$ pairs of numbers $u_i$ and $v_i$, one pair per line, with the meaning that there is an edge between nodes $u_i$ and $v_i$.

# Output data

The first line of the output file `scorpion.out` will contain a single integer, the result of the task that must be solved.
If $C = 1$, it will contain the score of the initial tree.
If $C = 2$, it will contain the maximum score of a tree with $N$ nodes.
If $C = 3$, it will contain the number of distinct trees with $N$ nodes that have the maximum score. Because the result can be very large, it is required to display it modulo $10^9 + 7$.

# Constraints and clarifications

* $2 \leq N \leq 300\ 000$;
* $1 \leq u_i, v_i \leq N$;
* $C = 1, 2,$ or $3$;
* The node numbered $1$ will always be the root of the tree;
* It is guaranteed that the initial graph is a tree;
* Two trees are considered different if the parent of at least one node differs between the two trees.

|#|Points|Constraints|
|-|-|-----------|
|1|20|$C = 1$|
|2|30|$C = 2$|
|3|50|$C = 3$|

# Example 1

`scorpion.in`
```
5 1
1 2
1 3
1 4
1 5
```

`scorpion.out`
```
4
```

## Explanation

All $4$ leaves are at a distance of $1$ from the root. $1 + 1 + 1 + 1 = 4$

# Example 2

`scorpion.in`
```
5 2
1 2
1 3
1 4
1 5
```

`scorpion.out`
```
6
```

## Explanation

One of the configurations that leads to the maximum score is the one that has the edges $(1, 2), (2, 3), (3, 4), (3, 5)$. Leaves $4$ and $5$ will be at a distance of $3$ from the root, resulting in a score of $3 + 3 = 6$.

# Example 3

`scorpion.in`
```
5 3
1 2
1 3
1 4
1 5
```

`scorpion.out`
```
16
```

## Explanation

One of the configurations that leads to the maximum score is presented in Example 2.