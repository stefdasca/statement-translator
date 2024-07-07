Two people, whom we will call Costel and Costin to maintain their anonymity, participate in the informatics team. Costel is part of the committee, while Costin is a participant.

The two made a rather bizarre agreement: in exchange for material benefits, Costel will help Costin achieve $100$ points on one of the problems. Knowing that all the problems in the team have an output of a single number, Costin has already chosen $50$ preferred numbers $R_i$, which he has given to Costel. Now, for a problem, Costel has to generate $50$ tests for which the answers are the $50$ numbers chosen by Costin.

The problem chosen by Costel to implement the plan is as follows: â€œGiven a tree (an undirected, acyclic, connected graph) consisting of $N$ nodes, $1 \leq N \leq 400$. For it, determine **the number of maximum independent sets of nodes for the given tree**. A maximum independent set of nodes is defined as a set of nodes with the maximum cardinality such that no two nodes in the set are connected by an edge in the original tree.â€

Due to an unfortunate accident that prevents him from continuing, Costel has tasked you to continue the plan. Construct $50$ trees for which, for each tree $i$, the answer to the chosen problem is the number $R_i$.

# Constraints and clarifications
This problem is output-only. Therefore, you do not need to upload a source that displays the answer. You will upload the output files corresponding to the input files present on the evaluation interface. Each input file has the following format:

* line $i \ (1 \leq i \leq 50)$: $R_i$, a positive integer, ($1 \leq R_i \leq 10^{18}$), representing the desired answer for the test number $i$.

In the corresponding output file, you must display the form of $50$ trees such that for the tree number $i$ the answer to the problem proposed by Costel is $R_i$. The trees will be displayed sequentially in the output file. An individual tree will be displayed as follows:

* line $1$: an integer $N$, $1 \leq N \leq 400$, representing the size of the tree.
* line $2 + i$ ($0 \leq i \leq N - 2$): $a$, $b$ two integers $0 \leq a, b \leq N - 1$ ($a \neq b$), indicating the existence of an edge between nodes $a$ and $b$.

It is guaranteed that there is a solution for all tests.

# Scoring
For a test, the maximum score is obtained if for each of the $50$ trees, the answer to the problem proposed by Costel corresponding to tree $i$ is $R_i$. Additionally, each tree displayed in the input file must contain at most $400$ nodes.

## Subtask 1 (13 points)
* $1 \leq R_i \leq 20$

## Subtask 2 (6 points)
* $1 \leq R_i \leq 100$

## Subtask 3 (5 points)
* $1 \leq R_i \leq 200$

## Subtask 4 (7 points)
* $1 \leq R_i \leq 10^{18}$
* $R_i$ is a power of $2$

## Subtask 5 (50 points)
* $1 \leq R_i \leq 2 \cdot 10^9$

## Subtask 6 (19 points)
* $1 \leq R_i \leq 10^{18}$

# Example

`Input`
```
3
2
```

`Output`
```
7
0 1
0 2
2 3
1 4
4 5
4 6
8
0 1
0 2
0 3
3 4
5 4
5 6
5 7
```

## Explanation

This example is only for demonstration purposes as it contains only $2$ numbers in the input file. The official tests contain $50$ numbers each.

For the first example, a tree must be generated that has exactly $3$ maximum independent sets. For the generated tree, the $3$ possible sets that can be chosen are those in the following images (the nodes of a set are those with a bold edge):â€

~[test.png]