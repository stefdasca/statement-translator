
~[appletree.jpg|align=right|width=30%]

An apple tree can be represented as a tree of $N$ nodes, where each node is an apple. Good apples are marked with $1$, while rotten apples are marked with $0$. There are $Q$ events of the following types:
* $1 \ l \ r$ - all apples in the range $[l, r]$ become **good**;
* $2 \ l \ r$ - all apples in the range $[l, r]$ become **rotten**;
* $3 \ l \ r$ - all apples in the range $[l, r]$ change their state $(0 \rightarrow 1, 1 \rightarrow 0)$.

# Task

Farmer John wonders after each event which two good apples $A$ and $B$ are such that the number of nodes located on the path between $A$ and $B$ is maximum.

# Input data

The first line contains the numbers $N$ and $Q$, with the significance described in the statement.  
The next $N-1$ lines contain the edges of the tree.  
The next line contains a binary string of length $N$, $S_i$ representing the state of apple $i$ ($1$ = **good**, $0$ = **rotten**).  
The next $Q$ lines contain the numbers $t$, $l$, and $r$, representing operation $i$.

# Output data

Print $Q$ lines, line $i$ containing the numbers $a_i$ and $b_i$, representing the good apples located at the maximum distance from each other. If there is not at least one good apple, print `0 0`.

# Constraints and clarifications

* $1 \leq N, Q \leq 100 \ 000$
* If there are multiple solutions, any of them can be printed
* The chosen apples do not have to be distinct
* If there is no good apple, print `0 0`
* It is recommended to use fast I/O
* If you have issues with the constant factor, you can try [pragmas](https://codeforces.com/blog/entry/96344)
* For tests worth $5$ points: $N, Q \leq 20$
* For other tests worth $5$ points: $N, Q \leq 200$
* For other tests worth $5$ points: $N, Q \leq 1 \ 000$
* For other tests worth $11$ points: the tree is of the form $1 - 2 - ... - N$
* For other tests worth $10$ points: updates of type $2$ or $3$ do not exist
* For other tests worth $14$ points: updates of type $3$ do not exist
* For other tests worth $19$ points: $N, Q \leq 60 \ 000$

# Example

`stdin`
```
9 7
1 2
1 3
2 7
7 8
7 9
3 4
3 5
3 6
100011101
1 2 3
2 5 7
3 1 9
3 1 4
3 2 6
1 1 9
2 1 9
```

`stdout`
```
6 9
3 9
5 8
5 8
4 8
8 5
0 0
```

## Explanation

Initially, the tree looks like this:  
~[1.png|width=30%]

### After the first event, the tree looks like this:  
~[2.png|width=30%]

In this case, one solution is $6 \ 9$, being at a distance of $5$. Another solution could have been $5 \ 9$.

### After the second event, the tree looks like this:  
~[3.png|width=30%]

In this case, the only solution is $3 \ 9$, being at a distance of $4$.

### At the end of all events, the tree looks like this:  
~[0.png|width=30%]

In this case, there is no good apple, so the solution will be $0 \ 0$.