Ana has a very beautiful tree... So beautiful, that she tries to keep it for herself. However, Bogdan is a very good friend of Ana, and having heard about this beautiful tree, he managed to convince Ana to reveal some nodes from it. 

Ana's tree consists of $N$ nodes, and the $i$-th node in the tree has a beauty coefficient $v_i$. Ana will send Bogdan photos of $K$ out of the $N$ nodes. Then, she will pretend that these nodes have been removed from the tree along with their edges. After that, she will look at each remaining connected component and calculate the sum of the beauty coefficients of the nodes in it. Consequently, the selection cost of those $K$ nodes is defined as the maximum value of these sums.

# Task

However, Ana still wants the more beautiful parts of the tree to remain unseen. For this reason, she seeks a selection of exactly $K$ nodes that minimizes the selection cost. Not being so sure about the optimal selection, she provides you with a description of how the tree looks, along with its beauty coefficients, and asks you to find the minimum selection cost and a selection that achieves it.

# Input data

The first line contains the numbers $N$ and $K$, with the meanings described above. The second line will contain $N$ numbers, the $i$-th representing the beauty coefficient of the node $i$. The next $N$ lines will contain two numbers $u$ and $v$, indicating that there is an edge between nodes $u$ and $v$.

# Output data

The first line of the program must print the minimum selection cost that can be obtained. The second line of the program must print $K$ numbers, representing the nodes in the selection. In case there are multiple selections that achieve this cost, any of them can be printed.

# Constraints and clarifications

* $1 \leq N \leq 10^6$
* $0 \leq K \leq N$
* $0 \leq v_i \leq 10^9$
* If there are no remaining connected components after selecting the nodes, the selection cost is considered to be $0$.
* For tests worth $16$ points, $N \leq 10$.
* For other tests worth $36$ points, $N \leq 1\ 000$.
* If the correct cost is displayed, but the selection shown does not obtain this cost, $50 \%$ of the score on the respective test will be awarded.

# Example 1

`arborele_frumos.in`
```
10 5
98 81 0 16 82 86 14 16 25 43
2 1
3 2
4 1
5 3
6 5
7 4
8 5
9 6
10 2
```

`arborele_frumos.out`
```
30
6 5 10 2 1
```

## Explanation

In the first example, a minimum cost selection is the one formed from the nodes $1$, $2$, $5$, $6$, $10$. After removing them, the following connected components remain:

* The component formed by nodes $4$ and $7$, with a cost of $30$;
* The component formed by node $3$, with a cost of $0$;
* The component formed by node $8$, with a cost of $16$;
* The component formed by node $9$, with a cost of $25$.

The maximum among the costs is $30$.

# Example 2

`arborele_frumos.in`
```
10 0
77 21 22 64 90 29 62 34 25 24
2 1
3 1
4 1
5 4
6 2
7 4
8 2
9 5
10 2
```

`arborele_frumos.out`
```
448

```

## Explanation

In the second example, $K = 0$, so we will not select any nodes. The selection cost becomes equal to the sum of the beauty coefficients in the tree, that is, $448$.