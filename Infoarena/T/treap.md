## Treap

Somewhere in a parallel universe, Piroman started to love water instead of fire, as usual. However, he hasn't changed much... he still likes treaps, as in the problem Metro. Considering that the A.G.M committee would be embarrassed if they let the third edition pass without a problem involving treaps, he decided to take care of the image of all his colleagues. Piro, a refined boy otherwise, does not want to be the most disliked member of the committee, so he will take a brief incursion with you into the secrets of the treap. A tree is a connected, acyclic undirected graph. A rooted tree is a tree which has a fixed root. A binary tree is a tree with the property that each node in its composition has at most two children. A binary search tree is a binary tree with the following properties:
- each node has an associated value
- for each node, the left subtree contains values smaller than or equal to the node's value, and the right subtree contains values strictly greater than the node's value

A max-heap is a binary tree with the property that each node has an associated value plus the associated value of a node is greater than or equal to the values of its children. A treap is a tree with the property that each node has two associated values: key and priority. If we look only at the keys of the nodes, ignoring the priorities, then it is a binary search tree. If we look at the priorities of the nodes, ignoring the keys, then it is a max-heap. Given a binary tree with $N$ nodes, rooted at node $1$, you need to determine which subtrees have the property of a treap.

## Input data

The input file `treap.in` will contain the number $N$ on the first line. The next $N-1$ lines will contain pairs of 2 natural numbers $x$, $y$ with the property that there is an edge between nodes $x$ and $y$ in the tree. The next line will contain $N$ numbers, the $i$-th of them being $KEY_i$ (i.e., the key of the respective node). The next line will contain another $N$ numbers, the $i$-th of them being $PRIO_i$ (i.e., the priority of the respective node).

## Output data

In the output file `treap.out` a sequence of $N$ numbers will be printed as follows: the $i$-th number in the sequence will be $1$ if the subtree rooted at node $i$ has the property of a treap and $0$ otherwise. The numbers will be printed with spaces between them.

## Constraints and clarifications

$1 \leq N \leq 150\ 000$  
$1 \leq KEY_i \leq 10^9$  
$1 \leq PRIO_i \leq 10^9$  
The tree is considered to be rooted at node $1$  
At the end of the output file there is `\n`, not a space  
A subtree rooted at a node that has no children is considered a leaf and is obviously a treap  
It is not guaranteed that the generated priorities are random, the treap can have the most diverse forms.

## Example

`treap.in`
```
3
1 2
1 3
5 5 7
100 9 1
```

`treap.out`
```
1 1 1
```

`treap.in`
```
3
1 2
1 3
5 8 7
100 9 1
```

`treap.out`
```
1 0 1
```

`treap.in`
```
3
1 2
2 3
2 1 3
3 2 1
```

`treap.out`
```
1 0 1
```