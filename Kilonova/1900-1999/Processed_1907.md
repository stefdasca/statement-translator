> "Dogs talk."

It was Traian's birthday recently, and he received a graph with $N$ nodes as a gift. Initially, each node was in a connected component by itself. But then, Traian's dog came and asked him $Q$ questions of the following form:
* $1 \\ x \\ y$: Add to your graph the edges $(x, x + 1), (x + 1, x + 2), ..., (y - 1, y)$
* $2 \\ x \\ y$: Tell if the nodes $x$ and $y$ are in the same connected component.

# Task

Answer Traian's dog's questions.

# Input data

The first line contains $N$ and $Q$, representing the number of nodes in the graph and the number of questions, respectively. The next $Q$ lines contain three numbers $t_i, x_i, y_i$, where $t_i$ represents the type of question, and $x_i$ and $y_i$ are two nodes in the graph.

# Output data

On line $i$, print the answer to the $i$-th question of type $2$. This answer can be either `Yes` or `No`, depending on the answer.

# Constraints and clarifications

* $1 \\leq N, Q \\leq 10^6$
* If in a question of type $1$, an edge has already been added, Traian will not add it again.
* For questions of type $2$, it is not guaranteed that $x \\leq y$

| # | Score | Constraints | 
| - | ----- | ------------ |
| 1 | 10 | $N \\leq 100, Q \\leq 100 $ |
| 2 | 10 | $N \\leq 1 \ 000, Q \\leq 100$ |
| 3 | 10 | $N \\leq 10^4, Q \\leq 10^4$ |
| 4 | 20 | $N \\leq 10^5, Q \\leq 10^5$ |
| 5 | 50 | Without additional constraints |

# Example

`stdin`
```
7 6
1 4 7
2 5 3
1 3 6
1 6 7
2 7 1
2 3 4
```

`stdout`
```
No
No
Yes
```

## Explanation

After question $1$, the graph will look like this:
~[joingraf1.png|align=center|width=300px]

The answer to question $2$ is no, because $3$ and $5$ are not in the same connected component.
After question $3$, the graph will look like this:
~[joingraf2.png|align=center|width=300px]

After question $4$, the graph will look like this:
~[joingraf2.png|align=center|width=300px]

The answer to question $5$ is no, because $1$ and $7$ are not in the same connected component.
The answer to question $6$ is yes, because $3$ and $5$ are in the same connected component.