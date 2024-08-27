
An $N$-node tree with root at node 1 is given, where each node **i** has an associated integer value **Vi**. A downward path in the tree is defined as any elementary chain that connects a node **A** with another node **B** from the subtree of **A**. The task is to determine how many downward paths exist for a given sum **S**, such that the sum of the values of the nodes along the path is equal to **S**.

### Task

Determine the number of downward paths in the tree such that the sum of the node values along the path is equal to **S**.

### Input data

The input file `arbore3.in` will contain on the first line the numbers **N** and **S**. The next **N** lines will each contain two numbers: line **i+1** will contain **Ti** and **Vi**, representing the parent of node **i** in the tree and the value associated with node **i**, respectively. For convenience, it is considered that the parent of node 1 (the root) is 0.

### Output data

In the output file `arbore3.out`, you will print a single value representing the number of downward paths with the sum of the node values equal to **S**.

### Constraints and clarifications

- $1 \leq N \leq 1\ 000\ 000$
- The numbers **S** and **Vi** are 32-bit signed integers.
- For any downward path, the sum of the values of the nodes along the path will fit within a 32-bit signed integer.
- Node 1 (the root) is the only node that appears with parent 0.

### Example

Read the data from the original problem statement

#### Explanation
The 3 chains are (1, 2, 3), (4), (5, 6, 8). Notice that although the chain (8, 6, 7) has a sum of 5, it is not counted because it is not a downward chain.
