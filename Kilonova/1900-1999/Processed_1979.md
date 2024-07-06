**Princess with Green Eyes**

Princess Rafaela from the kingdom of trees needs to collect taxes from all citizens of the kingdom. Formally, a tree with $N$ nodes is given, and each node initially contains a number given by the citizens. Rafaela would like to place the capital of the kingdom in one of the nodes, but due to the fluctuation of the number of citizens in the kingdom, she encountered a problem she would like to solve using a computer. Therefore, she will perform certain operations on the tree to eventually make a decision. The operations are of type update/query and are described below:

* `U nr id` – the character $U$ followed by two integers, representing an update operation, and means: in the node with index $id$, a number of $nr$ citizens appears (if the number is positive), or a number of $nr$ citizens disappears (in case the number is negative).
* `Q id` – the character $Q$ followed by an integer, representing a query operation to which you must respond: if we set the capital of the kingdom in the node with index $id$, then which edge would be the most used (on which the largest number of citizens travel) if all citizens decide to go from the nodes they are in to the capital? As there can be multiple such edges, Rafaela is satisfied to know only the number of citizens traveling on one of the most used edges.

# Task

Given a tree with $N$ nodes, the initial number of citizens in each node, and $Q$ update/query operations, you need to respond to the query operations.

# Input data

The input file `rafaela.in` contains the first line which contains two natural numbers $N$ and $Q$, separated by a space, representing the number of nodes in the tree and the number of operations performed, respectively. The following $N-1$ lines contain pairs of two natural numbers $a$ and $b$, separated by a space, representing an edge ($a$ and $b$ represent two nodes in the tree). On the following line are $N$ natural numbers separated by a space, the number at position $i$ representing the number of citizens initially in node $i$. On the following $Q$ lines are update/query operations, an update operation being coded by the character $U$, and a query operation by the character $Q$. In the case of an update operation, on the same line follow two integers $nr$ and $id$, separated by a space, where $nr$ represents the number of citizens appearing/disappearing in node $id$. In the case of a query operation, on the same line follows a natural number $id$, which represents the node that will become the capital and for which you are asked to find the answer.

# Output data

The output file `rafaela.out` will contain on each line one integer, representing the answers (in order) for each query operation in the input file.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq Q \leq 200\ 000$
* It is guaranteed that the total number of citizens, after each update operation, fits within 32 signed bits.
* It is guaranteed that the number of citizens in a node, after each update operation, is a positive number (greater than or equal to $0$).

# Example

`rafaela.in`
```
5 5
1 2
2 3
2 4
4 5
1 2 3 2 3
Q 2
U 10 3
Q 2
U -5 3
Q 1
```

`rafaela.out`
```
5 
13
15
```

## Explanation

For the first query, the answer is $5$, the most intensely used edge being the one between nodes $2$ and $4$ (all citizens from nodes $4$ and $5$ move towards capital $2$).

For the second query, the answer is $13$, the most used edge being the one that connects node $2$ to node $3$ (node $3$ contains $13$ citizens after the update operation).

For the third query, the answer is $15$, the most used edge being the one between node $1$ and node $2$.