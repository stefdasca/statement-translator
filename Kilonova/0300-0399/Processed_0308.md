While cleaning the Museum of Modern Art, Henry found a sculpture made up of $N$ balls numbered with distinct natural numbers from $1$ to $N$, attached to each other by $N-1$ rods. Henry, being observant, realized that the sculpture represents a binary tree with the following properties:

1. Except for the ball at the top of the sculpture (which is attached to the ceiling), each ball $X$ is connected by a rod to another ball $P$ above it. Thus, we will say that $P$ is the parent of $X$.
2. Each ball can have a maximum of $2$ balls attached below it: optionally one to the left (left child) and optionally one to the right (right child).
3. If a ball is numbered with a natural number $X$, then all balls that are attached to it, directly or indirectly through the left rod (left subtree) are numbered with values smaller than $X$, and all balls attached to it, directly or indirectly through the right rod (right subtree) are numbered with values larger than $X$.

As part of the new interactive features of the museum, next to the sculpture is a mobile model of it, also made up of $N$ balls numbered from $1$ to $N$, attached to each other by $N-1$ rods. Although the balls that form the model are connected differently, it follows the same rules ($1$, $2$ and $3$) as the sculpture.

Since he has finished cleaning, Henry is now thinking about modifying some connections in the model so that it has the same form as the sculpture (in other words, for each $X$, $1 \leq X \leq N$, each ball numbered with $X$ in the model should be connected to balls having exactly the same numbers as the balls connected to the ball $X$ in the sculpture). To make things more interesting, Henry is thinking about using only two operations to rearrange the model:

1. Right rotation around the ball numbered $D$: for two balls $B$ and $D$, the parent $P$ (which may or may not exist) of the ball $D$ and the subtrees $A$, $C$ and $E$ (which may or may not exist) connected as shown in figure 1, the connections are redone so that $P, A, B, C, D$ and $E$ are connected as shown in figure 2.
2. Left rotation around the ball numbered $B$: for two balls $B$ and $D$, the parent $P$ (which may or may not exist) of the ball $B$ and the subtrees $A$, $C$ and $E$ (which may or may not exist) connected as shown in figure 2, the connections are redone so that $P, A, B, C, D$ and $E$ are connected as shown in figure 1.

~[rotatii1.png]

For any type of rotation, all other connections between the balls of the model remain unchanged. Upon closer inspection, it can be observed that after any rotation operation, the model still follows rules $1$, $2$, and $3$.

Since Henry is only good at cleaning, he asks you to find a series of rotations that bring the model to the same form as the sculpture.

Input data
==========

The first line of the input file `rotatii.in` will contain a natural number $N$, representing the number of balls that make up the sculpture. The next $N$ lines will contain the description of the model. Thus, for each $i$, $1 \leq i \leq N$, on line $1 + i$ there will be two natural numbers separated by a space $ML[i]$, $MR[i]$, representing the left child and the right child of the ball labeled with $i$ in the model ($ML[i]$ and/or $MR[i]$ can be $0$ in case the ball $i$ does not have the corresponding child). Similarly to the description of the model, the next $N$ lines will contain the description of the sculpture. Thus, for each $i$, $1 \leq i \leq N$, on line $1 + N + i$ there will be two natural numbers separated by a space $SL[i], SR[i]$, representing the left child and the right child of the ball labeled with $i$ in the sculpture ($SL[i]$ and/or $SR[i]$ can be $0$ in case the ball $i$ does not have the corresponding child).

Output data
===========

The first line of the output file `rotatii.out` will contain a number $K$, representing the number of rotations required to bring the model to the same form as the sculpture. On the next $K$ lines, in order, the operations performed will be displayed in the form:
- $1 \ D$, meaning that a right rotation is performed around the ball $D$ in the model (see figure);
- $2 \ B$, meaning that a left rotation is performed around the ball $B$ in the model (see figure).

There will be exactly one space between $1$ and $D$, and between $2$ and $B$.

Constraints and clarifications
=======================

* $1 \leq N \leq 1 \ 000 \ 000$
* $K$ does not necessarily need to be minimal.
* For $50\%$ of the tests, $1 \leq N \leq 2 \ 000$
* $70\%$ of the points will be awarded for a test if the operations displayed in the output file bring the model to the form of the sculpture, and the program runs within the indicated time and memory limits, but $K > 2 \cdot N$.
* $100\%$ of the points will be awarded for a test if, in addition, $K \leq 2 \cdot N$.

# Example
`rotatii.in`
```
5
0 0
1 3
0 0
2 5
0 0
0 0
1 5
0 0
3 0
4 0
```

`rotatii.out`
```
2
1 4
2 4
```

Explanations
---
First, a right rotation will be performed around $4$, then a left rotation around $4$, as shown in the figure

~[rotatii2.png]