```markdown
# Task

Miruna and Sonia have invented the following game:

* Miruna thinks of a tree with $N$ nodes (numbered from $1$ to $N$).
* Sonia asks Miruna questions in the form of a triplet of distinct nodes $(A, B, C)$. Miruna needs to calculate which node $D$ has the minimal sum of distances to nodes $A$, $B$, and $C$, and tell Sonia.
* Sonia's goal is to discover the structure of the tree using as few questions as possible.

Given a tree with $N$ nodes, write a program that finds all the edges using the minimum number of questions.

# Interaction
Your program should not implement the `main` function nor use any text file. Instead, it should implement the function
```cpp
std::vector<std::pair<int, int>> solve(int N);
```
which returns a vector with $N - 1$ pairs of values representing the edges of the tree with $N$ nodes and the required structure. Within this function, you can interact with
```cpp
int query(int A, int B, int C);
```
implemented by the committee, which returns the node with the minimal sum of distances to nodes $A$, $B$, and $C$.

# Constraints and clarifications
* The `solve` function will be called at most $T \leq 5$ times within a test.
* $3 \leq N \leq 1 \ 000$

# Scoring

Let $X$ be the number of questions used by the committee's program:
* If your program uses at most $2 \cdot X$ questions, it will receive $100\%$ of the score.
* If your program uses at most $5 \cdot X$ questions, it will receive $50\%$ of the score.

The score for a test will be $0$ if any of the following cases occur:
* Your program uses more than $5 \cdot X$ questions.
* Your program exceeds the maximum execution time per test.
* Your program does not follow the interaction protocol.
* Your program does not correctly "guess" all $T$ trees.

# Example of interaction

Committee: `solve(3)`  
Competitor: `query(1, 2, 3)`  
Committee: `return 3`  
Competitor: `return {{1, 3}, {2, 3}}`  
Committee: `solve(4)`  
Competitor: `query(1, 2, 3)`  
Committee: `1`  
Competitor: `query(1, 2, 4)`  
Committee: `1`  
Competitor: `query(1, 3, 4)`  
Committee: `1`  
Competitor: `return {{1, 2}, {1, 3}, {1, 4}}`
```