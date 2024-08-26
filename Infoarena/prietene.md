## Friends

Given a directed graph with $N$ nodes and $M$ arcs. We say that the node $u$ is super-adjacent with $v$ if there exists a node $t$, different from $u$ and $v$, such that there is an arc from $u$ to $t$ ($u$ is adjacent to $t$) and there is an arc from $t$ to $v$ ($t$ is adjacent to $v$). We call two distinct nodes $x$ and $y$ friends if the set formed from the adjacents and super-adjacents of $x$, different from $x$ and $y$, coincides with the set formed from the adjacents and super-adjacents of $y$, different from $x$ and $y$. The following types of operations are performed on the given graph: $a \ x \ y$ – add an arc from node $x$ to node $y$ $d \ x \ y$ – delete the arc from node $x$ to node $y$ $q \ x \ y$ – answer the question “Are the nodes $x$ and $y$ friends?”

## Task

Given $N$, the number of nodes, $M$, the number of arcs, the $M$ arcs, $OP$, the number of operations and the list of these, perform the operations in the list order and display the answers to the $q$ operations when they appear.

## Input data

The input file `prietene.in` contains on the first line $T$, the number of tests in the file, the following line contains the positive integers $N$ and $M$, separated by a space. On each of the following $M$ lines, there will be two values $x \ y$, separated by a space, with the meaning that there is an arc from node $x$ to node $y$. The following line contains $OP$, the number of operations to be performed on the current test graph. On each of the following $OP$ lines there is an operation, in the form specified in the statement. The subsequent tests in the file have the same format.

## Output data

The output file `prietene.out` will display on each line the answer to the $q$ operations, in the order they appear in the input file. The answer is YES if the nodes in the operation $q$ are friends and NO otherwise.

## Constraints and clarifications

$1 \leq N \leq 150$

$1 \leq M \leq 22500$

$1 \leq OP \leq 730\ 000$

The number of $a$ and $d$ operations will not exceed 22500 per test

The input file does not contain $a$ operations that add existing arcs, nor $d$ operations that delete arcs that do not exist in the graph at that moment.

In a test file, there can be a maximum of 3 graphs with corresponding operations, described as in the input data.

## Example

`prietene.in`
```
1
4 5
1 2
2 1
3 4
3 2
1 4
9
q 1 4
a 4 3
d 3 2
q 1 4
d 1 4
q 2 1
a 4 2
a 1 3
q 1 3
```

`prietene.out`
```
NO
NO
YES
YES
```

## Explanation

In the first operation $q \ 1 \ 4$ the set corresponding to node 4 is the empty set, and the set corresponding to node 1 is $\{2,4,1\} \ - \{1,4\} = \{2\}$, so the answer is NO. We add the arc $(4,3)$ and remove the arc $(3,2)$. In the next operation $q \ 1 \ 4$ the set corresponding to 1 is $\{2,4,1,3\} \ - \{1,4\} = \{2,3\}$ and the set corresponding to 4 is $\{3,4\} - \{1,4\} = \{3\}$, so the answer is NO. We delete the arc $(1,4)$ then, in the next operation $q \ 2 \ 1$ the set of 2 is $\{1,2\}-\{1,2\} = \emptyset$ and the set corresponding to 1 is also $\{1,2\} - \{1,2\} = \emptyset$, so the answer is YES, because both sets are empty. We add the arcs $(4,2)$ and $(1,3)$ then in the last operation $q \ 1 \ 3$ the set of 1 is $\{1,2,3,4\} - \{1,3\} = \{2,4\}$ and the set corresponding to 3 is $\{2,3,4\} - \{1,3\} = \{2,4\}$, so the answer is YES.