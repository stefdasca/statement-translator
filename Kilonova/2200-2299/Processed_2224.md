```markdown
# Task

A new game called "Neconex" has been circulating on the internet for some time. The game can be played by two people using a graph that is not connected. The two players move alternately. A move consists of adding an edge between two distinct nodes that do not already have an edge between them. The player who causes the graph to become connected, meaning all nodes belong to the same connected component, loses the game.

Instead of preparing for the “National Informatics Team,” Ţirbi and Birţi play this game, and Ţirbi always moves first. Since they are both quite good at algorithms, they play optimally.

# Task

Given $T$ graphs, determine whether Ţirbi has a winning strategy for each graph.

# Input data

The input file `neconex.in` contains on the first line the number $T$, followed by the description of each graph. The description of each graph starts with a line containing $N$ and $M$ (representing the number of nodes and the number of edges of the graph), and the following $M$ lines contain two natural numbers $A$ and $B$ representing an edge between nodes $A$ and $B$.

# Output data

The output file `neconex.out` contains $T$ lines, one for each graph in the input file. Line $i$ will contain $1$ if Ţirbi has a winning strategy and $0$ otherwise.

# Constraints and clarifications

* $1 \leq T \leq 31$
* $2 \leq N \leq 20\ 000$
* $0 \leq M \leq 20\ 000$
* It is guaranteed that none of the graphs in the input file are connected.
* Optimum play means that both players try to win.
* For $15\%$ of the tests $M = 0$.
* For $30\%$ of the tests $T \leq 13$ and $N \leq 20$.
* For $60\%$ of the tests $N \leq 1\ 000$.

# Example

`neconex.in`
```
3
4 1
1 2
5 2
2 1
4 5
7 0
```

`neconex.out`
```
1
0
1
```
```